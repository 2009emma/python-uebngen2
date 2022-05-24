import random

print ("Herzlich willkommen!")
print ("du spielst. Schere, Stein, Papier: gebe bitte eine Auswahl ein:")
#computer = input ()
player =  input ()
auswahl = ["Schere", "Papier", "Stein"]
#computer = "schere"
comuter = random.choice(auswahl)

# gitHub.com


# != nicht gleich 
if player != "schere" and player != "Papier" and player != "Stein":
   print("Es gibt leider nicht diese Möglichkeit")
   player = input()



if player == "Stein" and computer == "Schere":
    print("Gewonnen") 
if player == "Papier" and computer == "Schere":
    print("Verloren")
if player == "Schere" and computer == "Schere":
    print( "Unendschieden")




