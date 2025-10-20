class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def get_capacidade(self):
        return self.__capacidade
    def get_carga(self):
        return self.__carga
    def set_carga(self, carga: int):
        self.__carga = carga


    def mostrar(self):
        print(f"{self.get_carga()}/{self.get_capacidade()}")
    
        

class Notebook:
    def __init__(self):
        self.__ligado : bool = False
        self.__bateria: Bateria | None = None

    def get_ligado(self):
        return self.__ligado
    def set_ligado(self, status: bool):
        self.__ligado = status
    def get_bateria(self):
        return self.__bateria
    def set_bateria(self, bateria: Bateria):
        self.__bateria = bateria

    def remover(self):
        self.__bateria = None



    def mostrar(self):
        if self.get_bateria == None:
            print (f"status: desligado, bateria: (nenhuma)")
        """
        if self.get_ligado() == False:
            print (f"status: desligado, bateria: ({bateria.get_carga()}/{bateria.get_capacidade()})")
            return
        if self.get_ligado() == True:
            print (f"status: ligado, bateria: ({bateria.get_carga()}/{bateria.get_capacidade()})")
            return
        """
    def ligar(self):
        if self.get_ligado() == True:
            print("notebook já está ligado")
            return
        if self.get_bateria() == None:
            print("fail: notebook sem bateria")
            return
        self.set_ligado(True)
        print("o notebook foi ligado")

    def desligar(self):
        if self.get_ligado() == False:
            print("o notebook já está desligado")
            return
        self.set_ligado(False)
        print("o notebook foi desligado")

    def usar(self, tempo: int):
        if self.get_ligado() == False:
            print("você precisa ligar o notebook primeiro")
            return
        if tempo > bateria.get_carga():
            print(f"bateria descarregou, você usou até {bateria.get_carga()} minutos")
            bateria.set_carga(0)
            return
        bateria.set_carga((bateria.get_carga()) - tempo)
        print(f"você usou o notebook por {tempo} minutos")
        

notebook = Notebook()
bateria = Bateria(50)
notebook.mostrar()
print(notebook.get_bateria())
