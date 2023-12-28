from datetime import datetime, timedelta

timestamp_str = "2023-12-27T16:00:00+03:00"

# Convert the string to a datetime object
timestamp_dt = datetime.fromisoformat(timestamp_str)

# Convert the time zone offset to a timedelta
time_zone_offset = timedelta(hours=int(timestamp_str[-6:-3]))

# Adjust the datetime object by subtracting the time zone offset
normalized_dt = timestamp_dt - time_zone_offset

print(normalized_dt)
formatted_time = normalized_dt.strftime("%H:%M")
print(formatted_time)

