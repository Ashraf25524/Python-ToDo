message = '''
START: To start the car
STOP: To stop the car
QUIT: To quit the game 
HELP: To display this help pannel
'''
started = False
while True:
    command = input('Enter your command > ')
    if command.upper() == "START":
        if started == False:
            started = True
            print("Your car is now starting") 
        else:
            print("You cannot start a car that is already moving")
    elif command.upper() == "STOP":
        if started == True:
            started = False
            print("Your car is stopping")
        else:
            print("You cannot stop a car that is not moving")
    elif command.upper() == "QUIT":
        quitting = input("Yes(Y) or No(N): ")
        if quitting.upper() == "Y":
            print("Your have quitted")
            break
        else:
            continue
    elif command.upper() == "HELP":
        print(message) 
    else:
        print("Invalid command")
