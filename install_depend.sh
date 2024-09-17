#!/bin/bash

which $1 >> /dev/null 2>&1
doescron=$?

if (( $doescron != 0 )) 
then
	echo "$1 is not installed."
	read -p "Would you like to install? (Y/n): " install
   
	if [[ $install == 'Y' ]]
	then
		# check package managers (apt then pacman)
		echo "Checking available package managers..."
		
		which apt > /dev/null 2>&1
		doesapt=$?

		if (( $doesapt == 0 ))
		then
			echo "Found apt."
			echo "Installing $1. Don't forget to update your packages."
			sudo apt -y install $1

			
			if (( $? != 0 ))
			then
				echo "Something went wrong."
				exit 1
			else
				exit 100 # successful install
			fi

		else
			which pacman > /dev/null 2>&1
			doespac=$?
			
			if (( $doespac == 0 ))
			then
				echo "Found pacman."
				echo "Installing $1. Don't forget to update your packages."
				
				if [[ $1 == "crontab" ]]
				then
					sudo pacman -S --noconfirm cronie
				else
					sudo pacman -S --noconfirm $1
				fi
				
					
				if (( $? != 0 ))
				then
					echo "Something went wrong."
					exit 1
				else
					exit 100 # successful install
				fi
			else
				echo "No supported package manager found, exiting."
				exit 1
			fi
		fi
	else
		echo "$1 not installed, stopping scron."
		exit 1
	fi

fi

exit 0 
