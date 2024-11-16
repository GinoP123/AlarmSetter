#!/bin/bash

touch text_files/next_alarm.txt
touch text_files/alarms.csv
touch text_files/alarm_reminder.py

if [[ $SHELL == *zsh ]]; then
	if [[ "$(cat ~/.zprofile | grep AlarmSetter)" == "" ]]; then
		echo "export PATH=\"\$PATH:$PWD/bin\"" >> ~/.zprofile
	fi
else
	if [[ "$(cat ~/.bashrc | grep AlarmSetter)" == "" ]]; then
		echo "export PATH=\"\$PATH:$PWD/bin\"" >> ~/.bashrc
	fi
fi
