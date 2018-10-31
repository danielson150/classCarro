class Carro:
    def __init__(self, nivel_combustivel, estado_inicial, velocidade_atual, velocidade_maxima, cambio):
        self.chassi = 14545646465
        self.marca = "Fiat"
        self.modelo = "Mobi"
        self.tipo_combustivel = "Gasolina"
        self.nivel_combustivel = nivel_combustivel
        self.estado_inicial = estado_inicial
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.cambio = cambio

    def Ligar(self):
        self.estado_inicial = "Ligado"
        print("A ignição do carro foi ligada")

    def Desligar(self):
        self.estado_inicial = "Desligado"
        print("A ignição do carro foi desligada")

    def Acelerar(self):
        print("Você pisou no acelerador!")
        self.velocidade_atual += 10

        if self.velocidade_atual>self.velocidade_maxima:
            print("Velocidade não permitida!")
            self.velocidade_atual = self.velocidade_maxima

    def Freiar(self):
        print("Você pisou no freio!")
        self.velocidade_atual -= 10

        if self.velocidade_atual<0:
            print("Carro se encontra parado!")
            self.velocidade_atual = 0

    def Trocar_Marcha(self, nova_marcha):
        self.cambio = nova_marcha

    def Abastecer(self, quantidade):
        self.nivel_combustivel += quantidade

    def Mostrar_Status(self):
        print("Marca: %s"%(self.marca))
        print("Chassi: %d"%(self.chassi))
        print("Modelo: %s"%(self.modelo))
        print("Estado inicial: ", self.estado_inicial)
        print("Nivel de combustivel: %d litros"%(self.nivel_combustivel))
        print("Velocidade atual: %d KM"%(self.velocidade_atual))
        print("Velocidade Maxima: %d KM "%(self.velocidade_maxima))
        print("Cambio do Carro: %d marcha"%(self.cambio))


def main():

    mobi = Carro(0, "Desligado", 10, 200, 1)

    while True:
        resp = int(input("Qual operação deseja executar:\n1-LIGAR\n2-DESLIGAR\n3-ACELERAR\n4-FREIAR\n5-TROCAR MARCHA\n6-ABASTECER\n7-MOSTRAR STATUS\n0-SAIR\n"))
        while (resp<0)or(resp>7):
            print("Opção Invalida. Digite novamente!")
            resp = int(input("Qual operação deseja executar:\n1-LIGAR\n2-DESLIGAR\n3-ACELERAR\n4-FREIAR\n5-TROCAR MARCHA\n6-ABASTECER\n7-MOSTRAR STATUS\n0-SAIR\n"))
        if resp == 1:
            mobi.Ligar()
        elif resp == 2:
            mobi.Desligar()
        elif resp == 3:
            mobi.Acelerar()
        elif resp == 4:
            mobi.Freiar()
        elif resp == 5:
            marcha = int(input("Qual marcha deseja colocar?"))
            mobi.Trocar_Marcha(marcha)
        elif resp == 6:
            mobi.Abastecer()
        elif resp == 7:
            mobi.Mostrar_Status()
        else:
            break


if __name__=='__main__':
    main()


