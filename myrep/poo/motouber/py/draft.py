class Pessoa:
    def __init__(self, nome: str, money: int):
        self.__nome = nome
        self.__money = money

    def getNome(self):
        return self.__nome
    def getMoney(self):
        return self.__money
    def setNome(self, nome: str):
        self.__nome = nome
    def setMoney(self, money: int):
        self.__money = money
    
    

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__money}"

class Moto:
    def __init__(self):
        self.__custo: int = 0
        self.__passageiro: Pessoa | None = None
        self.__motorista: Pessoa | None = None
    
    def setDrive(self, pessoa: Pessoa):
        if self.getDrive() != None:
            print("fail: já tem um motorista")
            return
        self.__motorista = pessoa

    def setPass(self, pessoa: Pessoa | None):
        if pessoa is None:
            self.__passageiro = None
            return
        if self.__passageiro is not None:
            print("fail: já tem um passageiro")
            return
        self.__passageiro = pessoa
    def setCusto(self, custo: int):
        self.__custo += custo

    def getDrive(self):
        return self.__motorista
    def getPass(self) -> Pessoa | None :
        return self.__passageiro
    def getCusto(self):
        return self.__custo
    

    def LeavePass(self):
        if self.getDrive() is None:
            print("fail: não tem motorista")
            return
        if self.getPass() is None:
            print("fail: não tem um passageiro")
            return
        
        passageiro = self.getPass()
        motorista = self.getDrive()
        custo = self.getCusto()

        if passageiro.getMoney() < custo:
            print("fail: Passenger does not have enough money")
            motorista.setMoney(motorista.getMoney()+custo)
            passageiro.setMoney(0)
            self.__custo = 0
            self.__passageiro = None
            print(f"{passageiro} left")
            
        else:
            passageiro.getMoney() >= custo
            motorista.setMoney(motorista.getMoney()+custo)
            passageiro.setMoney(passageiro.getMoney()-custo)
            self.__custo = 0
            self.__passageiro = None
            print(f"{passageiro} left")
        

    def __str__(self) -> str:
        passageiro = self.__passageiro if self.__passageiro != None else "None"
        motorista = self.__motorista if self.__motorista != None else "None"
        return f"Cost: {self.__custo}, Driver: {motorista}, Passenger: {passageiro}"
    

def main():
    moto = Moto()

    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setPass":
            nome = args[1]
            money = int(args[2])
            moto.setPass(Pessoa(nome, money))
        elif args[0] == "setDriver":
            nome = args[1]
            money = int(args[2])
            moto.setDrive(Pessoa(nome, money))
        elif args[0] == "drive":
            moto.setCusto(int(args[1]))
        elif args[0] == "leavePass":
            moto.LeavePass()
        

        

main()