import random
from pokemon import *
from pessoas import *

def escolher_pokemon_inicial(player):
    print("olá {}! Escolha seu pokemon inicial:".format(player))
    pokemon1 = PokemonEletrico("Pikachu", level=1)
    pokemon2 = PokemonFogo("Charmilion", level=1)
    pokemon3 = PokemonAgua("Squarttle", level=1)

    print("Você possui três escolhas:")
    print("1 - {}".format(pokemon1))
    print("2 - {}".format(pokemon2))
    print("3 - {}".format(pokemon3))

    while True:
        escolha = input("Escolha um pokemon: ")
        if escolha == "1":
            player.capturar(pokemon1)
            break
        elif escolha == "2":
            player.capturar(pokemon2)
            break
        elif escolha == "3":
            player.capturar(pokemon3)
            break
        else:
            print("Escolha inválida!")
        
        player.mostrar_pokemons()


# --- Programa Principal ---

# 1. Cria o jogador
player = Player("Michael")

# 2. Escolhe o inicial
escolher_pokemon_inicial(player)

# 3. Mostra os pokemons do jogador
player.mostrar_pokemons()