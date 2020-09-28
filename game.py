import enemy as en

#starting the game 
player = en.Enemy("player","battle")
print("You meet another " + player.enemy + " who wants to " + player.battle + ".")
print("The enemy has " + str(player.hp) + " HP.")
print("Type the a key to accept the challenge and then RETURN to attack!")

#Battle Initiation
while True:

    action=input()

    if action.lower() == "a":
        player.fight(player)

    if player.hp < 1:
        print("You win!")