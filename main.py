class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return "nome:{}, idade:{}".format(self.nome, self.idade)

class Heroi(Pessoa):
    def __init__(self, nome, idade, habilidade):
        super().__init__(nome, idade)
        self.habilidade = habilidade
    
    def __repr__(self):
        return "nome:{}, idade:{}, habilidade:{}".format(self.nome, self.idade, self.habilidade)

class Vilao(Pessoa):
    def __init__(self, nome, idade, arma):
        super().__init__(nome, idade)
        self.arma = arma
    
    def __repr__(self):
        return "nome:{}, idade:{}, arma:{}".format(self.nome, self.idade, self.arma)


if __name__=="__main__":
    flash = Heroi("Barry Allen", 27, "super velocidade")
    nancy = Pessoa("Nancy", 20)
    neggan = Vilao("Neggan", 50, "Taco de beisebol com arame farpado")

    print(flash)
    print(nancy)
    print(neggan)