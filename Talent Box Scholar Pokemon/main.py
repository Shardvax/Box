import pickle

from pokemon import ALL_POKEMON
from player import Player
from dojo import Dojo


def player_factory():
    # Log your intensions
    print("Getting another player!")

    # Try to load from a file
    response = input("Would you like to load from a file (y/N)? ")
    if response.lower().startswith('y'):  # this matches yes, yesh, YEP, yippee!
        # we are building the player from a file
        filename = input("What is your player file? ")
        return Player.load(filename)  # Error handling is done in Player.load

    # We have to build the player from scratch.
    print("Let's build you up from scratch then!")
    player_name = input("What's your name? ")
    print("Great, {}. Now, we'll pick your pokemon".format(player_name))

    # This introduces a way to get the keys of a dictionary
    print("Here's a list of all the pokemon you can pick:")
    for pokemon_name in ALL_POKEMON.keys():
        print("* {}".format(pokemon_name))
    print("When you're done picking pokemon, type DONE.")
    print()

    player_pokemon = []
    while True: # we break inside the loop
        pokemon_name = input("Pick a pokemon: ")
        if pokemon_name in ALL_POKEMON:
            new_pokemon = ALL_POKEMON[pokemon_name]() # note the end parenthesis
            player_pokemon.append(new_pokemon)

        # We break if they say "done", "DONE", or "dOnE"
        elif pokemon_name.upper() == "DONE":
            break  # we are done making pokemon

        else:
            print("Sorry, I don't recognize that pokemon. Please try again!")

    print()
    print("Great, {}. Here are your pokemon:".format(player_name))
    for pokemon in player_pokemon:
        print(pokemon)

    # Since the player has not saved themselves, we should give them that option:
    new_player = Player(player_name, player_pokemon)
    response = input("Would you like to save for future games (y/N)? ")
    if response.lower().startswith("y"):
        filename = input("What file should I save as? (eg. bob.player) ")
        Player.save(new_player, filename)

    return new_player

    # Pick the pokemon, one by one
    player_pokemon = []
    while True:  # we break inside the loop
        pokemon_name = input("Pick a pokemon: ")
        if pokemon_name in ALL_POKEMON:
            new_pokemon = ALL_POKEMON[pokemon_name]()  # note the end parenthesis
            player_pokemon.append(new_pokemon)

        # We break if they say "done", "DONE", or "dOnE"
        elif pokemon_name.upper() == "DONE":
            break  # we are done making pokemon

        else:
            print("Sorry, I don't recognize that pokemon. Please try again!")

    print()
    print("Great, {}. Here are your pokemon:".format(player_name))
    for pokemon in player_pokemon:
        print(pokemon)

    # Since the player has not saved themselves, we should give them that option:
    new_player = Player(player_name, player_pokemon)
    response = input("Would you like to save for future games (y/N)? ")
    if response.lower().startswith("y"):
        filename = input("What file should I save as? (eg. bob.player) ")
        Player.save(new_player, filename)

    return new_player

def main():
    my_dojo = Dojo("Dojo Of Death")

    player1 = player_factory()
    player2 = player_factory()

    my_dojo.add_player(player1)
    my_dojo.add_player(player2)
    my_dojo.start_battle()


if __name__ == '__main__':
    main()