#
# Globals
#
DEBUG=false
GITHUB="github.dxc.com"
GITHUBAPIURL="https://${GITHUB}/api/v3"
COLQUESTION="\u001b[36m"
COLINFO="\u001b[37m"
COLLOGS="\u001b[35m"
COLRESET="\u001b[m"
REPO=pet-clinic
WELCOME_URL=https://github.dxc.com/pages/GDO-CTO/Katacoda/katacoda/welcome/

if [ "$DEBUG" = false ] ; then
  CURL_NODEBUG="-sS"
fi

if [ "$1" == "-s" ] ; then
  HIDE_PAT="-s"
fi

#
# Ask for GitHub PAT
#
echo -e "${COLQUESTION}Please enter your ${GITHUB} Personal Access Token:${COLRESET}"
read ${HIDE_PAT} TOKEN
export TOKEN

echo -e "${COLLOGS}Fetching your details from GitHub...${COLRESET}"

SHORTNAME=$(curl ${CURL_NODEBUG} -H "Authorization: token ${TOKEN}" -X GET ${GITHUBAPIURL}/user | jq -r '.login')
export SHORTNAME
echo $SHORTNAME > /tmp/shortname.txt
echo $TOKEN >> /tmp/shortname.txt

EMAIL=$(curl ${CURL_NODEBUG} -H "Authorization: token ${TOKEN}" -X GET ${GITHUBAPIURL}/user | jq -r '.email//empty')
if [ -z "$EMAIL" ]; then
  EMAIL=${SHORTNAME}@dxc.com
fi
export EMAIL

git config --global user.email "${EMAIL}"

# Check if repository already exists and properly populated
echo -e "${COLLOGS}"
curl ${CURL_NODEBUG} -H "Authorization: token $TOKEN" -X GET ${GITHUBAPIURL}/repos/$SHORTNAME/$REPO/contents/Jenkinsfile | grep "Not Found"
REPO_DOES_NOT_EXIST=$?
if [ $REPO_DOES_NOT_EXIST -eq 0 ]; then
  echo -e "${COLRESET}> I'm confused..."
  echo -e "> I was expecting to find the $REPO repository under your GitHub username and I didn't, or the content does not look right."
  echo -e "> That must be me. But just in case:"
  echo -e "> - Close this Katacoda window: the environment will expire soon and you need ample time to complete the module"
  echo -e "> - Go through the Welcome module which will set everything up for you:"
  echo -e "> $WELCOME_URL"
  exit 1
fi

#
# Add Katacoda Jenkins URL
KatacodaJenkinsUrl=`curl ${CURL_NODEBUG} "https://katacoda.com/metadata/generate-url?port=8080&ip=$(ip addr show ens3 | grep -Po 'inet \K[\d.]+')"`
url="https://${KatacodaJenkinsUrl}"
echo $url >> /tmp/shortname.txt
#
# 
# Clone Pet Clinic locally
#
echo -e "${COLINFO}Cloning $REPO Git repository...${COLRESET}"
echo -e "${COLLOGS}"
cd ~
rm -fR $REPO
git clone https://${SHORTNAME}:${TOKEN}@${GITHUB}/${SHORTNAME}/${REPO}.git
echo -e "${COLRESET}"

#
# Remove existing web hook
#
echo -e "${COLINFO}Configuring your GitHub $REPO repository...${COLRESET}"
echo -e "${COLLOGS}"
curl ${CURL_NODEBUG} -H "Authorization: token $TOKEN" -X GET ${GITHUBAPIURL}/repos/$SHORTNAME/$REPO/hooks | grep id | cut -d ":" -f2 | cut -c 1-6> ids.txt

filename="ids.txt"

remove_existing_webhook()
{
while read -r line
do
    name="$line"
        curl ${CURL_NODEBUG} -H "Authorization: token $TOKEN" -X DELETE ${GITHUBAPIURL}/repos/$SHORTNAME/$REPO/hooks/"$line"
done < "$filename"
}
remove_existing_webhook

#
# Bring up Jenkins
#
bringing_up_jenkins()
{
echo -e "${COLINFO}Bringing up Jenkins...${COLRESET}"
echo -e "${COLLOGS}"
docker pull devopsdojo/jenkins-yb:latest
docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/shortname.txt:/tmp/shortname.txt devopsdojo/jenkins-yb:latest
}
bringing_up_jenkins

#
# Configure Web hook
#
adding_webhook()
{
echo -e "${COLINFO}Updating GitHub web hook to point to Katacoda Jenkins...${COLRESET}"
echo -e "${COLLOGS}"
JenkinsUrl=`curl ${CURL_NODEBUG} "https://katacoda.com/metadata/generate-url?port=8080&ip=$(ip addr show ens3 | grep -Po 'inet \K[\d.]+')"`

curl ${CURL_NODEBUG} -H "Authorization: token $TOKEN" -X POST --data '{"name": "web","active": true,"events": [ "push", "pull_request" ], "config":{"url": "https://'"$JenkinsUrl"'/github-webhook/","content_type":"json"}}' ${GITHUBAPIURL}/repos/$SHORTNAME/$REPO/hooks
}
adding_webhook

#
# Create dashboard tab to point to GitHub
#
echo -e "${COLINFO}Preparing tab to link to ${GITHUB}...${COLRESET}"
echo -e "${COLLOGS}"
sed -i "s/github_url/${GITHUB}\/${SHORTNAME}\/pet-clinic/g" ~/nginx/index.html
docker run --name nginx -p 9876:80 -v /root/nginx:/usr/share/nginx/html:ro -d nginx 


#
# Wait for Jenkins to be up
#
wait_for_jenkins()
{
  echo -e "${COLINFO}Waiting for Jenkins to come up...${COLRESET}"
  echo -e "${COLLOGS}"

  for i in {1..60}
  do
    if (( $( curl -s ${JenkinsUrl} | grep -c "Authentication" ) > 0)); then
      touch /tmp/jenkins_ready
      break
    fi
    echo "Retry $i..."
    sleep 5s
  done
}
wait_for_jenkins

echo -e "${COLINFO}You are all set! Click on 'CONTINUE'.${COLRESET}"
