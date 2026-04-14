import random

class Pokemon:
    def __init__(self, especie, level=random.randint(1, 100), nome=None):
        self.especie = especie 
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon))


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self,pokemon):
        print("{} deu um raio do trovão em {}".format(self,pokemon))

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self,pokemon):
        print("{} deu uma bola de fogo na cabeça {}".format(self,pokemon))

class PokemonAgua(Pokemon):
    tipo = "Agua"

    def atacar(self, pokemon):
        print("{} lançou um jato de agua {}".format(self, pokemon))


class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self, pokemon):
        print("{} lançou folhas cortantes em {}".format(self, pokemon))


class PokemonPsiquico(Pokemon):
    tipo = "psiquico"

    def atacar(self, pokemon):
        print("{} usou confusão em {}".format(self, pokemon))


class PokemonDragao(Pokemon):
    tipo = "dragao"

    def atacar(self, pokemon):
        print("{} usou sopro do dragão em {}".format(self, pokemon))


class PokemonFada(Pokemon):
    tipo = "fada"

    def atacar(self, pokemon):
        print("{} usou brilho mágico em {}".format(self, pokemon))


class PokemonGelo(Pokemon):
    tipo = "gelo"

    def atacar(self, pokemon):
        print("{} usou raio de gelo em {}".format(self, pokemon))


class PokemonInseto(Pokemon):
    tipo = "inseto"

    def atacar(self, pokemon):
        print("{} usou picada em {}".format(self, pokemon))


class PokemonLutador(Pokemon):
    tipo = "lutador"

    def atacar(self, pokemon):
        print("{} usou soco dinâmico em {}".format(self, pokemon))


meu_pokemon  =  PokemonFogo("charmander")
meu_amigo  =  PokemonEletrico("pikachu")

print(meu_pokemon, meu_pokemon.tipo)
print(meu_amigo, meu_amigo.tipo)

meu_pokemon.atacar(meu_amigo)
meu_amigo.atacar(meu_pokemon)