# ------------------------------------------------
#  Bunny Escape — A Text-Based Adventure Game
#  Author: Samy Sasikumar
# ------------------------------------------------


def ask_yes_no(prompt):
    """Ask a yes/no question and keep asking until a valid answer is given."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            return answer
        print("Please answer 'yes' or 'no'.")


def ask_place(prompt):
    """Ask the player to choose cave, hill, or burrow and keep asking until valid."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["cave", "hill", "burrow"]:
            return choice
        print("Please choose 'cave', 'hill', or 'burrow'.")


# ---------------- GAME LOOP ----------------
while True:
    print(
        "\nYou are a bunny who wriggles your fuzzy body through a hole in the cold metal gates.\n"
        "You run up a grassy hill and feel the bright lights fading away as you escape into a dark forest."
    )

    name = input("What is your tag number little bunny? ").strip()

    weight = float(input("Do you remember how much they weighed you? (use a decimal point) ").strip())

    fur_color = input("What is your fur color? ").strip().lower()

    print(f"\nHello there, {name}. You weigh {weight} pounds and you have {fur_color} fur.")

    # Weight affects the story — heavier bunnies move slower
    if weight > 10:
        print("You are a big bunny. You will need to be extra careful — you are harder to hide.")
    else:
        print("You are a small bunny. You are quick and easy to hide.")

    ready = ask_yes_no("\nAre you ready to go further into the vast unknown of this forest? (yes/no) ")

    if ready == "yes":
        print("Hurry! You hear humans yelling. You dive into a nearby bush at the forest entrance.")
        break
    else:
        print("\nYou freeze. The forest feels too vast. Let's start over...\n")


# ---------------- INVENTORY ----------------
inventory = ["half a carrot", "a number tag on string", "a rock"]

print("\nYou are carrying:", ", ".join(inventory))

print("\nYou begin to yawn...")
print("But then you remember that you are not the only one in this forest...")
print("You should find somewhere to spend the night.")


# ---------------- MOUSE INTERACTION ----------------
print("\nAs you hop through the grass, a tiny mouse appears on a rock.")

mouse_choice = ask_yes_no("The mouse looks hungry. Do you give the mouse your carrot? (yes/no) ")

if mouse_choice == "yes" and "half a carrot" in inventory:
    inventory.remove("half a carrot")
    print("\nThe mouse happily eats the carrot.")
    print('"Thank you!" the mouse squeaks.')
    print('"Be careful if you go to the hill... I saw humans there earlier."')
else:
    print("\nThe mouse looks disappointed and scurries away into the grass.")

print("\nAfter some cautious walking you see three places in the forest.")
print("A dark cave, a grassy hill, and a quiet burrow.")

place = ask_place("Where would you like to explore first? (cave/hill/burrow) ")


# ---------------- HILL ----------------
if place == "hill":
    print("\nYou hop quietly up the hill.")
    print("From the top you can see the glowing lights of the building far away.")

    print("Suddenly you hear footsteps behind you.")
    print("A lab worker shines a flashlight across the grass.")

    hide = ask_yes_no("Do you try to hide in the tall grass? (yes/no) ")

    if hide == "yes":
        print("\nYou press yourself flat against the ground.")
        print("But the light stops right on you.")
        print("The lab worker sighs with relief.")
        print('"There you are, little rascal."')
        print("You are picked up and carried back toward the bright building.")
        print("ENDING: You are brought back to the lab where you will be tested on for the rest of your life.....")
    else:
        print("\nYou try to run down the hill.")
        print("But the lab worker is faster.")
        print("A net drops over you.")
        print("ENDING: You are caught and brought back to the lab where you will be tested on for the rest of your life....")


# ---------------- BURROW ----------------
elif place == "burrow":
    print("\nYou crawl into the burrow expecting another rabbit.")
    print("Instead, several small eyes blink in the darkness.")
    print("A family of opossums stares back at you.")

    carrot = ask_yes_no("The baby opossums look hungry. Do you give them your carrot? (yes/no) ")

    if carrot == "yes" and "half a carrot" in inventory:
        inventory.remove("half a carrot")
        print("\nYou share your carrot with the opossum family.")
        print("They happily munch on it.")
        print("The mother opossum nods kindly.")
        print('"You may stay here tonight, little bunny."')
        print("You curl up safely in the warm burrow.")
        print("ENDING: You spend the night safely with the opossum family.")
    else:
        print("\nThe opossums still feel sorry for you.")
        print("They shuffle aside and make room.")
        print("You curl up beside them in the warm burrow.")
        print("ENDING: You safely spend the night with the opossum family.")


# ---------------- CAVE ----------------
elif place == "cave":
    print("\nYou slowly enter the cave.")
    print("The cave is dark and smells like damp stone.")
    print("A large shadow moves inside... it is a bear.")
    print('"Hmm... my eyesight is terrible," the bear mutters.')

    talk = ask_yes_no("Do you greet the bear politely? (yes/no) ")

    if talk == "yes":
        bear_question = ask_yes_no("The bear asks 'Is your fur brown?' (yes/no) ")
        if bear_question == "yes" and fur_color == "brown":
            print("\nThe bear nods.")
            print('"Good. Brown like another bear."')
            print('"You may sleep in my cave tonight."')
            print("You curl up against the warm cave wall.")
            print("The wind howls outside, but you are safe.")
            print("ENDING: You survive the night safely in the bear's cave.")
        else:
            print("\nThe bear squints.")
            print('"Hmm... You must not be a bear."')
            print('"You must sleep outside."')
            print("\nYou curl up in a bush outside the cave.")
            print("The forest grows quiet and cold.")
            print("But something is moving through the leaves...")
            print("A fox smells you in the darkness.")
            print("ENDING: You are eaten by a hungry fox.")
    else:
        print("\nThe bear hears you moving in the dark.")
        print('"Something is in my cave!" he growls.')
        print("You run outside and hide in a bush.")
        print("You turn around and meet face to face with a fox licking his lips.")
        print("ENDING: You are eaten by a hungry fox.")
