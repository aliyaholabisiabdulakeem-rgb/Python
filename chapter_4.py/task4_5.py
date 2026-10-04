def seconds_since_midnight(hour, minutes, seconds):
    hour_in_seconds = hour * 3600
    minutes_in_seconds = minutes * 60
    return hour_in_seconds + minutes_in_seconds + minutes

print(seconds_since_midnight(13, 30, 45))
