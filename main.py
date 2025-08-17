"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Klára Chvalinová
email: klarachvalinova@sezanm.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


users = {"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"}

username = input("Enter your user name: ")

if username not in users:
    print("Unregistered user, terminating the program..")
    exit()
    
while True:
    password = input("Enter your password: ")
    if users[username] == password:
        print("-" * 40)
        print(f"Welcome to the app, {username}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print("-" * 40)
        break
    else:
        print("Wrong password, try again.")

choice = input(f"Enter a number between 1 and {len(TEXTS)} to select: ")

if not choice.isdigit():
    print("Invalid input, terminating the program..")
    exit()

choice = int(choice)

if choice < 1 or choice > len(TEXTS):
    print("Invalid input, terminating the program.")
    exit()

print("-" * 40)

text = TEXTS[choice - 1]

words = text.split()
clean_words = []
word_lengths = {}

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
numbers_sum = 0

punctuation = ".,!?;:"

for word in words:
    clean_word = word.strip(punctuation)
    if clean_word == "":
        continue
    clean_words.append(clean_word)

    if clean_word.istitle():
        titlecase += 1
    elif clean_word.isupper() and clean_word.isalpha():
        uppercase += 1
    elif clean_word.islower():
        lowercase += 1
    elif clean_word.isdigit():
        numeric += 1
        numbers_sum += int(clean_word)

    length = len(clean_word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print(f"There are {len(clean_words)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")
print("-" * 40)

print("LEN|  OCCURRENCES  |NR.")
print("-" * 40)

max_count = 0
for length in word_lengths:
    if word_lengths[length] > max_count:
        max_count = word_lengths[length]

for length in sorted(word_lengths):
    stars = "*" * word_lengths[length]
    count = word_lengths[length]
    # zarovnání podle nejdelšího sloupce
    print(f"{length:>3}| {stars:<{max_count}}|{count}")