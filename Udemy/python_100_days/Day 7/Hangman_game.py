import random



words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli", "violet",
    "watermelon", "xylophone", "yellow", "zebra", "apricot", "blueberry", "cantaloupe", "dragonfruit", "eggplant", "fig",
    "grapefruit", "honeycrisp", "jackfruit", "kumquat", "lime", "mango", "nectar", "olive", "plum", "quinoa",
    "rhubarb", "starfruit", "tomato", "ugli", "vanilla", "walnut", "xenon", "yogurt", "zucchini", "antelope",
    "bamboo", "cactus", "dolphin", "eagle", "falcon", "giraffe", "hippopotamus", "iguana", "jaguar", "koala",
    "lemur", "monkey", "nightingale", "octopus", "penguin", "quail", "rabbit", "snake", "tiger", "umbrella",
    "vulture", "whale", "xylophone", "yak", "zebra", "airplane", "bicycle", "computer", "dragon", "engine",
    "furniture", "guitar", "house", "island", "jacket", "keyboard", "lamp", "mountain", "notebook", "ocean",
    "pencil", "quilt", "robot", "sunflower", "train", "unicorn", "violin", "window", "xylophone", "yacht"
]

random_word = random.choice(words)
print(random_word)



word_length = len(random_word)

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)


lives = 6 

correct_letter = []


while lives >= 0:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)

        elif letter in correct_letter:
            display += letter
         
        else:
            display += "_"
            lives = lives-1
    print(display) 

    if "_" not in display:
       print("You win")
   












