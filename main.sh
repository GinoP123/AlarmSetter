#!/bin/zsh

cd $(dirname "$0")

if [[ "$1" == "check" ]]; then
	./alarm_check.py
elif [[ "$1" == "set" && "$2" != "" ]]; then
	./alarm_set.py "$2"
elif [[ "$1" == "unset" ]]; then
	./alarm_unset.py
else
	echo -n "\n\tERROR: Invalid Arguments Given\n\n"
	exit 1
fi

