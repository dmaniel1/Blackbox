import main
roomInteract = ["Lamp", "Vent"]
inventory = []
while True:
  if main.sideOpen is True:
    roomInteract += "Computer maintenance door"
    roomInteract += "Computer insides"