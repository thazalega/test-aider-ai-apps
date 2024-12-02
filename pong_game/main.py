import pygame
import sys
from main.menu import main_menu
from main.game import main_game

def main():
    try:
        choice = main_menu()
        if choice == "start":
            main_game()
        elif choice == "exit":
            print("Exiting...")
            pygame.quit()
            sys.exit(0)
    except pygame.error as e:
        print(f"Pygame error: {e}")

if __name__ == "__main__":
    # Add the directory containing menu.py to the Python path
    sys.path.append('main')
    main()
