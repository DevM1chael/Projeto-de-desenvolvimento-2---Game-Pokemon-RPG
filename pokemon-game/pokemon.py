class Pokemon:
    def init(self,especie, level=1, nome=None):
        self.especie = especie 
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def str(self):
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

    def atacar(self,pokemon):
        print("{} lançou um jato de agua {}".format(self,pokemon))


meu_pokemon  =  PokemonFogo("charmander")
meu_amigo  =  PokemonEletrico("pikachu")

print(meu_pokemon, meu_pokemon.tipo)
print(meu_amigo, meu_amigo.tipo)

meu_pokemon.atacar(meu_amigo)
meu_amigo.atacar(meu_pokemon)