import random
class Pokemon:
    def __init__(self,especie, level = None, nome=None):
        if especie:
            self.especie = especie
        else:
            self.especie = random()
        if level:
            self.level = level
        else: 
            self.level = random.randint(1,1000)
        if nome:
            self.nome = nome
        else:
            self.nome = especie
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
        self.ataque = self.level * 5
        self.vida = self.level * 10
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
    def __str__(self):
        return "{} ({})".format(self.nome, self.level)
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    
    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo

        print("{} perdeu {} pontos de vida!".format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado!".format(pokemon))
            return True
        else:
            return False

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self,pokemon):
        print("{} deu um raio do trovão em {}".format(self,pokemon))
        return super().atacar(pokemon)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self,pokemon):
        print("{} deu uma bola de fogo na cabeça {}".format(self,pokemon))
        return super().atacar(pokemon)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self,pokemon):
        print("{} lançou um jato de agua {}".format(self,pokemon))
        return super().atacar(pokemon)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonPlanta(Pokemon):   
    tipo = "planta"

    def atacar(self,pokemon):
        print("{} lançou folhas de navalha em {}".format(self,pokemon))
        return super().atacar(pokemon)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||