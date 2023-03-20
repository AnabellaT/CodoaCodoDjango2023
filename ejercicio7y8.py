"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI

    @property
    def nombre(self):
        return self.nombre        
    @property
    def edad(self):
        return self.edad
    @property
    def DNI(self):
        return self.DNI
    
    @nombre.setter
    def nombre(self, nuevo):
        self.nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.nombre) 
    
    @edad.setter
    def edad(self, nuevo):
        self.edad = nuevo
        print ("La edad se ha modificado por")
        print (self.edad)

    @DNI.setter
    def DNI(self, nuevo):
        self.DNI = nuevo
        print ("El DNI se ha modificado por")
        print (self.DNI)

    def mostrar(self):
        print(f'Nombre:{self.nombre}, Edad:{self.edad}, DNI:{self.DNI}')

    def mayor_edad(self):
        if int(self.edad)>18:
            print("La persona es mayor de edad")
#Crea una clase llamada Cuenta que tendrá los siguientes atributos:
#titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
#Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.  
#Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
#mostrar(): Muestra los datos de la cuenta.  
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular,cantidad):
        self.titular=titular
        self.cantidad=float(cantidad)
        class titular(Persona):
            def __init__(self,nombre,edad,DNI):
                Persona().__init__(nombre, edad, DNI)
            
    def mostrar(self):
        print(f'Titular:{self.titular},Saldo:{self.cantidad}')
    
    def ingresar(self,cantidadIngresada):
        if cantidadIngresada > 0:
          self.cantidad=cantidadIngresada+self.cantidad

    def retirar(self,cantidadRetirada):
        self.cantidad=self.cantidad-cantidadRetirada

#definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. 
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase:  Un constructor.  Los setters y getters para el nuevo atributo.  
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
class CuentaJoven(Cuenta):
    
    def __init__(self,titular,cantidad,bonificación):
        Cuenta().__init__(titular,cantidad)
        self.titular=titular
        self.cantidad=cantidad
        self.bonificación=float(bonificación)

    def es_titular_válido(edad):
        if edad>18 and edad<25:
            True
        else:
            False
        
    def retirar(cantidadRetirada):
        if CuentaJoven.es_titular_válido():
            cantidad=cantidad-cantidadRetirada

    def mostrar(self):
        print(f'Cuenta Joven,{self.bonificación}%')
              

juan=Persona("Juan",20,3333333)
"""print(juan.edad)
print(juan.nombre)
print(juan.DNI)
juan.mostrar()
juan.mayor_edad()"""

N18520=CuentaJoven(["Pedro",35,185722],10)
"""N18520.mostrar()"""
N18520.ingresar(30)
N18520.retirar(5)
N18520.mostrar()



        

