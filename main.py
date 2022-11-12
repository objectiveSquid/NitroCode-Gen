from random import choice
from os import name, system
from inquirer import List, prompt
from threading import Thread
from time import sleep

# Defining clear screen function
def clearscreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# Defining creating codes loading screen function
def creating_codes_loading():
    global creating_point
    global creating_done
    global code_amount
    while creating_done == False:
        clearscreen()
        print(f"Your codes are being generated, please wait...\nStatus: {creating_point}/{code_amount}")
    writing_codes_loading()

# Defining writing codes loading screen function
def writing_codes_loading():
    global writing_done
    global code_amount
    global writing_point
    while writing_done == False:
        clearscreen()
        print(f"Your codes are being written to file, please wait...\nStatus: {writing_point}/{code_amount}")

clearscreen()

# Asking for code amount
while True:
    try:
        code_amount = int(input("How many codes should be generated?\n"))
    except ValueError:
        print("\nERROR: Invalid code amount, please enter only whole numbers.\n")
    else:
        break

clearscreen()

# Asking for format
format = prompt([List("format", message = "Format", choices = ["https://discord.gift/{nitro_code}", "{nitro_code}"])])["format"]

clearscreen()

# Asking for length
lenght = prompt([List("length/type", message = "Nitro type", choices = ["Nitro classic/basic = 16 characters", "Nitro boost = 24 characters"])])["length/type"]

# Generating codes
creating_point = 0
creating_done = False
writing_point = 0
writing_done = False
codes = []
Thread(target = creating_codes_loading).start()
if lenght == "Nitro classic/basic = 16 characters" and format == "{nitro_code}":
    for _ in range(code_amount):
        codes.append(f"{''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')for i in range(16))}\n")
        creating_point += 1
elif lenght == "Nitro boost = 24 characters" and format == "{nitro_code}":
    for _ in range(code_amount):
        codes.append(f"{''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')for i in range(24))}\n")
        creating_point += 1
elif lenght == "Nitro classic/basic = 16 characters" and format == "https://discord.gift/{nitro_code}":
    for _ in range(code_amount):
        codes.append(f"https://discord.gift/{''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')for i in range(24))}\n")
        creating_point += 1
elif lenght == "Nitro boost = 24 characters" and format == "https://discord.gift/{nitro_code}":
    for _ in range(code_amount):
        codes.append(f"https://discord.gift/{''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')for i in range(24))}\n")
        creating_point += 1
else:
    creating_done, writing_done = True, True
    clearscreen()
    input("Something went wrong!\nPress enter to close the program...\n")
    exit()
creating_done = True
with open("codes.txt", "a") as codes_opened:
    for code in codes:
        codes_opened.write(f"{code}")
        writing_point += 1
writing_done = True
