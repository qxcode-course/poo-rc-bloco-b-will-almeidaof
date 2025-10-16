class Camisa:
    def __init__(self):
        self.__size: str = ""

    def get_camisa(self):
        return self.__size

    def set_camisa(self, valor: str) -> None:
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__size = valor


def main():
    camisa: Camisa = Camisa()
    while True:
        line: str = input()
        print("$"+line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({camisa.get_camisa()})")
        elif args[0] == "size":
            args[1] = camisa.set_camisa(args[1])
        
        
main()

