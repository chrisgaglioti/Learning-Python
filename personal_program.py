__author__ = 'Chris Gaglioti'

# Game Introduction
print('')
print('\tWelcome to the Realm of Reason. This is a text-based game created to test the Python')
print('coding ability of Chris Gaglioti. Please follow the instructions given to the best of')
print('your ability. Note: any action choices presented to you will be in parentheses like')
print('so: knock(k) or ring(r). Please type the character for the option you choose.')
print('Otherwise, the game may not function correctly. Enough of this introduction.')
print("Let's begin.")
print('')
firstName = input('What is your first name: ')
gender = input('What is your gender(m) or (f): ')
gender = gender.lower()
while True:
    if gender == 'm' or gender == 'f':
        print('')
        print('Hello', firstName + '. Welcome to the game.')
        print('')
        break
    else:
        print('Please type the letter that corresponds to your gender.')
        gender = input('What is your gender(m) or (f): ')
        gender = gender.lower()

# Game Begins
print('You have been invited to a party at a mansion in the hollywood hills. As you walk up the driveway, you take a')
print('look at the clock; 9:07pm. The party was scheduled to begin at 9;00pm, and it appears many people have already')
print('arrived. You now stand at the front door. There is a doorbell to the right.')

# Door knock or ring - elif
while True:
    door01Command = input('Do you knock(k) on the door or ring(r) the doorbell? ')
    door01Command = door01Command.lower()
    if door01Command == 'k':
        print('')
        print('You knock on the large wooden door with a decent amount of force and wait patiently for')
        print('someone to answer. After a moment, a tall man in a tuxedo opens the door.')
        print('\t"I apologize for the delay. It\'s a little hard to hear the door over the crowd", he says.')
        break
    elif door01Command == 'r':
        print('')
        print('As you push the doorbell button, you are instantly shocked with electricity. The doorbell does not ring')
        print('and sparks are shooting out from behind the button. A tall man in a tuxedo opens the door.')
        print('\t"I apologize for the doorbell. Not everything around here is in working order", he says.')
        break
    else:
        print('')
        print('Please type the letter that corresponds to the action.')
        print('')
print('\t"Please come in. Can I take your coat ', end='')
if gender == 'm':
    print('Mr. ....?"')
else:
    print('Ms. ....?"')
lastName = input('[What is your last name]: ')
print('')
if gender == 'm':
    print('\t"Mr. ', firstName, ' ', lastName, '?', sep='', end='')
else:
    print('\t"Ms. ', firstName, ' ', lastName, '?', sep='', end='')
print(' We\'ve been expecting you. Right this way."')
print('You follow the man into a large foyer. He guides you to the left where another man waits behind a fully-')
print('stocked bar. "Feel free to grab a drink. It\'s going to be a long night", he says and walks away.')
