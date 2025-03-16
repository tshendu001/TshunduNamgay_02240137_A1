import math

def selection():
    while True:
        print("\nSelect a function please (one-6):")
        print("1. Calculate the sum of prime_numbers")
        print("2. Convert length_ units")
        print("3. Count consonants_ in a string")
        print("4. Find min and max numbers")
        print("5. Check for_ palindrome")
        print("6. Word_ Counter")
        print("0. program is been_ exit")
        
        try:
            putonee = int(input("Please can you give the choice: "))
        except ValueError:
            print("Oh!error input! put a number.")
            continue
        
        if putonee == 1:
            def prime_nums(num):
                if num < 2:
                    return False
                for aul in range(2, int(num**0.5) + 1):
                    if num % aul == 0:
                        return False
                return True             
            def sum_the_pri(first, last):
                return sum(number for number in range(first, last + 1) if prime_nums(number))
            first = int(input("enter the start of range: "))
            last = int(input("enter the end of range: "))
            print("Your_sum of prime_numbers in range:", sum_the_pri(first, last))
        
        elif putonee == 2:
            value = float(input("enter the value you desire to convert---: "))
            direc = input("Please Put the direction (M for the meters to feet / F for the feet to meters): ")
            if direc.upper() == "M":
                converted_num = round(value * 3.28084, 2)
            elif direc.upper() == "F":
                converted_num = round(value / 3.28084, 2)
            else:
                converted_num = "OH! Its Invalid direction"
            print(f"The_Converted_value: {converted_num}")
        
        elif putonee == 3:
            textt = input("Hy enter a text string: ")
            count_the_consonants = sum(1 for char in textt.lower() if char.isalpha() and char not in "aeiou")
            print("number of the consonants:", count_the_consonants)
        
        elif putonee == 4:
            try:
                countt = int(input("How many numbers do you  want to enter? "))
                if countt <= 0:
                    print("Please try to enter a number greater than 0.")
                    continue
                number = [float(input(f"Enter_the_number {i+1}: ")) for i in range(countt)]
                print(f"Minn: {min(number)}, Maxx: {max(number)}")
            except ValueError:
                print("invalid input! Enter_numbers_only.")
        
        elif putonee == 5:
            words = input("enter a text string!!!: ")
            cleaned_the_text = ''.join(char.lower() for char in words if char.isalnum())
            print("palindrome_check:", cleaned_the_text == cleaned_the_text[::-1])
        
        elif putonee == 6:
            files_paths = input("enter the file path please: ")
            words_to_count = ["the", "was", "and"]
            try:
                with open(files_paths, "r", encoding="utf-8") as file:
                    words = file.read().lower().split()
                    word_counts = {word: words.count(word) for word in words_to_count}
                    print("Word counts:", word_counts)
            except FileNotFoundError:
                print("error: file_ is_ been_ not_ found!")
        
        elif putonee == 0:
            print("exiting programm. Goodbye! hope to see you!")
            break
        
        else:
            print("Ohh!!invalid_option, Please Enter a Valid Number.")

selection()
