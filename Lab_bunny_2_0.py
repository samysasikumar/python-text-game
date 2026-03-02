# ============================================================
# LAB BUNNY 2.0
# A text-based adventure game
# Written by: Samy Sasikumar
# ============================================================
# HOW TO PLAY:
#   Run this file with Python 3: python Lab_bunny_2_0.py
#   Read each scene carefully and type your choice when prompted.
#   Your decisions affect what happens next!
# ============================================================

import time  # used for dramatic pauses between scenes

# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

def pause():
    """Short pause for dramatic effect."""
    time.sleep(1.2)

def slow_print(text):
    """Print text then pause — makes the story feel cinematic."""
    print(text)
    pause()

def ask(prompt, options):
    """
    Ask the player to choose from a list of options.
    Keeps asking until a valid choice is made.
    Returns the player's choice as a string.
    """
    while True:
        answer = input(f"{prompt} ({'/'.join(options)}) ").strip().lower()
        if answer in options:
            return answer
        print(f"  Please type one of: {', '.join(options)}")

def show_inventory(inventory):
    """Display the player's current inventory."""
    print("\n  🎒 You are carrying:", ", ".join(inventory))

# ------------------------------------------------------------
# INTRODUCTION
# ------------------------------------------------------------

def intro():
    print("\n" + "=" * 55)
    print("           L A B   B U N N Y   2 . 0")
    print("=" * 55)
    pause()

    slow_print(
        "\nYou are a bunny who wriggles your fuzzy body through\n"
        "a hole in the cold metal gates of the laboratory.\n"
    )
    slow_print(
        "You scramble up a grassy hill. The bright fluorescent\n"
        "lights fade behind you as you escape into a dark forest.\n"
        "The air smells like pine and freedom.\n"
    )

    # --- Player setup ---
    name = input("What is your tag number, little bunny? ").strip()
    weight = input("Do you remember how much they weighed you? (use a decimal) ").strip()
    fur_color = input("What is your fur color? ").strip()

    print(f"\nHello, {name}. You weigh {weight} lbs and have {fur_color} fur.")
    slow_print("You are small, quick, and very, very scared.\n")

    # Starting inventory
    inventory = ["half a carrot", "a number tag on a string", "a smooth rock"]
    show_inventory(inventory)
    print()

    # Ask if ready
    ready = ask("\nAre you ready to go deeper into the vast unknown?", ["yes", "no"])

    if ready == "no":
        slow_print(
            "\nYou freeze at the forest entrance. The trees loom tall.\n"
            "A twig snaps behind you. Human footsteps.\n"
            "You squeeze your eyes shut... and bolt forward anyway.\n"
            "Fear can wait. Survival cannot.\n"
        )
    else:
        slow_print(
            "\nHurry! You hear humans yelling from back at the lab.\n"
            "You dive into a bush at the forest entrance and catch your breath.\n"
        )

    return name, inventory

# ------------------------------------------------------------
# CHAPTER 1 — THE FORK IN THE PATH
# ------------------------------------------------------------

def chapter_one(name, inventory):
    print("\n--- Chapter 1: The Fork in the Path ---\n")
    pause()

    slow_print(
        "You push through the underbrush and reach a fork in the path.\n"
        "To the LEFT: you hear the soft trickle of water — a stream.\n"
        "To the RIGHT: you see a faint warm glow between the trees.\n"
    )

    direction = ask(f"Which way do you go, {name}?", ["left", "right"])

    if direction == "left":
        return chapter_two_stream(name, inventory)
    else:
        return chapter_two_glow(name, inventory)

# ------------------------------------------------------------
# CHAPTER 2A — THE STREAM
# ------------------------------------------------------------

def chapter_two_stream(name, inventory):
    print("\n--- Chapter 2: The Stream ---\n")
    pause()

    slow_print(
        "You follow the sound of water and find a clear bubbling stream.\n"
        "You drink deeply. Refreshing.\n"
        "But then you notice a fox drinking on the opposite bank.\n"
        "It hasn't seen you yet.\n"
    )

    choice = ask("Do you hide or try to sneak past?", ["hide", "sneak"])

    if choice == "hide":
        slow_print(
            "\nYou tuck yourself under a mossy log and stay perfectly still.\n"
            "The fox finishes drinking and trots away into the trees.\n"
            "You breathe again. You notice a bundle of berries near the log.\n"
        )
        inventory.append("a bundle of wild berries")
        slow_print("You add the berries to your pack. They might be useful.")
        show_inventory(inventory)
        return chapter_three(name, inventory, survived_fox=True)

    else:  # sneak
        slow_print(
            "\nYou tiptoe along the bank... but a stone shifts under your paw.\n"
            "SPLASH. The fox's ears prick up. It locks eyes with you.\n"
            "You RUN. Branches whip your face. You zigzag through the trees.\n"
        )
        escaped = ask("Do you dash for a hollow log or leap into the stream?", ["log", "stream"])

        if escaped == "log":
            slow_print(
                "\nYou dive into a hollow log and go completely still.\n"
                "The fox circles once, twice... then gives up and leaves.\n"
                "You made it. A little shaken, but alive.\n"
            )
            return chapter_three(name, inventory, survived_fox=True)
        else:
            slow_print(
                "\nYou leap into the stream! The cold shocks your whole body.\n"
                "But the current carries you safely downstream, away from the fox.\n"
                "You drag yourself onto the bank, soaked but free.\n"
                "The rock from your pack falls out and sinks. It's gone.\n"
            )
            if "a smooth rock" in inventory:
                inventory.remove("a smooth rock")
            show_inventory(inventory)
            return chapter_three(name, inventory, survived_fox=True)

