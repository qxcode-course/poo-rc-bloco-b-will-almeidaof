class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size: int = size

    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        else:
            return 0 


    def get_thickness(self):
        return self.__thickness

    def get_hardness(self):
        return self.__hardness
    def set_size(self, tamanho: int):
        self.__size = tamanho
    def get_size(self):
        return self.__size


    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

    
class Pencil:
    def __init__(self):
        self.__thickness: float = 0
        self.__tip: Lead | None = None

    def set_thickness(self, espessura: float):
        self.__thickness = espessura



    def get_tip(self):
        return self.__tip

    def inserir(self, grafite: Lead):
        if self.__tip != None:
            print("fail: ja existe grafite")
            return

        if grafite.get_thickness() != self.__thickness:
            print("fail: calibre incompativel")
            return
        self.__tip = grafite

    def remover(self) -> Lead | None:
        aux = self.__tip
        self.__tip = None
        return aux


    def writePage(self):
        if self.__tip is None:
            print("fail: nao existe grafite")
            return

        size = self.__tip.get_size()
        cost = self.__tip.usagePerSheet()
        resultado = size - cost

        if size <= 10:
            print("fail: tamanho insuficiente")
            return
        
        if resultado <10:
            print("fail: folha incompleta")
            self.__tip.set_size(10)
            return

        self.__tip.set_size(resultado)




    def __str__(self) -> str:
        grafite = self.__tip if self.__tip != None else "null"
        return f"calibre: {self.__thickness}, grafite: {grafite}"
    


def main():
    pencil = Pencil()
    while True:
        line = input()
        print("$"+line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "insert":
            thickness = args[1]
            hardness = args [2]
            size = args[3]
            lead = Lead(float(thickness), hardness, int(size))
            pencil.inserir(lead)
        elif args[0] == "init":
            pencil.set_thickness(float(args[1]))
        elif args[0] == "remove":
            pencil.remover()
        elif args[0] == "write":
            pencil.writePage()
main()