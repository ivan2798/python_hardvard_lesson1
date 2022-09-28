#Ask user for their name
#Remove whitespace from str and capitalize user's name and 
name = input("Whast's your name?").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello, {first} ")

