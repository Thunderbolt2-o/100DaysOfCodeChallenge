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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

l_or_r = input("Do you want to left or right, enter L or R\n")
if l_or_r == "R":
    print("You are taken away by ghosts. Game Over.")
    print('''           ,
        .--')
       /    /
      |    /
   /`.\   (_.'\
   \          /
    '--. .---'
jgs   ( " )
       '-'
                ,
                 \`-,      ,     =-
             .-._/   \_____)\
            ("              / =-
             '-;   ,_____.-'       =-
  jgs         /__.'


       .-.
      ( " )
   /\_.' '._/\
   |         |
    \       /
     \    /`
   (__)  /
jgs`.__.' 
 Game Over''')
else:
 print("Now you have just came accross a river do you to:-")
 s_or_w = input("swim or wait for the boat, Enter S or W\n")
 if s_or_w == "S":
  print("OMG you are eatean by a very big crocodile")
  print('''                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-' ''')
 elif s_or_w == "W":
  print("A boat just came, great go a head")
  print("You just came infront of three doors, Red, Yellow,and Blue")
  door_choice = input("Which door do you want to open R, Y or B")
  if door_choice == "R":
   print("There is a teleporter inside, your now teleported to sun")
   print('''              /         -/          ,                   
               #        .#         -#.                   
               #        #,       -##.                    
               #       ,#       %##                      
               #       -##     /##                       
               #,       ###    ###                       
               ##/      ;##    ###                       
     ,         ####+     ##-   ###            .          
      %        ,#####   ;##-  :###     -#####/           
      :%         ;###   ###  #####    :##+,              
      ,#;         ###::/##########   ,###                
       ##/..,-    ####/,   .-:###;   ###=                
       ,#######:  ##=          .%#+#####                 
        ,#######=++              -#####=                 
             ####;                .##;                   
              ##/  ;###%    ,%##%- ,#                    
               % ,#:-=##=  ,#/::+#= +;=.   %###=         
               -           #.     ,  ###:;#######=       
 =;      +###%#    -####, -+ +###-   #######;   -:=.     ?
  =#+  :#######    -,##   ;: ,##%.   +#####,             
   -###########      .    /:   .     /#//:               !
    .#####:/##%           //         /                   
              %           /+         /-                  !
              #           :#         ##/  ,-             
            /##.          +#         ########+           1
          =####/         %##        /#########+          
         ,######,                  .; +##%-  +#=         
         ########     :#+#%###/    #          =#.        
       ,%###   -##      .;#/,     ###           /.       1
 .:+######%    .###.     #/%:   -####                    
      =//-    =#####+.    =,  ,#; %###=                  
              #########:   ./###   #####:                
              #####% ###########    +####=               
              ####   #####%  ###       /#%               
              ###/   #####   ###        ##               
             .###.   ####   /###,       ,#               
            -###=    ####    %##+        #               
          -###%,     ####.    %##        --              
         ;:.         ;###=     ##         .              
                     .###=     +#                -dulle mari
                     =###      =/                        
                     ###       ,.                        
                    ;#:                                  
                    #.                                   
                   -                     ''')
  elif door_choice == "Y":
   print("Yay!! you won the treasure")
   print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
  else:
   print("You have disturbed a sleeping Vampire he is going take blood")
   print('''     /######\
               /##########\
              /   \###/    \
             /     \#/      \
          /\|               |/\
          | | \ ==\    /== / | |
           \|  \<|>\  /<|>/  |/     /|
    \__     |    -   \  -    |     /#|
     \#\     |        |      |   /###|
      \##\   |       \|     |  /#####|
       \###\  |   _______  | /######|
        \####\ | / \/ \/ \|/#######|
        |######\|        |#########|
        |########\______/##########|
        |#########\    /##########/
        |##########\  |#########/\
        /###########\/########/###\
    /################\######/########\
   /##################\###/###########\
  /###################\#/##############\
 /####################/#################\
/###################/####################''')