# ------------------------------------------------------------
# CHAPTER 2B — THE WARM GLOW
# ------------------------------------------------------------

def chapter_two_glow(name, inventory):
    print("\n--- Chapter 2: The Warm Glow ---\n")
    pause()

    slow_print(
        "You pad quietly toward the glow and discover a small campfire.\n"
        "A hiker sleeps beside it, snoring softly.\n"
        "Next to their backpack: a half-eaten sandwich and a cozy wool scarf.\n"
    )

    choice = ask("Do you take the sandwich, the scarf, or nothing and leave?", ["sandwich", "scarf", "nothing"])

    if choice == "sandwich":
        inventory.append("a ham sandwich (half eaten)")
        slow_print("\nYou snag the sandwich and bolt back into the trees. Delicious.")
        show_inventory(inventory)

    elif choice == "scarf":
        inventory.append("a warm wool scarf")
        slow_print(
            "\nYou drape the scarf around yourself. It's enormous on your tiny body,\n"
            "but wonderfully warm. You waddle back into the forest, cozy and content.\n"
        )
        show_inventory(inventory)

    else:
        slow_print(
            "\nYou decide not to risk it. You watch the dying fire for a moment,\n"
            "then slip silently back into the darkness. Wise.\n"
        )

    return chapter_three(name, inventory, survived_fox=True)

# ------------------------------------------------------------
# CHAPTER 3 — THE CLEARING
# ------------------------------------------------------------

def chapter_three(name, inventory, survived_fox):
    print("\n--- Chapter 3: The Clearing ---\n")
    pause()

    slow_print(
        "After what feels like hours, the trees thin out.\n"
        "You stumble into a wide moonlit clearing.\n"
        "In the center: an old rabbit warren — dozens of burrow entrances.\n"
        "A large rabbit with one torn ear emerges and studies you.\n"
        "\n'You've got lab tags,' she says. 'We don't take in lab animals.'\n"
        "'Too much heat from the humans.'\n"
    )
    pause()

    slow_print("She eyes your inventory.\n")
    show_inventory(inventory)

    # Check if player has something useful to trade or offer
    has_food = any(item in inventory for item in ["half a carrot", "a bundle of wild berries", "a ham sandwich (half eaten)"])

    if has_food:
        slow_print(
            "\nHer nose twitches toward your food.\n"
            "'...You have something to share?' she asks, her tone softening.\n"
        )
        share = ask("Do you offer her some of your food?", ["yes", "no"])

        if share == "yes":
            slow_print(
                "\nYou hold out the food with both paws.\n"
                "She takes a small piece. Chews. Nods slowly.\n"
                "\n'One night,' she says. 'Then you move on.'\n"
                "\nIt's not forever. But tonight, you are safe.\n"
            )
            return ending_good(name, inventory)

        else:
            slow_print(
                "\n'No?' She tilts her head. 'Then we have nothing to discuss.'\n"
                "She turns and disappears into the warren.\n"
                "You are alone in the clearing. You'll have to keep moving.\n"
            )
            return ending_neutral(name, inventory)

    else:
        slow_print(
            "\nYou have nothing to offer. She shakes her head slowly.\n"
            "'Move along, lab bunny.' She disappears underground.\n"
            "\nThe clearing is silent. You are alone. But you are free.\n"
            "And the forest is very, very large.\n"
        )
        return ending_neutral(name, inventory)

# ------------------------------------------------------------
# ENDINGS
# ------------------------------------------------------------

def ending_good(name, inventory):
    print("\n" + "=" * 55)
    print("           🌙  E N D I N G   —   S A F E  🌙")
    print("=" * 55)
    slow_print(
        f"\nYou curl up in a borrowed burrow, {name}.\n"
        "The sounds of the lab — the beeping machines, the cold metal —\n"
        "feel very far away now.\n"
        "\nYou don't know what comes next. But tonight you are warm,\n"
        "fed, and surrounded by others who understand what it means\n"
        "to just want to be free.\n"
        "\n✦ You escaped. You survived. You shared. ✦\n"
    )
    print("=" * 55)
    print("            T H A N K S   F O R   P L A Y I N G")
    print("=" * 55 + "\n")

def ending_neutral(name, inventory):
    print("\n" + "=" * 55)
    print("        🌲  E N D I N G   —   O N W A R D  🌲")
    print("=" * 55)
    slow_print(
        f"\nYou take a long breath, {name}.\n"
        "No shelter tonight. But the stars are out,\n"
        "and the forest is yours to explore.\n"
        "\nMaybe tomorrow you'll find somewhere that feels like home.\n"
        "For now, you keep hopping — one paw at a time.\n"
        "\n✦ The adventure continues... ✦\n"
    )
    print("=" * 55)
    print("            T H A N K S   F O R   P L A Y I N G")
    print("=" * 55 + "\n")

# ------------------------------------------------------------
# MAIN — run the game
# ------------------------------------------------------------

def main():
    name, inventory = intro()
    chapter_one(name, inventory)

if __name__ == "__main__":
    main()
