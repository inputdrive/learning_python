inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20}

inventory["invisible knife"] = 40
inventory["mithril shield"] = 25
print(inventory,'\n')

conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key:value for key, value in zip(conference_rooms, capacity)}

print(room_dict)