
import os
import time
import random
import json
import urllib.request
import urllib.error

def generate_random_name():
    url = "https://randomuser.me/api/?inc=name&nat=us"

    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            data = json.loads(response.read().decode("utf-8"))

        person = data["results"][0]["name"]
        return f"{person['first']} {person['last']}"

    except Exception:
        return "ANONYMOUS"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print("LARP MACHINE v0.1")
time.sleep(0.5)
print("=================")
time.sleep(3)
print("System initialized.")
time.sleep(1)
print("Loading fictional reality...")
time.sleep(2)
print("Reality initialized.")
time.sleep(2)
print("Connecting to the internet... (some options need a connection)")
time.sleep(2)
print("Internet connection status:"    )

try:
    with urllib.request.urlopen(
        "https://randomuser.me/api/",
        timeout=3
    ):
        print("CONNECTED")
except Exception:
    print("FAILED")

time.sleep(2)
print("Waiting for operator...")
time.sleep(5)

name = input("Operator name: ")
print("Welcome, " + name + ".")
time.sleep(2)
print("LARP MACHINE is ready.")
time.sleep(3)

clear_screen()

menu = """
================================
       LARP MACHINE v0.1
================================

What would you like to do?

1. Generate a fake scenario
2. Enter joke mode
3. Generate a fictional identity
4. Make something up
5. Exit

Choose an option: """


