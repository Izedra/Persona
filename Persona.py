import random

class Persona:
    def __init__(self, nombre="", edad=0, dni="", sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return "Nombre: " + str(self.nombre) + ", Edad: " + str(self.edad) + ", DNI: " + str(self.dni) + ", Sexo: " + str(self.sexo) + ", Peso: " + str(self.peso) + ", Altura(cm): " + str(self.altura)

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 0:
            print(-1)
        elif imc == 0:
            print(0)
        else:
            print(1)

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def introducirSexo(self, sexo):
        if sexo != 'M' or sexo != 'H':
            self.sexo = 'M'
        else:
            self.sexo = sexo

    def generaDNI(self):
        numero = random.randrange(10000000, 99999999)
        dniChars = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        letra = dniChars[numero % 23]
        self.dni = repr(numero) + letra