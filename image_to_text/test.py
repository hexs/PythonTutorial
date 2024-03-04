import keyboard

while True:

        event = keyboard.read_event()
        stamp_time = event.time
        event_type = event.event_type
        name = event.name
        if event_type == 'up' and name == 'right ctrl':
            print(555)


