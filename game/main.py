import random

def chooseOptions():
  options = ('piedra', 'papel', 'tijera')
  userOption = input("piedra, papel o tijera => ").lower()
  if not userOption in options:
    print('Opción inválida')
    return None, None
  
  computerOption = random.choice(options)
  
  print('Opción del usuario     => ', userOption)
  print('Opción de la computadora => ', computerOption)
  return userOption, computerOption

def checkRules(userOption, computerOption, userWins, computerWins):
  if userOption == computerOption:
    print("Empate")
    return userWins, computerWins
  elif userOption == "piedra":
    if computerOption == "tijera":
      print("Piedra gana a tijera")
      print("Usuario gana!")
      userWins += 1
    else:
      print("Papel gana a piedra")
      print("Computadora gana!")
      computerWins += 1
  elif userOption == "papel":
    if computerOption == "tijera":
      print("Tijera gana a papel")
      print("Computadora gana!")
      computerWins += 1
    else:
      print("Papel gana a piedra")
      print("Usuario gana!")
      userWins += 1
  else: # tijera
    if computerOption == "papel":
      print("Tijera gana a papel")
      print("Usuario gana!")
      userWins += 1
    else:
      print("Piedra gana a tijera")
      print("Computadora gana!")
      computerWins += 1
  return userWins, computerWins

def checkWinner(userWins, computerWins):
  if userWins >= 2:
    print("¡El ganador es el Usuario!")
    return True

  if computerWins >= 2:
    print("¡El ganador es la Computadora!")
    return True
    
  return False

def runGame():
  userWins = 0
  computerWins = 0
  rounds = 1

  while True:
    print('Hola,' + " " + 'Platzinauta')
    print('*' * 20)
    print('Ronda ', rounds)
    print('*' * 20)
    print("Usuario => ", userWins, "Computadora => ", computerWins)
    print('*' * 20)
  
    userOption, computerOption = chooseOptions()
    userWins, computerWins = checkRules(userOption, computerOption, userWins, computerWins)  

    rounds += 1

    if checkWinner(userWins, computerWins):
      break

runGame()
