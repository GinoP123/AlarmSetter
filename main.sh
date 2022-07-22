#!/bin/zsh

dir="$(dirname "$0")"

if [[ "$1" == "check" ]]; then
	"$dir/alarm_check.py"
elif [[ "$1" == "set" && "$2" != "" ]]; then
	shift
	"$dir/alarm_set.py" $@
elif [[ "$1" == "unset" ]]; then
	"$dir/alarm_unset.py"
else
	echo -n "\n\tERROR: Invalid Arguments Given\n\n"
	exit 1
fi

