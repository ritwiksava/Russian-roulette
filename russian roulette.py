import random 
import os 
def clear_screen():
    if os.name =='nt':
        os.system('cls') #os name is 'nt'  fo windows and 'posix' for linux and macos
    else :
        os.system('clear') #for linux and mac 
        #os.system(command) is used to execute a command in the terminal 
        #cls is the command to clear the screen in windows and clear is the command for linux and mac(in terminal)
def play_game():
    print("Welcome to Russian Roulette!")
    input("Press Enter to spin the chamber...")
    clear_screen()
    
    gun = [0, 0, 0, 0, 0, 1]  # 1 is the bullet
    random.shuffle(gun)
    input("Press Enter to pull the trigger ")
    clear_screen()
    
    if gun[0] == 1:
        print("BOOM! You lose....")
    else:
        print("Click! You SURVIVED.")

if __name__ == "__main__":
    play_game()

