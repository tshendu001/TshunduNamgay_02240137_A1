import math

def selection():
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in a string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")
        
        try:
            choice = int(input("Please can you enter your choice: "))
        except ValueError:
            print("Oh!Invalid input! Enter a number.")
            continue
        
        if choice == 1:
            def prime_number(number):
                if number < 2:
                    return False
                for i in range(2, int(number**0.5) + 1):
                    if number % i == 0:
                        return False
                return True             
            def sum_of_prime(start, end):
                return sum(number for number in range(start, end + 1) if prime_number(number))
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            print("Your sum of prime numbers in range:", sum_of_prime(start, end))
        
        elif choice == 2:
            value = float(input("Enter the value you want to convert: "))
            direction = input("Enter direction (M for meters to feet / F for feet to meters): ")
            if direction.upper() == "M":
                converted_value = round(value * 3.28084, 2)
            elif direction.upper() == "F":
                converted_value = round(value / 3.28084, 2)
            else:
                converted_value = "Invalid direction"
            print(f"Converted value: {converted_value}")
        
        elif choice == 3:
            text = input("Enter a text string: ")
            count_consonants = sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")
            print("Number of consonants:", count_consonants)
        
        elif choice == 4:
            try:
                count = int(input("How many numbers will you enter? "))
                if count <= 0:
                    print("Enter a number greater than 0.")
                    continue
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(count)]
                print(f"Min: {min(numbers)}, Max: {max(numbers)}")
            except ValueError:
                print("Invalid input! Enter numbers only.")
        
        elif choice == 5:
            text = input("Enter a text string: ")
            cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
            print("Palindrome check:", cleaned_text == cleaned_text[::-1])
        
        elif choice == 6:
            file_path = input("Enter the file path: ")
            words_to_count = ["the", "was", "and"]
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read().lower().split()
                    word_counts = {word: text.count(word) for word in words_to_count}
                    print("Word counts:", word_counts)
            except FileNotFoundError:
                print("Error: File not found!")
        
        elif choice == 0:
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Ohh!!Invalid option, please enter a valid number.")

selection()
