#resources
import os
import random
import time
import storage
#functions
def wait(seconds):
  time.sleep(seconds)
def text(text, delay, color, inbetweenChar, printAfterCharPrinted, enterAfterDone):
  for i in text:
    print(color + i + reset, end=inbetweenChar, flush=printAfterCharPrinted)
    wait(delay)
  else:
    if enterAfterDone is True:
      print()
    elif enterAfterDone is False:
      print("", end="")
#normal terminal variables:
redColor = "\033[0;31m"
redBackground = "\033[41m"
reset = "\033[0m"
blueColor = "\u001B[34m"
boldBlueColor = "\033[1;34m"
boldRedColor = "\033[1;31m"
redItalics = "\033[31;49;3m"
greenColor = "\u001B[32m"
greenBackground = "\u001B[42m"
greenItalics = "\033[32;3m"
yellowColor = "\u001B[33m"
yellowBackground = "\u001B[43m"
cyanColor = "\u001B[36m"
boldCyanColor = "\033[36;49;1m"
blueBackground = "\u001B[44m"
blackColor = "\u001B[30m"
brightYellowColor = "\033[0;93m"
cyanBackground = "\033[46m"
boldWhiteColor = "\033[1;37m"
italics = "\033[3m"
clear = "\033[H\033[2J"
#global variables:
game = True
roomNum = 2
sideOpen = False
#menu = 0
#intro = 1
#room = 2
#computer on = 3
computerWelcome = True
askIfNeedHelp = True
#misc booleans
givePaper = True
#computer variables
loginOrTerm = False
loginAttempts = 0
#code:
while game is True:
  if roomNum == 0:
    print("░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓"
  "▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ \n"
  "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░"
  "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n"
  "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░"
  "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n"
  "░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░"
  "▒▓█▓▒░░▒▓██████▓▒░  \n"
  "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░"
  "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n"
  "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░"
  "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n"
  "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓████"
  "██▓▒░░▒▓█▓▒░░▒▓█▓▒░ \n")
    begin = input("Begin? [Y/N]\n")
    if begin == "Y" or begin == "y":
      print("Let's begin.")
      wait(2)
      roomNum = 1
    elif begin == "N" or begin == "n":
      print("Not like you had a choice anyway.")
      wait(3)
      roomNum = 1
  #beginning of the game
  if roomNum == 1:
    print(clear)
    text("Wake up. Get on your feet.", 0.05, greenItalics, "", True, False)
    wait(2)
    print(clear)
    text("You need to wake up.", 0.05, greenItalics, "", True, False)
    wait(2)
    print(f"{clear}You pick yourself up off the floor.")
    wait(3)
    print(f"{clear}You can't remmber who you are, where you came from, or how you got here. You don't even remember your name.")
    wait(4)
    print(f"{clear}You find yourself in a giant box with no windows, no doors, and no furniture.")
    wait(4)
    print(f"{clear}That is, except for a desk bolted to one of the walls and a singular ventilation shaft.")
    wait(5)
    print(f"{clear}There is a lamp on that desk (thank god), and it is your only source of light.")
    wait(5)
    print(f"{clear}There is also a CRT monitor on the desk. It has a power button. There is a white keyboard in front of it. No mouse. Strange.")
    wait(7)
    print(f"{clear}Then, a disembodied voice comes from nowhere.")
    wait(4)
    print(f"{clear}It says to you: \"", end="")
    wait(0.1)
    text("Welcome, welcome! Welcome to our facilities! This is where you will be spending the next [FLOAT OVERFLOW] days. Your task will be to test the terminal on the computer in front of you. Good luck! Enjoy your stay!", 0.05, greenColor, "", True, False)
    print("\"")
    wait(5)
    print(f"{clear}Is this purgatory?")
    wait(3)
    print(f"{clear}what did i do wrong?")
    wait(3)
    print(clear +"With no other forseeable options, you approach the terminal.")
    wait(3)
    print(f"{clear}Let's begin.")
    roomNum = 2
  while roomNum == 2:
    choice = input(f"{clear}What would you like to do?\n{boldWhiteColor}[1]: {reset}Interact with environment\n{boldWhiteColor}[2]: {reset}Check your inventory\n{boldWhiteColor}[3]: {reset}Use the computer\n")
    if choice == "1":
      listNumber = storage.roomInteract.__len__() - 1
      print(f"{clear}You can interact with: ", end="")
      for i in storage.roomInteract:
        if storage.roomInteract.index(i) != listNumber:
          print(f"{i}, ", end="")
        elif storage.roomInteract.index(i) == listNumber:
          print(f"and {i}.")
      print("What would you like to interact with?\n")
      for i in storage.roomInteract:
          print(f"{boldWhiteColor}{storage.roomInteract.index(i) + 1}: {reset}{i}")
      print(f"{boldWhiteColor}{listNumber + 2}: {reset}Don't interact with anything")
      inputChoice = input()
      if inputChoice == "1" and storage.roomInteract.count("Lamp") == 1:
        if givePaper is True:
          print(f"You feel around the rim of the lamp, and find a slip of paper.\n{greenColor} + Paper Note{reset}")
          storage.inventory.append("Paper Note")
          givePaper = False
          wait(3)
        else:
          print("You turn the lamp off, and you are immidiately plunged into darkness. You turn it back on.")
          wait(3)
      elif inputChoice == "2" and storage.roomInteract.count("Vent") == 1:
        print("You stand on the desk and reach up to the vent. You cannot open it.")
        wait(3)
      elif inputChoice == listNumber + 2:
        print("You do not interact with anything.")
        wait(3)
      else:
        print("Unknown input.")
    elif choice == "2":
      print(clear + "--------Inventory--------")
      if storage.inventory.__len__() > 0:
        for i in storage.inventory:
          print(i)
        print("-------------------------")
        shouldIUse = input("Would you like to use an item? [Y/N]\n")
        if shouldIUse == "Y" or shouldIUse == "y":
          print("Which item would you like to use?")
          for i in storage.inventory:
            print(f"{boldWhiteColor}{storage.inventory.index(i) + 1}: {reset}{i}")
          choose = input()
          if choose == "1" and "Paper Note" in storage.inventory:
              print("You read the note. It reads: ")
              text("Username: terminaltester", 0.05, italics, "", True, True)
              text("Password: password123", 0.05, italics, "", True, True)
              wait(4)
          else:
            print("You have no items to use.")
        elif shouldIUse == "N" or shouldIUse == "n":
          print("No item will be used.")
          wait(3)
        else:
          print("Unknown input.")
      else:
        print("Nothing here.")
        print("-------------------------")
        wait(3)
    elif choice == "3":
      print("You walk up to the monitor and press the power button. You hear it whirr to life.")
      wait(4)
      roomNum = 3
  while roomNum == 3:
    if computerWelcome is True:
      print("Welcome to the terminal. Please input credentials.")
    elif computerWelcome is False:
      print("Welcome back to the terminal. Please input your credentials.")
    else:
      print("How the fuck are you accessing this shit dawg wtf that was a boolean")
    username = input(clear + boldWhiteColor + "Username: " + reset)
    if username == "terminaltester":
      password = input(boldWhiteColor + "Password: " + reset)
      if password == "password123":
        print(greenBackground + "Access granted." + reset)
        loginAttempts = 0
        wait(2)
        print(clear)
        loginOrTerm = True
      else:
        print(redBackground + "Access denied." + reset)
        loginAttempts += 1
        wait(1.5)
        print(clear)
    else:
      print(redBackground + "Access denied." + reset)
      loginAttempts += 1
      wait(1.5)
      print(clear)
    if loginAttempts == 5:
      print("You have been locked out.")
      wait(2)
      roomNum = 2
    while loginOrTerm is True:
      if askIfNeedHelp is True:
        print("If you forgot the commands, use \"help\" to find them.")
        askIfNeedHelp = False
      else:
        print()
      command = input(boldBlueColor + "~/terminaltest" + reset + "$ ")
      if str.lower(command) == "help":
        print(boldWhiteColor + "----------COMMANDS----------" + reset)
        print("help [information about commands]")
        print("files [list of downloaded and created files]")
        print("read [reads/runs a file] (needs a specific file)")
        print("write [overwrites/appends text to a file] (needs a specific file)")
        print("create [creates a file] (only supports .py and .txt)")
        print("delete [deletes a file] (needs a specific file)")
        print("whoami [info on the user]")
        print("whatisthis [information about the terminal]")
        print("clear [clears terminal]")
        print("off [shuts off computer]")
        print(boldWhiteColor + "---------END COMMANDS---------" + reset)
      if str.lower(command) == "":
        print()
      elif str.lower(command) == "clear":
        print(clear)
      elif str.lower(command) == "files":
        with os.scandir("/home/runner/blackbox/game_files") as entries:
          for entry in entries:
              print(entry.name)
              wait(0.1)
      elif str.lower(command) == "read":
        file = "/home/runner/blackbox/game_files/" + input("File to run: ")
        if ".py" in file:
          with open(file) as file:
            exec(file.read())
        elif ".txt" in file:
          with open(file, "r") as fileToRead:
            print(fileToRead.read())
      elif str.lower(command) == "write":
        appendOrOverwrite = input("Append or overwrite? [A/O] ")
        if str.lower(appendOrOverwrite) == "o":
          writefile = "/home/runner/blackbox/game_files/" + input("File to overwrite: ")
          if writefile == "/home/runner/blackbox/game_files/q&a.txt" or writefile == "/home/runner/blackbox/game_files/welcome.txt":
            print("Error: cannot edit files created by administrator.")
          else:
            print(boldWhiteColor + "Current version:" + reset)
            with open(writefile, "r") as printCurrentVersion:
              print(printCurrentVersion.read())
            overwrite = input(boldWhiteColor + "New version:\n" + reset)
            with open(writefile, "w") as writingfile:
              writingfile.write(overwrite)
              print("Overwritten!")
        elif str.lower(appendOrOverwrite) == "a":
          appendToFile = "/home/runner/blackbox/game_files/" + input("File to overwrite: ")
          if appendToFile == "/home/runner/blackbox/game_files/q&a.txt" or appendToFile == "/home/runner/blackbox/game_files/welcome.txt":
            print("Error: cannot edit files created by administrator.")
          else:
            print(boldWhiteColor + "Current version:" + reset)
            with open(appendToFile, "r") as printCurrentVersion:
              print(printCurrentVersion.read())
            append = input(boldWhiteColor + "Text to append:\n" + reset)
            with open(appendToFile, "a") as appendingToFile:
              appendingToFile.write(append)
              print("Appended!")
      elif str.lower(command) == "create":
        filetype = ""
        filetypechoice = input("What filetype would you like to create?\n" + boldWhiteColor + "1:" + reset + " .py\n" + boldWhiteColor + "2:" + reset + " .txt\n")
        if filetypechoice == "1":
          filetype = ".py"
        elif filetypechoice == "2":
          filetype = ".txt"
        else:
          print("Error: Unknown filetype.")
        filename = input("What would you like the file to be named? ")
        if filename + filetype in [entry.name for entry in os.scandir("/home/runner/blackbox/game_files")]:
          print("Error: File already exists.")
        else:
          try:
            with open("/home/runner/blackbox/game_files/" + filename + filetype, "x") as fileToCreate:
              pass
            print("File has been created.")
          except FileExistsError:
            print("Error: File already exists.")
      elif str.lower(command) == "delete":
        fileToDelete = "/home/runner/blackbox/game_files/" + input(boldWhiteColor + "File to delete: " + reset)
        if fileToDelete == "/home/runner/blackbox/game_files/q&a.txt" or fileToDelete == "/home/runner/blackbox/game_files/welcome.txt":
          print("Error: Cannot delete files created by administrator.")
        else:
          if os.path.exists(fileToDelete):
            os.remove(fileToDelete)
          else:
            print("Error: File does not exist.")
      elif str.lower(command) == "whoami":
        print(boldWhiteColor + "----------USER INFO----------" + reset)
        wait(.1)
        print(boldWhiteColor + "Username: " + reset + "terminaltester")
        wait(.1)
        print(boldWhiteColor + "Password: " + reset + "password123")
        wait(.1)
        print(boldWhiteColor + "First name: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"ufname\"" + reset)
        wait(.1)
        print(boldWhiteColor + "Last name: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"ulname\"" + reset)
        wait(.1)
        print(boldWhiteColor + "Age: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"uage\"" + reset)
        wait(.1)
        print(boldWhiteColor + "Gender: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"ugender\"" + reset)
        wait(.1)
        print(boldWhiteColor + "Occupation: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"uoccupation\"" + reset)
        wait(.1)
        print(boldWhiteColor + "Location: " + boldRedColor + "ERROR: UNDEFINED VARIABLE: \"uloc\"" + reset)
        wait(.1)
        print(boldWhiteColor + "---------END USER INFO---------")
      elif str.lower(command) == "whatisthis":
        print(boldWhiteColor + "----------TERMINAL INFO----------")
        wait(.1)
        print(boldWhiteColor + "Terminal name: " + reset + "Blackbox 5")
        wait(.1)
        print(boldWhiteColor + "Terminal version: " + reset + "1.2.4a")
        wait(.1)
        print(boldWhiteColor + "Terminal company: " + redColor + "Error: Administrator has restricted this information." + reset)
        print(boldWhiteColor + "Computer name: " + reset + "Crane Tech. CRTs")
        wait(.1)
        print(boldWhiteColor + "Computer model: " + reset + "cCRT2")
        print(boldWhiteColor + "Display type: " + reset + "Color CRT")
        wait(.1)
        print(boldWhiteColor + "Display resolution: " + reset + "1024x768 px")
        wait(.1)
        print(boldWhiteColor + "Refresh rate: " + reset + "160 Hz")
        wait(.1)
        print(boldWhiteColor + "Bit depth: " + reset + "32-bit")
        wait(.1)
        print(boldWhiteColor + "---------END TERMINAL INFO---------" + reset)
      elif str.lower(command) == "off":
        print("Shutting down...")
        wait(1)
        roomNum = 2
        break
      else:
        print("Error: Unknown command.")