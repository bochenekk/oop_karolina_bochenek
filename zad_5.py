class Tamagotchi:
    prog_nudy = 5 # A
    prog_glodu = 10 # A

    def __init__(self, imie): # B, E || self, imie - C
        self.imie = imie
        self.slowa = ["Mmmmrrp", "Hrrp"]
        self.poziom_nudy = 0


burek = Tamagotchi("Burek") # D

