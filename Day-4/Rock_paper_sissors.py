rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# This code allows you to play rock paper sissors with computerr LOLOLOL 🤪🤣😂😅
import random
elements = [rock, paper, scissors]
random_number = random.randint(0,2)

user_choice = input("Rock, Paper or Scissor. Enter R, P or S respectively\n")
wining_list = [[0,2], [2,1], [1,0]]
losing_list = [[2,0], [1,2], [0,1]]
if user_choice == "R":
 print(elements[0])
 number = 0
elif user_choice == "P":
 print(elements[1])
 number = 1
elif user_choice == "S":
 print(elements[2])
 number = 2
else:
  print('''
                                           \ / _
                                      ___,,,
                                      \_[o o]
     Errare humanum est!              C\  _\/
             /                     _____),_/__
        ________                  /     \/   /
      _|       .|                /      o   /
     | |       .|               /          /
      \|       .|              /          /
       |________|             /_        \/
       __|___|__             _//\        \
 _____|_________|____       \  \ \        \
                    _|       ///  \        \
                   |               \       /
                   |               /      /
                   |              /      /
 ________________  |             /__    /_
 b'ger        ...|_|.............. /______\.......''')
  print("You did some mistake try agian")
print(elements[random_number])
choice = [random_number, number]
print(choice)
if random_number == number:
  print("It's a Draw")
  print('''             .     .
            (>\---/<)
            ,'     `.
           /  q   p  \
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/  hjw
        `._ _/_  ___.'-\
           `--\
''')
else:
 if choice == wining_list[0] or choice == wining_list[1] or choice == wining_list[2]:
  print("Yay you have won the computer")
  print('''
      .   ,      .
          L\  o    .-""-.
           |\_    / (--> \
       o  .\ \'--.)_>_=/_(   __
     .      \ )`-._/|_,(    (==)
         o   |_\ (_   ( \  /|~~|
       o . _.' `\ ) \_/\ \/ |  |
      _ _.','\ _/\   (__'._/|()|
     |=/=/====\======/==|  /`  `\
     \ ' . o . '-..-' o / /      \
      `'-.__  o'  __.-'` ;  _/\_  ;
            `'..'`       ||`    `||
              ||         ||PARTY!||
              ||         ||      ||
          jgs ||         | \____/ |
           _.'  '._      |        |
          <        >     \_.-""-._/
           `""""""`       `""""""`''')
 else:
  print("Aww!! computer won")
  print('''
      ooooooooooooooooooooooooooooooooooooo
      8                                .d88
      8  oooooooooooooooooooooooooooood8888
      8  8888888888888888888888888P"   8888    oooooooooooooooo
      8  8888888888888888888888P"      8888    8              8
      8  8888888888888888888P"         8888    8             d8
      8  8888888888888888P"            8888    8            d88
      8  8888888888888P"               8888    8           d888
      8  8888888888P"                  8888    8          d8888
      8  8888888P"                     8888    8         d88888
      8  8888P"                        8888    8        d888888
      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
      8 .od88888888888888888888888888888888    8      d88888888
      8888888888888888888888888888888888888    8     d888888888
                                               8    d8888888888
         ooooooooooooooooooooooooooooooo       8   d88888888888
        d                       ...oood8b      8  d888888888888
       d              ...oood888888888888b     8 d8888888888888
      d     ...oood88888888888888888888888b    8d88888888888888
     dood8888888888888888888888888888888888b''')
