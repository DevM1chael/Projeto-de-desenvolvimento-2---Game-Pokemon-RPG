import random
from pokemon import *

NOMES = [
    "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
    "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonAgua("Squirtle"),
    PokemonPlanta("Bulbasaur"),
    PokemonEletrico("Pikachu"),
    PokemonPsiquico("Mewtwo"),
    PokemonDragao("Dragonite"),
    PokemonFada("Clefairy"),
    PokemonGelo("Lapras"),
    PokemonInseto("Scyther"),
    PokemonLutador("Machamp"),
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome

        else:
            self.nome = "Anônimo"   
        
        self.pokemons = pokemons
    
    def __str__(self):
        return self.nome
    
    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem nenhum pokemon".format(self))
class Player(Pessoa):
    tipo = "player"

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou  {}".format(self, pokemon))

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        
        super().__init__(nome=random.choice(NOMES), pokemons=pokemons)

meu_inimigo = Inimigo()
meu_inimigo.mostrar_pokemons()