# Create a loop that displays a menu and responds to user input
while True:
    # Display the menu
    print("\n=== Personal To-Do List ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Exit")
    
    # Get the user's choice
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print("\n--- Current Tasks ---")

        # Open the file in Read mode and read the tasks into a list

            
        # Display the tasks

            
    elif choice == "2":
        new_task = input("\nWhat do you need to do? ")

        # Open the file in Append mode to add to the end of the list

            
        print("Task saved!")
        
    elif choice == "3":
        # Exit the program
        print("\nGoodbye! Stay productive.")
        break 
        
    else:
        # Handle invalid input
        print("\nInvalid choice. Please choose 1, 2, or 3.")