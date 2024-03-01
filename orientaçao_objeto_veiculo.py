#AULA 1
#caracteristicas da classe - Init é responsavel por ditar as caracteristicas da classe as coisas que devem ter
class Veiculo ():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

class Aviao():
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano 

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilidrada):
        super().__init__(tipo, chassi, marca, modelo, ano)#atributos e metodos de outra classe
        self.cilindrada = cilidrada
#Aula 2
#instanciando a classe carro e atribuindo as caracteristicas necessarias do carro que é pedida pela classe
carro = Veiculo("carro", "1234567", "ferrari", "x001", "2012")
print(vars(carro))

objeto_aviao = Aviao("carga", "quadrimotor", "soulcode airlines", "airbus a 380", "2010")
print(vars(objeto_aviao))

v = Veiculo('carro', "98789098987", 'Ferrari', 'f112', '2017')
print(vars(v))
m = Motocicleta('motocicleta', '545343488975', 'Honda', 'CG', '2008', 150)
print(vars(m))