run = True
menu = True
play = False
rules = False

while run:
  while menu:
    print("1. NEW GAME")
    print("2. HOW TO PLAY")
    print("3. QUIT GAME")
    
    choice = input("> ")
    
    if choice == "1":
      print("Narrator => What's your name, hero?")
      name = input("> ")
      menu = False
      play = True
    elif choice == "2":
      print("Type the answer to the questions the game asks and press enter")
    elif choice == "3":
      quit()
  
  while play:
    print("Frank => Hi hero " + name + "!")
    input("> ")
    print("Frank => Look out! There is an evil slime coming!")
    print("1. FIGHT")
    print("2. RUN")
    choice = input("> ")
    
    if choice == "1":
      print("")
    elif choice == "2":
      print("Frank => Lets get out of here, hero!")
    