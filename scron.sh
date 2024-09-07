#!/bin/bash

# TRY TO FIND A REPLACEMENT FOR REPTITIVE WHICH COMMANDS

which crontab >> ./scron.log 2>&1
doescron=$?

if (( $doescron != 0 )) 
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

		if (( $doesapt == 0 ))
		then
			echo "Found apt."
			echo "Installing crontab. Don't forget to update your packages."
			sudo apt -y install crontab
		else
			which pacman >> ./scron.log 2>&1
			doespac=$?
			
			if (( $doespac == 0 ))
			then
				echo "Found pacman."
				echo "Installing crontab. Don't forget to update your packages."
				sudo pacman -S --noconfirm cronie
			else
				echo "No supported package manager found, exiting."
				exit
			fi
		fi
	else
		echo "cron not installed, stopping scron."
		exit
	fi

fi

