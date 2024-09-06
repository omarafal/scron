#!/bin/bash

which crontab 1>> ./scron.log 2>&1
doescron=$?

if [ ! $doescron -eq 0 ] 
#if which crontab >> ./scron.log 2>&1
then
   echo "crontab is not installed."
   echo "Would you like to install? (Y/n)"
fi

