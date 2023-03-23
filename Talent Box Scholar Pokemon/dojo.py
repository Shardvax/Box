class Dojo():

    """
    Dojos are where two players can come and fight between each other!
    They simply handle the actual fights- loading player and other
    similar functions are a responsibility of a main program, not the
    dojo itself!
    """
    def __init__(self, dojo_name):
        self.dojo_name = dojo_name
        self.players = []


    def __str__(self):
        """ Prints out information about the dojo """
        return "This is {}, with {} players inside.".format(
            self.dojo_name, len(self.players))


    def add_player(self, new_player):
        if len(self.players) == 2:
            print("Sorry, but there are already the maximum capacity of players in this dojo")
            return
        if any(p.name == new_player.name for p in self.players):
            print("Sorry, this player is already in the dojo.")
            return
        self.players.append(new_player)
        print("Players {} has entered {}.".format(new_player.name, self.dojo_name))


    def start_battle(self):

        if len(self.players) != 2:
            print("Sorry, I need 2 players to start a battle, and I have {}".
                  format(len(self.players)))
            return

        # It's easier to use player1 and player2
        player1 = self.players[0]
        player2 = self.players[1]

        print("{} and {} begin to BATTLE".format(player1.name, player2.name))
        print()  # this prints an empty line, to add some space

        current_round = 0  # keep track of the current round
        while player1.has_pokemon_left() and player2.has_pokemon_left():
            # Update the current round, and add a newline
            current_round += 1
            print()
            # print that the round has begun, and gather the players
            # next pokemon.
            print("===ROUND {}===".format(current_round))
            p1s_pokemon = player1.next_pokemon()
            p2s_pokemon = player2.next_pokemon()
            # Player1 attacks player 2:
            print("{}: ".format(player1.name), end="")
            p1s_pokemon.attack(p2s_pokemon)

            # it is possible that this fainted player two's pokemon: in that
            # scenario, we need to get the next pokemon that player
            # two has.
            if not p2s_pokemon.is_alive():
                p2s_pokemon = player2.next_pokemon()

            # if player two has run out of pokemon, we need to break
            # the loop right away
            if not player2.has_pokemon_left():
                break

            # Player 2 attacks player one
            print("{}: ".format(player2.name), end="")
            p2s_pokemon.attack(p1s_pokemon)

            if player1.has_pokemon_left():
                winner = player1
                loser = player2
            else:
                winner = player2
                loser = player1

            self.players = [winner]

            # Print final statistics
            print("After a long battle, {} emerged victorious!".format(
                winner.name))
            print("{} is exiled from the {}.".format(loser.name, self.dojo_name))

if __name__ == '__main__':
    from player import Player
    from pokemon import *

    p1 = Player("Arya", [Pichu(), Pichu()])
    p2 = Player("Dummy", [TrainingDummy(), TrainingDummy()])
    p3 = Player("AnotherPlayer", [Pichu(), TrainingDummy()])

    dojo = Dojo("Ultimate Dojo of DOOM")
    dojo.add_player(p1)
    dojo.start_battle()  # this should fail!
    dojo.add_player(p1)  # this should fail!
    dojo.add_player(p2)
    dojo.add_player(p3)  # this should fail!
    print(dojo)

    dojo.start_battle()
    print(dojo)
