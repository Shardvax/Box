class Pokemon():
    '''
    awdBase class, representing all Pokemon. Base classes can
    describe features that are common to all Pokemon. In this case,
    we want all pokemon to have a name and a health. If their health is
    zero or below, the pokemon is fainted.
    """
    '''
    def __init__(self):
        """ Initializes a new pokemon. Subclasses are responsible for setting
            the name, and the health.
        """
        self.name = ""
        self.health = 0

    def __str__(self):
        """ This overwrites the printing of all our pokemon! """
        return "{} (health: {})".format(self.name, self.health)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

        # Note: this can also be written as:
        return self.health > 0

    def attack(self, other_pokemon):
        """ All pokemon have the ability to attack another pokemon!"""
        raise NotImplementedError(
            "Sorry, all subclasses have to write their own attack function!")


class Pichu(Pokemon):
    """
    Baby Pikachu. Quite weak, but makes an adoreable zap sound!
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Pichu"
        self.health = 30  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 10
        if other_pokemon.is_alive():  # still alive
            print("Pichu ZAPPED {}, dealing 2 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Pichu ZAPPED {}, which faints".format(other_pokemon.name))


class Starpecker(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Starpecker"
        self.health = 170  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 14
        if other_pokemon.is_alive():  # still alive
            print("Starpecker slashed at {}, dealing 14 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Starpecker killed {}".format(other_pokemon.name))

class DarkDemon(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Dark Demon"
        self.health = 100  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 25
        if other_pokemon.is_alive():  # still alive
            print("Dark Demon punished {}, dealing 25 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Dark Demon took advantage of the situation and killed {}".format(other_pokemon.name))

class FireWarrior(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Fire-Bound Warrior"
        self.health = 175  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 15
        if other_pokemon.is_alive():  # still alive
            print("Fire-Bound Warrior burnt {}, dealing 5 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Fire-Bound Warrior KO'ed {}".format(other_pokemon.name))

class MysticalArcher(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Mystical Archer"
        self.health = 150  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 17
        if other_pokemon.is_alive():  # still alive
            print("Mystical Archer shot {}, dealing 17 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Mystical Archer slayed {}".format(other_pokemon.name))

class GalaxyWing(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Galaxy's Wing"
        self.health = 120  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 30
        if other_pokemon.is_alive():  # still alive
            print("Galaxy's Wing hit {}, dealing 30 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Galaxy's Wing slapped {} out of the world".format(other_pokemon.name))


class OverPowered(Pokemon):
    """
    Medium-sized flying creature that takes its prey by picking them up with its hard claws,
    then dropping it from the sky then snatching and flying away with it.
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Galaxy's Wing"
        self.health = 12000  # so smol

    def attack(self, other_pokemon):
        other_pokemon.health -= 2500
        if other_pokemon.is_alive():  # still alive
            print("Galaxy's Wing hit {}, dealing 30 damage [{}]".format(
                other_pokemon.name, other_pokemon.health))
        else:
            print("Demon slapped {} out of the world".format(other_pokemon.name))

class TrainingDummy(Pokemon):
    """
    Baby Pikachu. Quite weak, but makes an adoreable zap sound!
    """

    def __init__(self):
        """ Makes sure to overwrite the methods of the base class! """
        self.name = "Training Dummy"
        self.health = 125  # so smol

    def attack(self, other_pokemon):
       print("Training Dummy just sat there...")

ALL_POKEMON = {"Pichu": Pichu, "Training Dummy": TrainingDummy, "Starpecker": Starpecker, "Galaxy's Wing": GalaxyWing, "Fire-Bound Warrior": FireWarrior,
               "Mystical Archer": MysticalArcher, "Dark Demon": DarkDemon}


'''pichu = Pichu()
print(pichu)
dummy = TrainingDummy()
print(dummy)
starpecker = Starpecker()
print(starpecker)
pichu.attack(dummy)
starpecker.attack(dummy)

print(pichu)
print(starpecker)
print(dummy)'''

