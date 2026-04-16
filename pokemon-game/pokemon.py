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

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    
    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self,pokemon):
        print("{} deu um raio do trovão em {}".format(self,pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self,pokemon):
        print("{} deu uma bola de fogo na cabeça {}".format(self,pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self,pokemon):
        print("{} lançou um jato de agua {}".format(self,pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self,pokemon):
        print("{} lançou folhas de navalha em {}".format(self,pokemon))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||