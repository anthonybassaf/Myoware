import random

class Enemy():
    def __init__(self,enemy,battle):
        self.enemy=enemy
        self.battle=battle
        self.hp=40
        self.stg=random.randrange(0,20)
        self.ac=random.randrange(5,15)
        self.alive=True

    def fight(self,tgt):
        print("You take a swing at the " + self.enemy + ".")
        hit=random.randrange(0,20)

        if self.alive and hit > self.ac:
            print("You hit the " + self.enemy + " for " + str(hit) + " damage!")
            self.hp = self.hp - hit
            print("The " + self.enemy + " has " + str(self.hp) + " HP remaining.")
        else:
            print("You missed.")

        print("Type the a key and then RETURN to attack again!")

        if self.hp < 1:
            self.alive=False