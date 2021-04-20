def main():
    # data: rooms, items
    rooms = {
        'Common Room': {'name': 'Common Room', 'south': 'Supply Room', 'north': 'Locker Room', 'east': 'HR Office',
                        'item': 'coffee'},
        'HR Office': {'name': 'HR Office', 'west': 'Common Room', 'north': '1SG Office', 'item': 'sham shield'},
        'Supply Room': {'name': 'the Supply Room', 'east': 'Arms Room', 'north': 'Common Room', 'item': 'grid squares'},
        'Arms Room': {'name': 'Arms Room', 'west': 'Supply Room', 'item': 'bayonet'},
        'Locker Room': {'name': 'Locker Room', 'south': 'Common Room', 'item': 'reflective belt'},
        '1SG Office': {'name': '1SG Office', 'south': 'HR Office', 'item': '1SG'}
    }

    current_room = rooms['Common Room']
    command = input(print('Enter command')).lower()

    for key, value in rooms.items():
        if (command == value):
            print(value)
        else:
            print(key, ':', value)


main()
