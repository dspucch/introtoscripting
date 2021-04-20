#Dominic Spucches
# data setup
rooms = {'Company Area': {'name': 'Company Area', 'east': 'Common Room',
        'text': 'You are in the Company Area.'},
    'Common Room': {'name': 'Common Room', 'south': 'Supply Room', 'west': 'Company Area', 'north': 'Locker Room','east': 'HR Office', 'text': 'You are in the Supply Room.'},      
    'HR Office': {'name': 'HR Office', 'west': 'Common Room', 'north': '1SG Office', 'text': 'You have entered the HR Office.'},
    'Supply Room': {'name': 'the Supply Room', 'east': 'Arms Room', 'north': 'Common Room', 'text': 'You are in the Supply Room.'},  
    'Arms Room': {'name': 'Arms Room', 'west': 'Supply Room',
        'text': 'You are in the Arms Room.'},
    'Locker Room': {'name': 'Locker Room', 'south':'Common Room', 'text': 'You are in the Locker Room'},
    '1SG Office': {'name': '1SG Office', 'south': 'HR Office', 'text': 'You have entered the 1SG Office.'}
    }
directions = ['north', 'south', 'east', 'west']
current_room = rooms['Company Area']

print('You are now playing a game!')
print('We must force the Company First Sergeant into submission to release us early for the weekend!')
print('Gather all the items necessary to defeat him!')
print('Enter north, east, south, or west to move between rooms.')

while True:
    if current_room['name'] == '1SG Office':
        #will create if/else statement to require all items in inventory
        #before having ability to enter 1SG Office
        print('You knock, the crusty voice of an old 1SG tells you to enter. '
              'You walk in with confidence; stil facing his computer, he asks \n'
              '"What do you want SPC?" you respond.. "Top, if you dont release us early, \n'
              'there will be a mutiny!" The 1SG turns around in his chair; \n'
              'he is blinded by your reflective belt. Caught off guard he \n'
              'notices the bayonet, he swings cautiously, deflected by your \n'
              'Combat Helmet. The 1SG becomes enraged and conflict, you tell \n'
              'him he has one last chance. Threated, he asks "or what?" You \n'
              'slowly reach into your pocket... pulling out the mighty Sham Shield, \n'
              'throwing it like a ninja star. The Sham Shield hits the 1SG in the \n'
              'forehead, knocks him back into his chair. \n'
              'The 1SG conceeds and you are the victor.\n')
        break
    
    # display current location
    print('You are in {}.'.format(current_room['name']))
    
    # get user input
    command = input('\nWhat do you do?')
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print('You cannot go that way.')
    # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # bad command
    else:
        print('Invalid input')