while True:
    print(menu, end="")
    choice = input().strip()

    if choice == "5":
        print("\nShutting down...")
        time.sleep(1)
        clear_screen()
        break

    elif choice == "1":
        clear_screen()

        print("""
================================
       SCENARIO GENERATOR
================================

Choose a category:

A. The Underground
B. Business
C. Minecraft Manhunt

X. Return to main menu
""")

        category = input(
            "Choose A, B, C, or X: "
        ).strip().upper()

        if category == "X":
            clear_screen()
            continue

        elif category in ("A", "B", "C"):
            clear_screen()

            if category == "A":
                print("THE UNDERGROUND")
                print("==============================")
                print("\nPOV: YOU ARE CHARA")
                time.sleep(2)

                print(
                    "\nYou fall into the underground, "
                    "a world of monsters."
                )
                time.sleep(2)

                print(
                    "\nYou meet Asriel, "
                    "the prince of the underground."
                )
                time.sleep(2)

                print("\nASRIEL BRINGS YOU TO THE CORE")
                time.sleep(2)

                print("\nYOU ARE IN THE CORE")
                time.sleep(2)

                print(
                    "\nYOU GO TO NEW HOME AND MEET "
                    "THE KING, ASGORE AND THE QUEEN, TORIEL"
                )
                time.sleep(2)

                print(f"\nWhat do you do, {name}?")

                print("""
1. Tell Toriel to cook "butterscotch" pie
2. Sleep
3. Play with Asriel
4. Eliminate Asriel
""")

                action = input(
                    f"Choose 1, 2, 3, or 4, {name}: "
                ).strip()

                if action == "1":
                    print(
                        '\nYou ask Toriel to cook '
                        '"butterscotch" pie.'
                    )
                    time.sleep(2)
                    print(
                        "Toriel: Of course, my child!"
                    )
                    time.sleep(2)
                    print(
                        "\nToriel cooks the pie and serves it to you."
                    )
                    time.sleep(2)
                    print(
                        "\nYou eat the pie and feel happy, only for now."
                    )
                    time.sleep(2)
                    print(
                        "\nToriel: I hope you enjoyed the pie, my child."
                    )
                    time.sleep(2)
                    print("\nIt was actually made of buttercup, which is poisonous to humans."
                                            " You die from the poison." )
                    print("\nBad ending. You have died." )

                elif action == "2":
                    print("\nYou decide to sleep.")
                    time.sleep(2)
                    print(
                        "You wake up feeling rested."
                    )
                    time.sleep(2)
                    print(
                        "\nToriel: Good morning, my child!"
                    )
                    time.sleep(2)
                    print("\nGood ending. You have survived the night.")

                elif action == "3":
                    print(
                        "\nYou decide to play with Asriel."
                    )
                    time.sleep(2)
                    print(
                        "Asriel is happy to play with you!"
                    )
                    time.sleep(2)
                    print("\nYou have a fun time playing with Asriel.")
                    time.sleep(2)
                    print("\nFriendship ending. You have made a friend. How wonderful!")

                elif action == "4":
                    print(
                        "\nAsriel looks at you, confused."
                    )
                    time.sleep(2)
                    print(
                        "Asriel: Chara...? What's wrong?"
                    )
                    time.sleep(2)
                    print("\nYou bring the knife from the kitchen and stab Asriel.")
                    time.sleep(2)  
                    print("\nAsriel: Why...? Why would you do this?")
                    time.sleep(2)
                    print("\nMurder ending. You have killed a friend, what have you done?")

                else:
                    print(f"\nInvalid action, {name}.")

            elif category == "B":
                print("BUSINESS")
                print("==============================")
                print("\nPOV: YOU ARE ELON DUSK")
                time.sleep(2)
                print(
                    "\nYou created the Cyber SUV."
                )
                time.sleep(2)
                print(
                    f"\nEveryone cheers at you."
                )
                time.sleep(2)
                print("\nBut there is only ONE hater.")
                time.sleep(2)
                print(f"\nWhat will you do next, {name}?")

                print("""
1. Ignore the hater
2. Confront the hater
3. Offer the hater a free Cyber SUV
4. Challenge the hater to a duel
5. Record the hater and hate him back in 4k
""")

                action = input(
                    f"Choose 1, 2, 3, 4, or 5, {name}: "
                ).strip()

                if action == "1":
                    print("\nYou decide to ignore the hater.")
                    time.sleep(2)
                    print(
                        "\nYou continue on with your life, ignoring the hater."
                    )
                    time.sleep(2)
                    print("\nThe hater goes nuts...")
                    time.sleep(2)
                    print("\nGood ending??? You have successfully ignored the hater.")

                elif action == "2":
                    print("\nYou decide to confront the hater.")
                    time.sleep(2)
                    print(
                        "\nYou confront the hater and ask why he is hating on you."
                    )
                    time.sleep(2)
                    print("\nThe hater says he is jealous of your success and your projects are trash.")
                    time.sleep(2)
                    print("\nYou tell him to chill out and help him.")
                    time.sleep(2)
                    print("\nGood ending??? You have successfully confronted the hater and made him feel better.")

                elif action == "3":
                    print("\nYou decide to offer the hater a free Cyber SUV.")
                    time.sleep(2)
                    print(
                        "\nThe hater is thinking...."
                    )
                    time.sleep(2)
                    print("\nThe hater accepts the offer and is now happy.")
                    time.sleep(2)
                    print("\nOffer ending. You have successfully offered the hater a free Cyber SUV.")
                elif action == "4":
                    print("\nYou decide to challenge the hater to a duel.")
                    time.sleep(2)
                    print("\nThe hater challenges you in a fortnite game")
                    time.sleep(2)
                    print("\nYou accept the challenge and play fortnite with the hater.")
                    time.sleep(2)
                    print("\nYou lose the game and the hater is now happy.")
                    time.sleep(2)
                    print("\nBad ending. You suck at fortnite and lost the duel with the hater.")
                elif action == "5":
                    print("\nYou decide to record the hater and hate him back in 4k.")
                    time.sleep(2)
                    print("\nThe hater is now mad at you and is now hating on you even more.")
                    time.sleep(2)
                    print("\nYou have successfully recorded the hater and hated him back in 4k.")
                    time.sleep(2)
                    print("\nWorst ending. You have made the hater even more mad at you.")
                else:
                    print(f"\nInvalid action, {name}.")

            elif category == "C":
                print("MINECRAFT MANHUNT")
                print("==============================")
                print(f"\nPOV: YOU ARE DREAM")
                time.sleep(2)
                print(
                   "\nYou are playing Minecraft Manhunt,"
                   "while running from the hunters."
                )
                time.sleep(2)
                print(
                   "\nYou somehow fall in the cave."
                )
                time.sleep(2)
                print(
                   f"\nWhat will you try to do, {name}?"
                )

                print("""
1. Try to escape the cave
2. Try to find diamonds
3. Make a spear and fight the hunters
4. Try to find a way to the surface
""")
                
                action = input(
                    f"Choose 1, 2, 3, or 4, {name}: "
                ).strip()

                if action == "1":
                    print("\nYou try to escape the cave.")
                    time.sleep(2)
                    print(
                        "\nBut the cave was too deep."
                    )
                    time.sleep(2)
                    print("\nTrapped ending. You have failed to escape the cave.")

                elif action == "2":
                    print("\nYou stripmine to find diamonds.")
                    time.sleep(7)
                    print(
                        "\n..."
                    )
                    time.sleep(2)
                    print("\nYou realized you only have a stone pickaxe and you can't mine diamonds.")
                    time.sleep(2)
                    print("\nBad ending. You have failed to find diamonds.")

                elif action == "3":
                    print("\nYou make a spear and fight the hunters.")
                    time.sleep(2)
                    print(
                        "\nYou fight the hunters with your spear and somehow escape."
                    )
                    time.sleep(2)
                    print("\nFight ending. You have successfully fought the hunters and escaped.")

                elif action == "4":
                    print("\nYou try to find a way to the surface.")
                    time.sleep(2)
                    print(
                        "\nYou find a way to the surface and run away from the hunters."
                    )
                    time.sleep(2)
                    print("\nGood ending. You have successfully found a way to the surface and escaped the hunters.")

                else:
                    print(f"\nInvalid action, {name}.")

            input(f"\nPress Enter to return, {name}.")

        else:
            print(f"\nInvalid category, {name}.")
            time.sleep(1)

        clear_screen()

    elif choice == "2":
        clear_screen()

        print(f"""
================================
          JOKE MODE
================================

Welcome to Joke Mode, {name}.

1. Generate a ridiculous joke
2. Generate a fake news headline
3. Generate a random goofy quote
X. Return to main menu
""")

        joke_choice = input("Choose an option: ").strip().upper()

        if joke_choice == "1":
            print("\nTeacher says the homework is a piece of cake.")
            print("The students eat it because they thought it was a real cake.")
            print("Guess it is 'easy as BUTTERCUP PIE' after all.")

        elif joke_choice == "2":
            print("\nBREAKING NEWS:")
            print("Local LARPER invents a Cyber SUV")
            print("that runs on pure BUTTERSCOTCH PIE.")
            print("He really BONED for it.")

        elif joke_choice == "3":
            print('\nDid you know shampoo is shampoo?')
            print("Because a guy named Sham poo'd on it. LOL")

        elif joke_choice == "X":
            clear_screen()
            continue

        else:
            print(f"\nInvalid option, {name}.")

        input(f"\nPress Enter to return, {name}.")
        clear_screen()

          
    elif choice == "3":
        clear_screen()

        print("==============================")
        print("     FICTIONAL IDENTITY")
        print("==============================")

        identity_name = generate_random_name()

        print(f"\nName: {identity_name}")
        print("Occupation: Professional Button Presser")
        print("Location: The Internet")

        input("\nPress Enter to return to the main menu...")
        clear_screen()

         
    elif choice == "4":
        clear_screen()

        print("==============================")
        print("     RANDOM TEXT GENERATOR")
        print("==============================")

        subjects = [
            "The purple toaster",
            "A mysterious potato",
            "The school principal",
            "Sans",
            "A Windows 7 computer"
        ]

        actions = [
            "has officially declared war on",
            "accidentally summoned",
            "is secretly controlling",
            "just discovered",
            "has challenged"
        ]

        objects = [
            "the school Wi-Fi",
            "the Moon",
            "a suspicious duck",
            "the Internet",
            "Papyrus"
        ]

        for i in range(5):
            sentence = (
                random.choice(subjects) + " "
                + random.choice(actions) + " "
                + random.choice(objects) + "."
            )
            print("\n" + sentence)

        input("\nPress Enter to return to the main menu...")
        clear_screen()


    else:
        print(
            f"\nThat option isn't implemented yet, {name}."
        )
        input(f"Press Enter to return to the menu, {name}...")
        clear_screen()
        clear_screen()
