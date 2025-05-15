from random import randint as rn

class Personaje:
    def __init__(self, nombre, vida = int, ataque = int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        evasividad = rn(1, 20)
        if evasividad == 15:
            print(f"¡{self.nombre} ha atacado, pero ha fallado su ataque!")
        else:
            daño = rn(self.ataque -5, self.ataque +5)
            print(f"¡{self.nombre} ataca a {objetivo.nombre} y le causa {daño} de daño!")
            objetivo.recibir_daño(daño)

    def recibir_daño(self, daño = int):
        self.vida -= daño
        if self.vida <= 0:
            print(f"¡{self.nombre} ha sido derrotado!")
        else:
            print(f"¡{self.nombre} ha sido golpeado y tiene {self.vida} de vida restante!")

    def defenderse(self, daño = int, estado = bool):
        if estado == True:
            daño = daño/2
        else: 
            pass
        
class Guerrero(Personaje):
    def __init__(self, nombre, vida = 120 ,ataque = 25):
        super().__init__(nombre, vida, ataque)
    
    def atacar(self, objetivo):
        print(f"¡{self.nombre} le propina un tajo!")
        super().atacar(objetivo)

    def recibir_daño(self, daño):
        return super().recibir_daño(daño)
    
#    def defenderse(self, daño, estado=bool):
        print(f"¡{self.nombre} levanta su escudo y bloquea el ataque!")
        super().defenderse(daño, estado)

class Mago(Personaje):
    def __init__(self, nombre, vida = 75, ataque = 40):
        super().__init__(nombre, vida, ataque)
        
    def atacar(self, objetivo):    
        print(f"¡{self.nombre} lanza un hechizo congelante!")
        super().atacar(objetivo)

    def recibir_daño(self, daño):
        return super().recibir_daño(daño)
    
#    def defenderse(self, daño, estado=bool):
        print(f"¡{self.nombre} conjura una barrera protectora!")
        super().defenderse(daño, estado)

class Orco(Personaje):
    def __init__(self, nombre = "Orco", vida = 120, ataque = 30):
        super().__init__(nombre, vida, ataque)

    def atacar(self, objetivo):
        print(f"¡{self.nombre} blande su garrote desquiciadamente!")
        super().atacar(objetivo)

    def recibir_daño(self, daño):
        return super().recibir_daño(daño)
    
#    def defenderse(self, daño, estado=bool):
        print(f"¡{self.nombre} levanta una piedra bloquea el impacto!")
        super().defenderse(daño, estado)

class Litch(Personaje):
    def __init__(self, nombre = "Litch", vida = 60, ataque = 40):
        super().__init__(nombre, vida, ataque)

    def atacar(self, objetivo):
        print(f"¡{self.nombre} conjura una maldicion!☠️")
        super().atacar(objetivo)
    
    def recibir_daño(self, daño):
        return super().recibir_daño(daño)
    
#    def defenderse(self, daño, estado=bool):
        print(f"¡{self.nombre} usa a uno de sus esqueletos como escudo!")
        super().defenderse(daño, estado)

def iniciar_combate(jugador, enemigo):
    print(f"¡Combate de {jugador.nombre} vs {enemigo.nombre}")
    turno = 0

    while jugador.vida > 0 and enemigo.vida > 0:
        turno = turno +1
        print(f"Turno actual :{turno}")
#        rn(1,1)
        jugador.atacar(enemigo)
        if enemigo.vida > 0:
            enemigo.atacar(jugador)
#        if rn == 1:
#            estado = True
#            jugador.defenderse(estado) WIP
    if jugador.vida <= 0:
        print(f"Porfavor desinstalá")
    else:
        print(f"Has ganado por favor no jugues más 70 ⭐ de review")

#def menu(): WORK IN PROGRESS 
#    pass WIP

def main():
    print("Bienvenido a RPG promedio")

    nombre = input("Elige tu nombre    ")
    clase = input("Elige tu clase. Guerrero/Mago    ").lower()
    if clase == "guerrero":
        jugador = Guerrero(nombre)
    else:
        jugador = Mago(nombre)

    enemigo = rn(0, 1)
    if enemigo == 0:
        enemigo = Orco()
    else:
        enemigo = Litch()

    iniciar_combate(jugador, enemigo)

main()