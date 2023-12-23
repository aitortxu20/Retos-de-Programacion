class ConversorEnteroRomano:
    def __init__(self,n):
        self.n = n

    def n_to_romano(self, n):
        diccionarioRomano = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,"IX": 9, "V": 5, "IV": 4, "I": 1}
        miles = int(n[-4])
        centenas = int(n[-3])
        decenas = int(n[-2])
        unidades = int(n[-1])



diccionarioRomano = {"MMM": 3000, "MM": 2000, "M": 1000, "CM": 900,"DCCC": 800,"DCC": 700, "DC": 600, "D": 500, "CD": 400, "CCC": 300, "CC": 200, "C": 100, "XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50, "XL": 40, "XXX": 30, "XX": 20, "X": 10,"IX": 9, "VIII": 8, "VII": 7, "VI": 6, "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1}
n="1975"
miles = int(n[-4]) * 1000
centenas = int(n[-3]) * 100
decenas = int(n[-2]) * 10
unidades = int(n[-1])
listan = [miles,centenas,decenas,unidades]
numeroromano = ""
for elemento in listan:
    for k, v in diccionarioRomano.items():
        if elemento == v:
            numeroromano += k


print(numeroromano)

class ConversorRomanoEntero:
    def __init__(self,n):
        self.n = n

    def romano_to_entero(self, n):
        pass

diccionariormanoarabe={"M":1000, "D":500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
entradaromao="MMMCMXCIX"
lista_valores = []
sumaromano = 0
for letra in entradaromao:
    lista_valores.append(diccionariormanoarabe[letra])

for i in range(len(lista_valores)-1):
    if lista_valores[i+1] > lista_valores[i]:
        lista_valores[i] = lista_valores[i] * -1

print(sum(lista_valores))

print(sumaromano)


print(lista_valores)
