# __Global Var__
import random

step = 0
sum = 0

table = ["0", "0", "0",
         "0", "0", "0",
         "0", "0", "0"]


# 100 Games
for x in range(100):

 sum = sum + step

# Game Still Going
 continueplay = True
# Steps Reset
 step = 0
# Board Reset
 table = ["0", "0", "0",
          "0", "0", "0",
          "0", "0", "0"]


 def display_table():
     print(table[0] + " | " + table[1] + " | " + table[2])
     print(table[3] + " | " + table[4] + " | " + table[5])
     print(table[6] + " | " + table[7] + " | " + table[8])


 def play_game():
         display_table()

         while continueplay:
             handle_turn()

             check_if_game_over()


 def handle_turn():
     print("Position Given:")
     # Chooses Random Board Position
     position = random.randint(0, 8)
     print(position)
     if table[position] == "0":

         rings = ['1', '2', '3']
         print("Ring Size: ")
         # If Board Position Blank, Chooses Random Ring Size
         table[position] = random.choice(rings)
         print(table[position])
         STEPS()
         display_table()

     elif table[position] == '1':
         print("Ring Size: ")
         rings1 = ['2', '3']
         # If Board Position Already Has A Small Ring Size, Adds A Random Bigger One
         table[position] = random.choice(rings1)
         print(table[position])
         STEPS()
         display_table()

     elif table[position] == '2':
         print("Rings Size: ")
         # If Board Position Already Has A Medium Sized Ring, Adds The Large One
         table[position] = '3'
         print(table[position])
         STEPS()
         display_table()

     elif table[position] == '3':
         print("Ring Size: ")
         print(table[position])
         display_table()


 def check_if_game_over():
     check_if_win()


 def check_if_win():
     check_rows()

     check_columns()

     check_diagonals()

     return


 def check_rows():
     # Set Up Global Variables
     global continueplay
     # Check Rows
     row_1 = table[0] == table[1] == table[2] != "0"
     row_2 = table[3] == table[4] == table[5] != "0"
     row_3 = table[6] == table[7] == table[8] != "0"
     if row_1 or row_2 or row_3:
         continueplay = False
     elif table[0] == '1' and table[1] == '2' and table[2] == '3':
         continueplay = False
     elif table[3] == '1' and table[2] == '2' and table[1] == '3':
         continueplay = False
     elif table[3] == '1' and table[4] == '2' and table[5] == '3':
         continueplay = False
     elif table[5] == '1' and table[4] == '2' and table[3] == '3':
         continueplay = False
     elif table[0] == '1' and table[1] == '2' and table[2] == '3':
         continueplay = False
     elif table[3] == '1' and table[2] == '2' and table[1] == '3':
         continueplay = False

     return


 def check_columns():
     # Set Up Global Variables
     global continueplay
     # Check Columns
     col_1 = table[0] == table[3] == table[6] != "0"
     col_2 = table[1] == table[4] == table[7] != "0"
     col_3 = table[2] == table[5] == table[8] != "0"
     if col_1 or col_2 or col_3:
         continueplay = False
     elif table[0] == '1' and table[3] == '2' and table[6] == '3':
         continueplay = False
     elif table[6] == '1' and table[3] == '2' and table[0] == '3':
         continueplay = False
     elif table[1] == '1' and table[4] == '2' and table[7] == '3':
         continueplay = False
     elif table[7] == '1' and table[4] == '2' and table[1] == '3':
         continueplay = False
     elif table[2] == '1' and table[5] == '2' and table[8] == '3':
         continueplay = False
     elif table[8] == '1' and table[5] == '2' and table[2] == '3':
         continueplay = False

     return


 def check_diagonals():
     # Set Up Global Variables
     global continueplay
     # Check Columns
     diag_1 = table[0] == table[4] == table[8] != "0"
     diag_2 = table[6] == table[4] == table[2] != "0"

     if diag_1 or diag_2:
         continueplay = False
     elif table[0] == '1' and table[4] == '2' and table[8] == '3':
         continueplay = False
     elif table[8] == '1' and table[4] == '2' and table[0] == '3':
         continueplay = False
     elif table[2] == '1' and table[4] == '2' and table[6] == '3':
         continueplay = False
     elif table[6] == '1' and table[4] == '2' and table[2] == '3':
         continueplay = False

     return


 def STEPS():
     # Steps Per Game
     global step
     step = step + 1
     print("Step: ")
     print(step)

     return

 play_game()

# Average Steps Per Game
avg = sum/100
print("Average Moves Per Game: ")
print(int(avg))