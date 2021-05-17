# random = input('')
# if random == 'start':
#     print('Car started...Ready to go!')
# elseif random == 'stop':
#     print('Car stopped ')
# else random == 'quit':
#     break:
# expert I forgot to edit this so please come back to edit it for correction
command = ""
started = False
while True:
    command = input("> ").lower()
    previous_command = command.lower()
    if command == "start":
        print("Car started...")
        while True:
            if command == "start":
                print("Car is already started") 
    elif command == "stop":
        print("Car stopped.")
    elif previous_command == "stop":
        print("Car already stopped")
    elif command == "help":
        print("""
Start - to start the car 
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry , I don't understand that!")
