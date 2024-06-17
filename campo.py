from typing import Optional
from vehiculo import Vehiculo

class Campo:
    def __init__(self,id:int) -> None:
        self.id:int = id
        self.vehiculo:Optional[Vehiculo] = None
        self.hora_ingreso:Optional[float] = None

    def esta_vacio(self)->bool:
        return self.vehiculo is None
    
    def parquear(self,v:Vehiculo, hora:float)->bool:
        if self.esta_vacio ():
            self.vehiculo = v
            self.hora:ingreso = hora
            return True
        else:
            return false