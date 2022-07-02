#!/usr/bin/env python3

import settings
import library as lb

next_alarm = lb.get_next_alarm()
if not next_alarm:
	print("\n\tERROR: No Alarm Set\n")
	exit(1)

hours_rem, minutes_rem = time_remaining(*next_alarm)
plural = lambda x: 's' if x != 1 else ''
hours_remaining = f"{hours_rem} hour{plural(hours_rem)}"
minutes_remaining = f"{minutes_rem} minute{plural(minutes_rem)}"

if hours:
	remaining = f"\n\t{minutes_remaining}, {hours_remaining} remaining\n"
else:
	remaining = f"\n\t{minutes_remaining} remaining\n"

print(remaining)

