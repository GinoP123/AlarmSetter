#!/bin/zsh

cd $(dirname "$0")

if [[ "$1" == "check" ]]; then
	python3 alarm_check.py
elif [[ "$1" == "set" && "$2" != "" ]]; then
	python3 alarm_set.py "$2"
elif [[ "$1" == "unset" ]]; then
	python3 alarm_unset.py
else
	exit 1
fi

