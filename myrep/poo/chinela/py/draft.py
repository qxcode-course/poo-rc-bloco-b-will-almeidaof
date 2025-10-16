class Chinela:
    def __init__(self):
        self.__size = 0

    def Get_Size(self) -> int:
        return self.__size

    def Set_Size(self, valor: int):
        if valor < 20 or valor > 50 and valor %2 != 0:
            print("fail: tamanho inválido")
            return
        self.__size = valor

chinela: Chinela = Chinela()

while chinela.Get_Size() == 0:
    print("DIGITE O TAMANHO DE SUA CHINELA")
    tamanho = int(input())
    chinela.Set_Size(tamanho)


print("Parabens, você comprou uma chinela tamanho", chinela.Get_Size())