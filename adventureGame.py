#Christopher Savage
def adventure_game():
    print("You are walking through a dark forest and find three items: a MATCH, a FLASHLIGHT, and a MAP.")
    choice = input("Which one do you want to pick up? ").strip().lower()

    if choice == "match":
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated.")
        next_choice = input("You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ").strip().lower()
        if next_choice == "run":
            print("You run as fast as you can, but the bear catches up to you. Unfortunately, you didn't make it. You lose.")
        elif next_choice == "hide":
            print("You hide behind a tree and the bear eventually goes away. You are safe for now.")
            next_choice_2 = input("You find a hidden path. Do you want to FOLLOW the path or RETURN to where you started? ").strip().lower()
            if next_choice_2 == "follow":
                print("You follow the path and discover a hidden village with friendly inhabitants.")
                village_choice = input("The villagers offer you shelter. Do you ACCEPT their offer or CONTINUE your journey alone? ").strip().lower()
                if village_choice == "accept":
                    print("You stay with the villagers and find a new home, living peacefully. You win!")
                elif village_choice == "continue":
                    print("You continue your journey and eventually night falls. You are all alone. Bats swarm around. A bear attacks you. You lose.")
                else:
                    print("Invalid choice. You wander aimlessly in the forest and eventually get lost. You lose.")
            elif next_choice_2 == "return":
                print("You return to where you started and the forest seems even darker. You lose.")
            else:
                print("Invalid choice. You wander aimlessly in the forest and eventually get lost. You lose.")
        else:
            print("That's not a valid option. The bear notices you and you're in trouble! You lose.")

    elif choice == "flashlight":
        print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you.")
        next_choice = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ").strip().lower()
        if next_choice == "follow":
            print("You follow the path and safely make it out of the forest. You win!")
        elif next_choice == "look":
            print("You look in the trees and find a scary monster that attacks you! You lose.")
        else:
            print("That's not a valid option. You get lost in the forest. You lose.")

    elif choice == "map":
        print("You pick up the map and study it. It shows three paths: NORTH, EAST, and SOUTH.")
        next_choice = input("Which path do you want to take? ").strip().lower()
        if next_choice == "north":
            print("You head north and find a beautiful clearing with a stream.")
            next_choice_2 = input("Do you want to REST by the stream or EXPLORE the surrounding area? ").strip().lower()
            if next_choice_2 == "rest":
                print("You rest by the stream, rejuvenated by the fresh water and peaceful surroundings. You win!")
            elif next_choice_2 == "explore":
                print("You explore the area and find a hidden cave with ancient markings. You win!")
            else:
                print("Invalid choice. You get lost in the forest. You lose.")
        elif next_choice == "east":
            print("You head east and encounter a dense thicket.")
            next_choice_2 = input("Do you want to CUT through the thicket or GO around? ").strip().lower()
            if next_choice_2 == "cut":
                print('You start cutting. The thicket never ends, you chop until your hands bleed and night falls.\n The bear comes for you. He stands on his hind legs."You got any honey?" He then procceeds to maul you. You lose.  ')
            elif next_choice_2 == "go":
                print("You go around the thicket and find an ancient ruin. You win!")
            else:
                print("Invalid choice. You get lost in the forest. You lose.")
        elif next_choice == "south":
            print("You head south and find a steep hill.")
            next_choice_2 = input("Do you want to CLIMB the hill or WALK around it? ").strip().lower()
            if next_choice_2 == "climb":
                print("You climb the hill and get a great view of the entire forest. You win!")
            elif next_choice_2 == "walk":
                print("You walk around the hill and find an abandoned cabin. A creepy stranger slowly creeps out of the house. \n Axe in hand he chases you til you meet a cliff, where you also meet, your demise. You lose")
            else:
                print("Invalid choice. You get lost in the forest. You lose.")
        else:
            print("That's not a valid option. You remain lost in the forest. You lose.")

    else:
        print("That's not a valid option. You remain lost in the dark forest. You lose.")

# Run the game
adventure_game()
