class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade




    def __str__(self) -> str:
        return f"{self.get_nome()}:{self.get_idade()}"


class Moto:
    def __init__(self):
        self.__pessoa: Pessoa | None = None
        self.__power: int = 1
        self.__time: int = 0

    def get_pessoa(self):
        return self.__pessoa
    def set_pessoa(self, pessoa: Pessoa | None):
        self.__pessoa = pessoa

    def get_potencia(self):
        return self.__power
        
    def buytime(self, time: int):
        self.__time += time
        
    def setpower(self, power: int):
        self.__power = power    

    def inserir(self,pessoa: Pessoa):
        if self.get_pessoa() != None:
            print("fail: busy motorcycle")
            return
        self.set_pessoa(pessoa)

    def remover(self) -> Pessoa | None:
        aux = self.get_pessoa()
        self.set_pessoa(None)
        return aux
    
    def honk(self):
        letra = "e"
        print("P"+(letra*self.get_potencia())+"m")

    def drive(self, distancia: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.get_pessoa() == None:
            print("fail: empty motorcycle")
            return
        if self.get_pessoa().get_idade() > 10:
            print("fail: too old to drive")
            return
        if self.__time < distancia:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
            return
        self.__time -= distancia







    def __str__(self) -> str:
        pessoa = self.__pessoa if self.__pessoa != None else "empty"
        return f"power:{self.__power}, time:{self.__time}, person:({pessoa})"

def main():
    moto = Moto()

    while True:
        line = input()
        print("$"+ line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = args[2]
            pessoa = Pessoa(nome, int(idade))
            moto.inserir(pessoa)
        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa == None:
                print("fail: empty motorcycle")
            else:
                print(f"{pessoa}")
        elif args[0] == "honk":
            moto.honk()
        elif args[0] == "init":
            moto.setpower(int(args[1]))
        elif args[0] == "buy":
            moto.buytime(int(args[1]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))

main()