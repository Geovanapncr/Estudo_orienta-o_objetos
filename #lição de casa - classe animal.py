#lição de casa - classe animal

class Animal():
    def __init__(self, tamanho, especie, habitat ):
       self.tamanho = tamanho
       self.especie = especie
       self.habitat = habitat

class Mamiferos(Animal):
    def __init__(self, tamanho, especie, habitat, classe):
        super(). __init__(tamanho, especie, habitat)
        self.classe = classe

jacare = Animal("2M", "Paleosuchus palpebrosus", "Pântanos")
print(vars(jacare))
leao = Mamiferos("1,8M", "Panthera leo", "Savanas", "Mamifero")
print(vars(leao))

