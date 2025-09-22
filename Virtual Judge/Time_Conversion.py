time_12hr = input().strip()  # Example input: 07:05:45PM

# Extract hour, minute, second, and period (AM/PM)
hour = int(time_12hr[:2])
minute = time_12hr[3:5]
second = time_12hr[6:8]
period = time_12hr[8:]

if period == "AM":
    if hour == 12:
        hour = 0
elif period == "PM":
    if hour != 12:
        hour += 12

print(f"{hour:02}:{minute}:{second}")