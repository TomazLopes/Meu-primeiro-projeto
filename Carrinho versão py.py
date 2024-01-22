import time

print('Welcome to the car game!')

car_moving = False
command = ''
game_on = True
while command.lower() != 'quit':
    command = input('> ')
    if command.lower() == 'help':
        print('''
 start = start the car
 stop = stop the car 
 quit = to exit''')
    elif command.lower() == 'start' and car_moving == False:
        car_moving = True
        print('the car has started ')
    elif command.lower() == 'start' and car_moving == True:
        print('car already moving!' )
    elif command.lower() == 'stop' and car_moving == True:
        car_moving = False
        print('the car has stopped ')
    elif command.lower() == 'stop' and car_moving == False:
        print('the car is alread stopped! ')
    elif command.lower() == 'quit':
        game_on = False
        print('the game has ended! ')
        time.sleep(3)
        break
    else:
        print('''I don't understand that! Try asking for 'help'
              ''')
