#!/bin/bash

#
# Globals
#
COLQUESTION="\u001b[36m"
COLRESET="\u001b[m"
COLINFO="\u001b[37m"

echo -e "${COLINFO}Installing dependencies...${COLRESET}"

# Install python pre-reqs
2>/dev/null 1>/dev/null python3 -m pip install pyyaml

# if learner doesn't enter name, default will be set in dialog.py
echo -e "${COLQUESTION}Please enter your first name:${COLRESET}"
read FIRSTNAME
echo $FIRSTNAME > /tmp/firstname.txt

echo -e "${COLINFO}You are all set! Click on 'CONTINUE'.${COLRESET}"
