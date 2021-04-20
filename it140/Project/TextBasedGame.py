# Dominic Spucches

def instructions():
    # print instructions for main menu
    print('\nHello there and welcome to my text based game!')
    print('In this game there are 5 items you must acquire to win.')
    print('You must move from room to room to collect them.')
    print('Move commands are: north, south, east, west.')
    print('Type the item name to place in inventory.')
    print('At anytime if you want to quit type "quit".')


#def showStatus(current_room, **inventory):


#current_room = rooms['Common Room']
#inventory = []
#rooms = []

#showStatus(inventory)


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

    directions = ['north', 'south', 'east', 'west']
    current_room = rooms['Common Room']
    inventory = []

    while True:
        # show user status
        print('\nYou are in {}.'.format(current_room['name']))
        print('You see a {}. Do you want it?.'.format(current_room['item'], ))
        print(f'Your inventory is {inventory}')
        print('---------------------------------------------')

        # get user input
        command = input('Enter your move:\n').lower()

        # movement
        if command in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
            elif (command not in directions) or (command not in current_room['item']):
                print('Invalid command.')
        # get items from rooms
        if command in current_room['item']:
            inventory.append(f"{command}")
            if len(inventory) == 5:
                print('----------------------------------------------------------')
                print('You have collected all the items needed to defeat the 1SG!')
                print('         ***** TELEPORTS TO 1SG OFFICE *****')
                print('             You have defeated the 1SG!')
                print('                 ***** END GAME *****')
                print('----------------------------------------------------------')
                exit()
        elif current_room['name'] == '1SG Office':
            print('You have encountered the 1SG without your items, you have lost.')
            exit()
        # quit game
        elif command == 'quit':
            print('Thanks for playing!')
            exit()
        # bad command
        return inventory


instructions()
main()
