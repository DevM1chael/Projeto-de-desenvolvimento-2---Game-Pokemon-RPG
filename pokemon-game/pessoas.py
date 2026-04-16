from pokemon import *

NOMES = [
    "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
    "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
]
POKEMONS = [
    PokemonEletrico("sugachoque"),
    PokemonFogo("charmilion"),
    PokemonEletrico("raichu"),
    PokemonEletrico("pikachu"),
    PokemonAgua("squarttle"),
    PokemonAgua("margikap")
]

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome

        else:
            self.nome = "Anônimo"   
        
        self.pokemons = pokemons

        self.dinheiro = dinheiro
    
    def __str__(self):
        return self.nome

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{}) {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon".format(self))


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}!".format(self,pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não tem nenhum pokemon!")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def mostrar_dinheiro(self):
        print("Você tem ${} de dinheiro!".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade: int):
        self.dinheiro += quantidade
        print("Você ganhou ${}! ".format(quantidade))
        self.mostrar_dinheiro()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def batalhar(self, pessoa):
        print("{} desafiou {} para uma batalha!".format(self, pessoa))
    
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()


        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
        
        else:
            print("Essa batalha não pode ocorrer!")
        
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Player(Pessoa):
    tipo = "player"

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou  {}".format(self, pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha um pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} Eu escolho você!!!".format(pokemon_escolhido))
                    return pokemon_escolhido

                except:
                    print("Escolha inválida!")
        else:
            print("ERRO: Você não tem nenhum pokemon!")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
       if not pokemons:
           for i in range(random.randint(1,6)):
               pokemons.append(random.choice(POKEMONS))

       super().__init__(nome=nome,pokemons=pokemons)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    

meu_inimigo = Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemons()