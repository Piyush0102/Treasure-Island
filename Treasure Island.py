#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Fifteen Men on the Dead Man's Chest. Yo, Ho, Ho and a Bottle of Rum")
print("Welcome to the Treasure Island.\nHere your aim is to find the hidden treasure.")
choice1=input("You are at a crossroad. Where would you like to go?? left or right?\n").lower()
if choice1=='left':
    choice2=input("You have come to a lake. There is an island in the middle of the lake. What would you like to do?? wait or swim?\n").lower()
    if choice2=='wait':
        choice3=input("You arrived at the island unharmed. There is a house with 3 doors, one red, one yellow and one blue. Which door would you like to choose??\n").lower()
        if choice3=='red':
            print("Sorry, Game Over. You were burnt into ashes with the room!")
        elif choice3=='yellow':
            print("YaY!! You found the hidden treausre.")
        elif choice3=='blue':
            print("Sorry, Game over. You were murdered!")
        else:
            print("You choose the door that dosen't exists. Game over!")
    else:
        print("Sorry, Game Over. You drowned to death!")
else:
    print("Sorry, Game Over. You were eaten by a tiger!")


# In[ ]:





# In[ ]:




