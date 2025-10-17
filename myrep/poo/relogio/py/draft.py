class Relogio:
    def __init__(self):
        self.__hora = 0
        self.__mins = 0
        self.__segs = 0
    
    def get_hora(self):
        return self.__hora
    def get_mins(self):
        return self.__mins
    def get_segs(self):
        return self.__segs

    def __str__(self) -> str:
        return f"{self.get_hora():02}:{self.get_mins():02}:{self.get_segs():02}"
    
    def set_hora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def set_mins(self, mins: int):
        if mins < 0 or mins > 59:
            print("fail: minuto invalido")
            return
        self.__mins = mins
    
    def set_segs(self, segs: int):
        if segs < 0 or segs > 59:
            print("fail: segundo invalido")
            return
        self.__segs = segs

    def cont_hora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            self.__hora = 0   
            return
        self.__hora = hora

    def cont_mins(self, mins: int):
        if mins < 0 or mins > 59:
            print("fail: minuto invalido")
            self.__mins = 0
            return
        self.__mins = mins
        
    def cont_segs(self, segs: int):
        if segs < 0 or segs > 59:
            print("fail: segundo invalido")
            self.__segs = 0
            return
        self.__segs = segs

    def NextSecond(self):
        if self.get_segs() == 59:
            self.set_segs(0)
            if self.get_mins() == 59:
                self.set_mins(0)
                if self.get_hora() == 23:
                    self.set_hora(0)
                else:
                    self.set_hora(self.get_hora() + 1)
            else:
                self.set_mins(self.get_mins() + 1)
        else:
            self.set_segs(self.get_segs() + 1)
        
def main():
    relogio: Relogio = Relogio()
    while True:
        line: str = input()
        print("$"+ line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(relogio)
        if args[0] == "set":
            args[1] = relogio.set_hora(int(args[1]))
            args[2] = relogio.set_mins(int(args[2]))
            args[3] = relogio.set_segs(int(args[3]))
        if args[0] == "init":
            args[1] = relogio.cont_hora(int(args[1]))
            args[2] = relogio.cont_mins(int(args[2]))
            args[3] = relogio.cont_segs(int(args[3]))
        if args[0] == "next":
            relogio.NextSecond()
    
main()