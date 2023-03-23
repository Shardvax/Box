import pickle
from pokemon import Pichu, TrainingDummy, Starpecker

class Player():
    """
    This is the base class for players!
    They are expected to fill out the name, pokemon and order.
    """
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

    def next_pokemon(self):
        """ Gets the first pokemon in the players list
            of pokemon that is currently alive. """
        for pokemon in self.pokemon:
            if pokemon.is_alive():
                return pokemon
        return None  # there are no more pokemons!

    def next_pokemon(self):
        alive_pokemon = [p for p in self.pokemon if p.is_alive()]
        if alive_pokemon:
            return alive_pokemon[0]
        else:
            return None

    def has_pokemon_left(self):
        if self.next_pokemon() != None:
            return True
        else:
            return False

    def has_pokemon_left(self):
        return (self.next_pokemon() != None)

    def __str__(self):
        return "I'm player {}, and I have {} pokemon!".format(self.name, self.has_pokemon_left())

    #"I'm player <player_name>, and I have <number_of_pokemon> pokemon"
    #"I'm player Billy, and I have 4 pokemon".

    # Printing players ^
    #                  ]
    #                  [
    #                  ]
    #                  [

    def save(player, location):
        """ Saves player, which is a Player, to the file at location. """
        with open(location, "wb") as f:
            pickle.dump(player, f)

    def load(location):
        """ Loads the player from the file at location, if the file exists. """
        try:
            with open(location, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Sorry, that player does not exist...")
            exit()

if __name__ == "__main__":
    aryas_pokemons = [Pichu(), TrainingDummy()]

    player1 = Player("Arya", aryas_pokemons)
    Player.save(player1, "arya.player")

    del player1

    player1 = Player.load("arya.player")
    print(player1)
    print(player1.has_pokemon_left())
    print(player1.next_pokemon())
