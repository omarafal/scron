#!/bin/bash

# TRY TO FIND A REPLACEMENT FOR REPTITIVE WHICH COMMANDS

which crontab >> ./scron.log 2>&1
doescron=$?

if [ ! $doescron -eq 0 ] 
#if which crontab >> ./scron.log 2>&1
then
	echo "crontab is not installed."
	read -p "Would you like to install? (Y/n): " install
   
	if [[ $install == 'Y' ]]
	then
		# check package managers (apt then pacman)
		echo "Checking available package managers..."
		
		which apt >> ./scron.log 2>&1
		doesapt=$?
		if [ $doesapt -eq 0 ]
		then
			echo "Installing crontab."
			sudo apt -y install crontab
		else
			which pacman >> ./scron.log 2>&1
			doespac=$?
			if [ $doespac -eq 0 ]
			then
				echo "Installing crontab."
				sudo pacman -S --noconfirm cronie
			else
				echo "No supported package manager found, exiting."
				exit
			fi
		fi
	else
		echo "cron not installed, aborting scron."
	fi

fi

