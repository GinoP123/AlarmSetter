from datetime import datetime, timedelta
import settings


def to_datetime(hour, minute):
	return datetime.strptime(f"{hour}, {minute}", "%H, %M")


def time_after_delta(minutes):
	time = datetime.now() + timedelta(minutes=minutes)
	return time.hour, time.minute


def time_remaining(time):
	hour, minute, _ = time
	dt = to_datetime(hour, minute)
	now = to_datetime(*datetime.now().strftime("%H, %M").split(', '))

	day = timedelta(days=1)
	diff = dt - now

	if diff.days < 0:
		diff += day
	assert diff.days >= 0

	return diff.seconds // 3600, (diff.seconds // 60) % 60


def get_alarms():
	alarms = []
	with open(settings.alarms_file) as infile:
		for line in infile:
			hour, minute, message = line.strip().split(',')
			hour, minute = map(eval, [hour, minute])
			alarms.append((hour, minute, message))
	return alarms


def get_next_alarm():
	with open(settings.next_alarm_file) as infile:
		next_alarm = infile.read()
		if not next_alarm:
			return
		hour, minute, message = next_alarm.split(',')
		hour, minute = map(eval, (hour, minute))
		return hour, minute, message


def write_next_alarm(data):
	with open(settings.next_alarm_file, 'w') as outfile:
		if data:
			hour, minute, message = data
			outfile.write(f"{hour},{minute},{message}")


def min_alarm(*alarms):
	if alarms:
		return min(alarms, key=time_remaining)
	return None


def alarms_line(hour, minute, message):
	return f"{hour},{minute},{message}\n"


def crontab_line(hour, minute):
	return f"{minute} {hour} * * * {settings.alarm_unset_script}\n"


def write_reminder(m):
	if not m:
		m = "Alarm Finished!"
	time = datetime.now().strftime("%I,%M,%p").split(',')
	time = f"{int(time[0])}:{time[1]} {time[2]}"

	message = '_=' 
	message += '"' * 3
	message += f"\n\n\tIts {time}!!!\n\n\n\n"
	message += f"\t\t{m}\n\n\n\n"
	message += '"' * 3

	with open(settings.alarm_reminder_file, 'w') as outfile:
		outfile.write(message)

