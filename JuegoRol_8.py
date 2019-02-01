class Person:
    def __init__(self, life, position, speed):
        self.life = life
        self.position = position
        self.speed = speed

    def get_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            return "has died"
        else:
            return "has " + str(self.life) + " of life"

    def move(self, direccion, speed):
        self.position = direccion
        self.speed = speed


class Soldier(Person):
    def __init__(self, life, position, speed, attack):
        super().__init__(life, position, speed)
        self.attack = attack

    def toAttack(self, person):
        return person.get_damage(self.attack)


class Farmer(Person):
    def __init__(self, life, position, speed, farm):
        super().__init__(life, position, speed)
        self.farm = farm

    def toFarm(self):
        return str(self.farm)


winterSolder = Soldier(45, 2, 2, 20)
capitainAmerican = Soldier(100, 8, 10, 40)

jonathanKent = Farmer(18, 5, 1, 200)

print("winterSolder has " + str(winterSolder.speed) + " speed, " + str(winterSolder.life)
      + " life, " + str(winterSolder.position) + " position and do " + str(winterSolder.attack) + " damage")
print("capitainAmerican has " + str(capitainAmerican.speed) + " speed, " + str(capitainAmerican.life)
      + " life, " + str(capitainAmerican.position) + " position and do " + str(capitainAmerican.attack) + " damage")
print("jonathanKent has " + str(jonathanKent.speed) + " speed, " + str(jonathanKent.life)
      + " life, " + str(jonathanKent.position) + " position and recolected " + str(jonathanKent.farm) + " of farm")

print(" JonathanKent go to farm rice")
print("jonathanKent farmed " + jonathanKent.toFarm() + " rice\n")

print("winterSolder attack JonathanKent")
print("jonathanKent " + winterSolder.toAttack(jonathanKent) + "\n")

print("capitainAmerica attack winterSolder")
print("winterSolder " + capitainAmerican.toAttack(winterSolder) + "\n")

