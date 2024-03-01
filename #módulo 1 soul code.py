#módulo 1 soul codE

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

#Aula 2
#instanciando a classe carro e atribuindo as caracteristicas necessarias do carro que é pedida pela classe
carro = Veiculo("carro", "1234567", "ferrari", "x001", "2012")
print(vars(carro))

objeto_aviao = Aviao("carga", "quadrimotor", "soulcode airlines", "airbus a 380", "2010")
print(vars(objeto_aviao))

#liçaõ de casita - fazer outros objetos e classes
class Casa():
    def __init__(self, tamanho, n_comodos, preco):
        self.tamanho = tamanho
        self.n_comodos = n_comodos 
        self.preco = preco

casa1 = Casa("100m", "5", "500.000.000")
print(vars(casa1))
casa2 = Casa("150m", "6", "550.000.000")
print(vars(casa2))

#Aula 3 - INIT e SELF
class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario 

#SELF - parametro que se refere ao objeto (a ele mesmo), caracteristicas relacionadas a ele mesmo
#INIT - metodo relacionado ao CONSTRUTOR

#Aula 4 - ATRIBUTOS E METODOS
#ATRIBUTOS - caracteristicas que as classes recebem nas suas construções
#METODOS - ações que as classes executam 

class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome         
        self.cpf = cpf          #atributos
        self.salario = salario 

    #metodos
    def get_salario(self):
        print("Meu salário é:", self.salario)  #ação do metodo

    def get_bonificacao(self):
        bonificacao = self.salario * 0.15
        return bonificacao + self.salario
        
#objeto 
jose = Funcionario( "josé", "12345", 5000)
jose.get_salario()
print(jose.get_bonificacao())

#Aula 5 - Encapsulamento: esconder métodos e atributos para que não sejam acessados por outras classes/usuarios 
class Funcionario():
    def __init__(self, nome, cargo, valor_hora):
        self.nome = nome         
        self.cargo = cargo          #atributos
        self.valor_hora = valor_hora

        self.__salario = 0 #atributo privado com dois underlines, valor atribuido dentro da classe
        self.__horas_trabalhadas = 0 #privada

    #decorador property -     
    @property
    def salario (self):
        return self.__salario

    #metodo setter - onde atribuiremos o valor do salario, nesta função se o funcionario tentar atribuir o salário diretamente vai receber esse erro
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar salário diretamente, use a função calcula_salario().")
    
    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora

jose = Funcionario('José', 'Professor', 50)

#Aula 6 - Herança: uma classe filha puxa as funções de uma classe mãe
#classe mãe
class Veiculo ():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilidrada):
        super().__init__(tipo, chassi, marca, modelo, ano)#atributos e metodos de outra classe
        self.cilindrada = cilidrada

v = Veiculo('carro', "98789098987", 'Ferrari', 'f112', '2017')
print(vars(v))
m = Motocicleta('motocicleta', '545343488975', 'Honda', 'CG', '2008', 150)
print(vars(m))

#Aula 7 - Associação: criação de vinculo entre duas classes existentes
class Escritor():
    def __init__(self, nome):
        self.__nome = nome 
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter 
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta():
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("caneta esta escrevendo...")

escritor = Escritor('José')
caneta = Caneta('BIC')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()