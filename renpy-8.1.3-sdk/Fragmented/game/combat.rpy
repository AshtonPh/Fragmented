init python:
    class Entity:

        def __init__(self, character, name, HP = 10, AC = 10, ATK = 3):
            self.c = charaScter
            self.name = name
            self.HP = HP
            self.AC = AC
            self.ATK = ATK

        def attack(self, target):
            target.HP -= self.ATK

$P = Entity(Character("Player"), "Player", 10, 10, 3)
$W = Entity(Character("Wolf"), "Wolf", 5, 5, 5)


label combat:
    while ($P.HP > 0 and $W.HP > 0):
        $P.HP -= $W.ATK
        $W.HP -= $P.ATK
        print ("Player HP: " + str($P.HP))
        print ("Wolf HP: " + str($W.HP))