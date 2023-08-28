import matplotlib.pyplot as plt
import time
import sys
from colorama import init, Fore, Style
import pyfiglet

def loading_screen():
    init(autoreset=True)
    animation_delay = 0.1
    spinner_frames = ['-', '\\', '|', '/']

    custom_fig = pyfiglet.Figlet(font='block')
    loading_text = custom_fig.renderText('Loading')

    print(Fore.CYAN + loading_text + Style.RESET_ALL)
    print(Fore.GREEN + "Please wait..." + Style.RESET_ALL)
    
    for _ in range(20):  # You can adjust the number of frames
        for frame in spinner_frames:
            sys.stdout.write(Fore.GREEN + frame + " Loading" + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(animation_delay)
            sys.stdout.write('\b' * (len(frame) + 8))  # Clear the line
            sys.stdout.flush()

    print("\nLoading complete!")
    print(Fore.YELLOW + "Project Made by " + Fore.MAGENTA + "Shubham" + Fore.RED + " TEAM - CODE RED" + Style.RESET_ALL)

if __name__ == "__main__":
    loading_screen()
    # Add your main program logic here

def is_perfect_square(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def generate_fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def display_fibonacci_sequence(sequence):
    plt.plot(sequence, marker='o')
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

def main():
    while True:
        print("1. Check if a number is a Fibonacci number")
        print("2. Generate Fibonacci sequence")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            number = int(input("Enter a number: "))
            if is_fibonacci_number(number):
                print(f"{number} is a Fibonacci number.")
                print("Explanation: It satisfies the mathematical property of Fibonacci numbers.")
            else:
                print(f"{number} is not a Fibonacci number.")
                print("Explanation: It does not satisfy the mathematical property of Fibonacci numbers.")
            satisfaction = input("Are you satisfied with the result? (yes/no): ")
            if satisfaction.lower() == "no":
                print("We're sorry to hear that. Please try again.")
            else:
                print("Thank you for using the program!")
                break
        elif choice == 2:
            limit = int(input("Enter the limit for Fibonacci sequence: "))
            fibonacci_sequence = generate_fibonacci_sequence(limit)
            print("Fibonacci sequence:", fibonacci_sequence)
            display_fibonacci_sequence(fibonacci_sequence)
            satisfaction = input("Are you satisfied with the result? (yes/no): ")
            if satisfaction.lower() == "no":
                print("We're sorry to hear that. Please try again.")
            else:
                print("Thank you for using the program!")
                break
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

# THANKS ME FOR PROVIDING THIS PROJECT FILE