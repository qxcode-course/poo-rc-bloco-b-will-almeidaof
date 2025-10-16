class Camisa:
    def __init__(self):
        self.__size: str = ""

    def get_camisa(self):
        return self.__size

    def set_camisa(self, valor: str) -> None:
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Tamanho inválido")
            return
        self.__size = valor

camisa: Camisa = Camisa()

while camisa.get_camisa() == "":
    print("Digite o seu tamanho de roupa")
    tamanho = input()
    camisa.set_camisa(tamanho)

print("Parabens, você comprou uma roupa tamanho", camisa.get_camisa())