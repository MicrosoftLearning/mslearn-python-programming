 # Load the pyfiglet package
import pyfiglet

 # Ask the user for their name
name = input("What is your name? ")
name = name.strip()

 # Turn the name into a banner
banner = pyfiglet.figlet_format(name)

 # Print a greeting
print(banner)
print(f"Hello, {name.upper()}! Welcome to VS Code.")