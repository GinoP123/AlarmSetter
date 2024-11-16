#!/bin/bash

if [[ $SHELL == *zsh ]]; then
	if [[ "$(cat ~/.zprofile | grep AlarmSetter)" == "" ]]; then
		echo "export PATH=\"\$PATH:$PWD/AlarmSetter/bin\"" >> ~/.zprofile
	fi
else
	if [[ "$(cat ~/.bashrc | grep AlarmSetter)" == "" ]]; then
		echo "export PATH=\"\$PATH:$PWD/AlarmSetter/bin\"" >> ~/.bashrc
	fi
fi
