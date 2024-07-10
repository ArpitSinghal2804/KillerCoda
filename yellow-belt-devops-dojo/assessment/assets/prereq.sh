#!/bin/bash

COLQUESTION="\u001b[36m"
COLRESET="\u001b[m"
COLINFO="\u001b[37m"

# note ensuring pip version associated with python version is used 
# using python3 command with -m option to import the module
echo -e "${COLINFO}Installing dependencies...${COLRESET}"
2>/dev/null 1>/dev/null python3 -m pip install pyyaml

# if learner doesn't enter name, default will be set in dialog.py
echo  "Please enter your first name:"
read FIRSTNAME

echo $FIRSTNAME > /tmp/firstname.txt

#echo "Hello" + $FIRSTNAME
