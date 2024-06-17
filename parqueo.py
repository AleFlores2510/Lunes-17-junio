from campo import Campo
from vehiculo import Vehiculo
class Parqueo:
    def __init__(self, cantidad_campos: int = 10) -> None:
        self.campos: list[Campo]=[]
        for i in range (1, cantidad_campos+1):
            self.campos.append(Campo(i))
    def hay_espacio(self)->bool:
        respuesta:bool = False

        for campo in self.campos:
            if campo.esta_vacio():
                respuesta = True
                break
        return respuesta
    
    def parquear(self,v:Vehiculo, hora:float)-> bool :
        respuesta:bool = False

        for campo in self.campos:
            if campo.esta_vacio():
                respuesta = campo.parquear(v, hora)
                break
        return respuesta