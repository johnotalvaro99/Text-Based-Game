# John Otalvaro

# Story
def show_story():
    print("Space Station Invasion")
    print("--------------------------------------------------------------------------------")
    print("You are an astronaut sent on a mission to the Internation Space Station (ISS).")
    print("Once aboard, you realize the crew that was expecting you is nowhere to be found.")
    print("You find a video recording from a member of the crew that was uploaded 14 hours ago.")
    print("The video explains an alien life form has infiltrated the station,")
    print("and they had to escape before your arrival.")
    print("Your mission now is to escape, but the remaining escape pod is down and needs repair.")
    print("You must collect some items scattered around the ISS in order to repair the pod.")
    print("You need an oxygen mask from the supply room so you can breathe,")
    print("a wrench from the engineering room to repair the pod,")
    print("a fuse in the storage room to replace the missing one in the pod,")
    print("an MRE from the kitchenette to eat to recharge your energy,")
    print("an escape pod manual in the window room to know how to repair the pod,")
    print("and a med kit from the medical bay in case the alien hurts you.\n")


# Instructions
def show_mission():
    print("Your Mission:")
    print("Collect all items to repair escape pod 1 and escape the ISS.")
    print("Avoid the alien in Escape Pod 2!")
    print("Move commands: North, South, East, West")
    print("Type the item's name to pick it up.")
    print("Type 'exit' to quit the game.\n")


# Rooms and items dictionary
rooms = {
    'Command Center': {'East': 'Engineering Room', 'South': 'Supply Room'},
    'Engineering Room': {'West': 'Command Center', 'item': 'Wrench'},
    'Supply Room': {'North': 'Command Center', 'South': 'Medical Bay', 'East': 'Storage Room', 'West': 'Window Room',
                    'item': 'Oxygen Mask'},
    'Window Room': {'East': 'Supply Room', 'South': 'Escape Pod 1', 'item': 'Escape Pod Manual'},
    'Storage Room': {'West': 'Supply Room', 'South': 'Kitchenette', 'item': 'Fuse'},
    'Kitchenette': {'North': 'Storage Room', 'South': 'Escape Pod 2', 'item': 'MRE'},
    'Medical Bay': {'North': 'Supply Room', 'item': 'Med Kit'},
    'Escape Pod 1': {'North': 'Window Room'},  # Win room
    'Escape Pod 2': {'North': 'Kitchenette'}  # Alien room, automatically lose
}


# Player's starting room and inventory
current_room = 'Command Center'
inventory = []


# Function to show current status
def show_status():
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)
    if 'item' in rooms[current_room]:
        print("\nYou see a", rooms[current_room]['item'])
    print("---------------------------")


# Main game loop
def main():
    global current_room  # Declare current_room as global
    show_story() # Show the backstory of the game
    show_mission() # Show the player the mission

    # Loop until the player wins, loses, or exits
    while True:
        show_status()

        # Get player's input (direction or item)
        move = input("Enter your move: ").strip().lower() # Removes extra spaces and turns everything to lowercase in player inputs

        # Handle exit command
        if move == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        # Process direction commands
        elif move.capitalize() in rooms[current_room]: # Capitalizes first letter of player input to match directions in rooms dictionary
            current_room = rooms[current_room][move.capitalize()] # Retrieves room that corresponds to that direction from current_room

        # Process item collection by typing the item's name directly
        elif 'item' in rooms[current_room] and move == rooms[current_room]['item'].lower():
            item = rooms[current_room]['item']
            if item not in inventory:
                inventory.append(item)
                print(f"You picked up the {item}.")
                del rooms[current_room]['item']  # Remove item from room after getting it
            else:
                print("You already have that item.")

        else:
            print("\nInvalid move, try again!")

        # Check for win or loss
        if current_room == 'Escape Pod 1':
            if len(inventory) == 6:
                print("Congratulations! You collected all the items and escaped!")
            else:
                print("You made it to Escape Pod 1, but you didn't collect all the items and the alien got to you. Game Over!")
            break

        if current_room == 'Escape Pod 2':
            print("You encountered the alien! GAME OVER.")
            break


main()
