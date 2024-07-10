![Dan](../../assets/yellow-belt-devops-dojo/test-driven-development/dan.png)

> @Paulo, we are done. Following TDD, we wrote unit tests first - which failed initially, then the code, then we iterated to make all test pass.

![Santhosh](../../assets/yellow-belt-devops-dojo/test-driven-development/santhosh.png)

> I checked the user story, and we have covered all the acceptance criteria. This is ready for you to review @Paulo: ready to go?

![Paulo](../../assets/yellow-belt-devops-dojo/test-driven-development/paulo.png)

> Looks good to me. Let's ask directly the business and give Brenda the button to deploy.

# Steps

* In the pull request, ask for Brenda to review by adding a comment: `/brenda, can you please review?`{{copy}}
* Brenda will review and merge the pull request.
* Verify that the user story in GitHub is closed, with a reference to the pull request.
* Navigate to <a href="https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/blue/organizations/jenkins/pet-clinic/activity" target="jenkins">Jenkins</a> and verify that a new build is triggered, as merging the pull request onto the `master` branch triggered Jenkins again.

Congratulations, the changes have been merged to master and are now live!
