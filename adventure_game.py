import os
os.system('clear')
import time

def clear_screen():
    # Clears the terminal screen on Windows and Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds):
    # Small helper to slow down dramatic moments
    time.sleep(seconds)
    
def intro():
    clear_screen()
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("             👾👽THE STRANGE HOUSE👽👾            ")
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    print("            (TEXT-BASE ADVENTURE GAME)\n")
    print("-" * 50 +"\n")
    print("""
    On a late scary night you find yourself on the front porch of a small scary house.
    And it was rumored that it was haunted and everyone the enters dies.
    But you have to enter the house because something in your head is telling you to enter the strange
    house and you need to escape the house safely. So you stand on the front porch and wonder where to go in.
    """)
    pause(2)
    choice = input("Do you enter through the 'back door', 'front door', or 'window'? ").lower()
    
    if choice == 'back door':
        kitchen()
    elif choice == 'front door':
        living_room()
    elif choice == 'window':
        bedroom()
    else:
       print("Invaild choice. Try again. ")
       intro()

def kitchen():
    clear_screen()
    print("M" * 50)
    print("                    🔪kitchen🔪              ")
    print("W" * 50 +"\n")
    print("""
    You step into the kitchen, the faint hum of the refrigerator breaking the silence. The air feels colder here. 
    In front of you, two doors stand out against the dim light—one is black, its surface faintly glowing with an eerie shimmer, 
    while the other is deep red, a low, flickering light seeping out from beneath it.\n Something about both feels wrong, yet you know you 
    have to decide. To move forward, you must choose the right door. 
     """)
    pause(2)
    choice = input("Do you want to enter the 'black door' or 'red door'? ")

    if choice == 'red door':
        dining_room()
    elif choice == 'black door':
        game_over("You were possessed by thr glowing light in the room which it was a ghost. ")
    else:
       print("Invaild choice. Try again. ")
       kitchen()
      
def living_room():
    clear_screen()
    print("M" * 50)
    print("                    🤖living room🤖              ")
    print("W" * 50 +"\n")
    print("""
   You’ve entered the living room. The air feels strangely still, heavy with quiet tension. 
   Two doors stand before you—one painted deep blue, a faint light glowing from beneath it, and the other a soft yellow, 
   with a gentle rustling sound coming from the room beyond. 
   You pause for a moment, uncertain of what lies behind either one.
    """)
    pause(2)
    choice = input("Do you want to enter the 'blue door' or 'yellow door'? ")
    
    if choice == 'blue door':
        dining_room()
    elif choice == 'yellow door':
        landry_room()
    else:
       print("Invaild choice. Try again. ")
       living_room()

def bedroom():
    clear_screen()
    print("M" * 50)
    print("                    🛏️bedroom🛏️              ")
    print("W" * 50 +"\n")
    print("""
   You have crawled into a small bedroom. The air feels still, almost too quiet—except for two sounds. 
   From the closet comes a faint noise, something soft and rhythmic, almost like someone eating. Across the room stands a pink door, 
   a gentle rustling sound coming from behind it.\n You can feel a strange tension in the air as you realize theres no turning back. 
   You have to choose one of the two paths if you want to move on to the next part of the game. 
    """)
    pause(2)
    choice = input("Do you want to enter the 'pink door' or 'closet'? ")
    
    if choice == 'pink door':
        landry_room()
    elif choice == 'closet':
        game_over("You were dragged into the closet and never seen again")
    else:
       print("Invaild choice. Try again. ")
       bedroom()

def landry_room():
    clear_screen()
    print("M" * 50)
    print("                    👕landry room👖              ")
    print("W" * 50 +"\n")
    print("""
    You step into the room, the steady rustling of the dryer echoing softly around you. The air feels warm and heavy, 
    carrying the faint scent of fabric softener.\n In the corner, you notice a single green door, faint light spilling out from underneath it.
    It seems to be the only way forward—there are no other entrances or exits in sight.
          """)
    pause(2)
    choice = input("You enter the 'green door'. ")
    
    if choice =='green door':
        guest_room()
    else:
       print("Invaild choice. Try again. ")
       landry_room()

def dining_room():
    clear_screen()
    print("M" * 50)
    print("                    🍽️dining room🍽️              ")
    print("W" * 50 +"\n")
    print("""
   As you step into the dining room, the air seems to shift, heavy with silence. In front of you stands a deep purple door, 
   its surface glimmering faintly in the dim light. From the narrow gap beneath it, a strange glow seeps out — soft, unsteady, 
   and beckoning you closer.
          """)
    pause(2)
    choice = input("You enter the 'purple door'. ")
    
    if choice =='purple door':
        guest_room()
    else:
       print("Invaild choice. Try again. ")
       dining_room()
    
def guest_room():
    clear_screen()
    print("M" * 50)
    print("                    🍩guest room🍩              ")
    print("W" * 50 +"\n")
    print("""
    You have entered the guest room. The space is quiet, sunlight filtering faintly through the curtains.
    On the neatly made bed rests a single donut—it looks fresh, soft, and strangely irresistible, its sweet scent filling the air.
    You glance toward the window, where a cool breeze drifts in, offering a chance to escape.
    You can either climb out the window and leave… or take a bite of the delicious-looking donut waiting on the bed.
          """)
    pause(2)
    choice = input("Do you want to exit 'out the window' or take a bite of the 'donut'? ")
    
    if choice == 'out the window':
        win()
    elif choice == 'donut':
        game_over("You had eaten the donut and you were poisoned and died. ")
    else:
       print("Invaild choice. Try again. ")
       guest_room()

def game_over(reason):
    print("\nGAME OVER: " + reason)
    pause(4)
    play_again()

def win():
    print("\nYou have escaped 'THE STRANGE HOUSE' goodjob! ")
    pause(2.5)
    play_again()

def play_again():
    clear_screen()
    choice = input("\nWould you like to play again yes or no: ").lower()
    if choice == 'yes':
        intro()
    else:
       print("\nThank you for playing my game! Byeeee!")

# Start the game
intro()