import random
import pickle
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


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo!")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Jogo carregado com sucesso!")
            return player
    except Exception as error:
        print("Erro ao carregar jogo!")
        print(error)
        return None

# --- Programa Principal ---

# 1. Cria o jogador

if __name__ == "__main__":
    print('____________________________')
    print("Bem-vindo ao mundo Pokemon!")
    print('____________________________')

    player = carregar_jogo()

    if not player:
        nome = input("Digite seu nome: ")
        player = Player(nome)
        print('____________________________')
        print("Olá {}! esse é um mundo habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons".format(nome))
        print("Capture o máximo de pokemons que conseguir e lute com seus inimigos")
        player.mostrar_dinheiro()

    
    if player.pokemons:
        print("Já vi que você tem alguns pokemons")
        player.mostrar_pokemons()
    else:
        print("Você não tem nenhum pokemon! Por tanto precisa escolher um para começar:")
        escolher_pokemon_inicial(player)
    
    print("Pronto, agora que você já possui um pokemon, enfrente seu arqui-inimigo Gary!")
    gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squarttle", level=1)])
    player.batalhar(gary)
    salvar_jogo(player)

    while True:
        print('____________________________')
        print("O que você deseja fazer?")
        print("1 - Explorar pelo mundo a fora")
        print("2 - Batalhar com um inimigo")
        print("3 - Ver Pokeagenda")
        print("0 - Sair do jogo")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            player.batalhar(Inimigo())
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        elif escolha == "0":
            print("Obrigado por jogar!")
            print('Fechando o jogo...')
            print('____________________________')
            break
        else:
            print("Escolha inválida!")