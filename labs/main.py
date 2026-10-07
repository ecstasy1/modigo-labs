def longest_streaks(daily_records):
  names = set()
  for day in daily_records:
    names.update(day.keys())

  current = {name:0 for name in names}
  longest = {name: 0 for name in names}

  for day in daily_records:
    for name in names:
        if day.get(name) == "present":
            current[name] +=1
            longest[name] = max(longest[name], current [name])
        else:
            current[name] = 0
  return longest