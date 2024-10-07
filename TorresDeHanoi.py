class Pila:
    def __init__(self, nombre):
        self.discos = []
        self.nombre = nombre  

    def poner_disco(self, disco):
        self.discos.append(disco)

    def quitar_disco(self):
        if len(self.discos) != 0:
            return self.discos.pop()
        else:
            return None

    def tope(self):
        if len(self.discos) != 0:
            return self.discos[-1]
        else:
            return None

    def __str__(self):
        return self.nombre  

def movimiento(n, origen, auxiliar, destino, movimientos):
    if  n== 1:
        disco = origen.quitar_disco()
        destino.poner_disco(disco)
        movimientos.append(f"Mover disco {disco} de {origen} a {destino}")
    else:
        movimiento(n - 1, origen, destino, auxiliar, movimientos)
        disco = origen.quitar_disco()
        destino.poner_disco(disco)
        movimientos.append(f"Mover disco {disco} de {origen} a {destino}")
        movimiento(n - 1, auxiliar, origen, destino, movimientos)


def resultado(n):
    movimientos = []
    torreA = Pila("A")  
    torreB = Pila("B")
    torreC = Pila("C")

    for i in range(n, 0, -1):
        torreA.poner_disco(i)

    movimiento(n, torreA, torreB, torreC, movimientos)
    return movimientos


discos = 3
respuesta = resultado(discos)

for mover in respuesta:
    print(mover)

    



        
