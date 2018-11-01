class Carro:
    chassi = ""
    marca = ""
    modelo = ""
    tipo_combustivel = ""
    nivel_combustivel = ""
    estado_inicial = ""
    velocidade_atual = ""
    velocidade_maxima = ""
    capacidade_tanque = "" 
    cambio = ""
    def __init__(self, chassi, marca, modelo, tipo_combustivel, nivel_combustivel, estado_inicial, velocidade_atual, velocidade_maxima, cambio, capacidade_tanque):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.tipo_combustivel = tipo_combustivel
        self.nivel_combustivel = nivel_combustivel
        self.estado_inicial = estado_inicial
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.capacidade_tanque = capacidade_tanque 
        self.cambio = cambio

    def Ligar(self):
        if self.estado_inicial == "Ligado":
            print("O carro já está ligado")
        else:
            self.estado_inicial = "Ligado"
            print("A ignição do carro foi ligada")

    def Desligar(self):
        if self.estado_inicial == "Desligado":
            print("O carro já está desligado")
        else:    
            self.estado_inicial = "Desligado"
            print("A ignição do carro foi desligada")

    def Acelerar(self):
        if(self.estado_inicial == "Ligado")and(self.nivel_combustivel>0):
            print("Você pisou no acelerador!")
            self.velocidade_atual += 10

            if self.velocidade_atual>self.velocidade_maxima:
                print("Velocidade não permitida!")
                self.velocidade_atual = self.velocidade_maxima
        else:
            print("O carro deve está LIGADO e ABASTECIDO para ACELERAR")
            print("Estado: ", self.estado_inicial)
            print("Nível do Combustivel: ", self.nivel_combustivel)

    def Freiar(self):
        if self.velocidade_atual == 0:
            print("Carro se encontra parado!")
            self.velocidade_atual = 0
        else:
             print("Você pisou no freio!")   
             self.velocidade_atual -= 10

    def Trocar_Marcha(self, nova_marcha):
        if(nova_marcha<0)or(nova_marcha>5):
            print("Marcha inválida. Operação não foi concluida!")
        else:
            self.cambio = nova_marcha

    def Abastecer(self, quantidade):
        
        self.nivel_combustivel += quantidade
        
        if(quantidade>self.capacidade_tanque):
            print("Quantidade maior que a capacidade do tanque")
            self.nivel_combustivel = self.nivel_combustivel - quantidade
            print("Capacidade Máxima: %s litros"%(self.capacidade_tanque))
            
        if(self.nivel_combustivel>self.capacidade_tanque):
            print("O tanque está cheio!")
            self.nivel_combustivel = self.nivel_combustivel - quantidade
            print("Nível do combustivel: %s litros"%(self.nivel_combustivel))


    def Mostrar_Status(self):
        print("Marca: %s"%(self.marca))
        print("Chassi: %d"%(self.chassi))
        print("Modelo: %s"%(self.modelo))
        print("Tipo de Combustivel: %s"%(self.tipo_combustivel))
        print("Estado inicial: ", self.estado_inicial)
        print("Nivel de combustivel: %d litros"%(self.nivel_combustivel))
        print("Velocidade atual: %d KM"%(self.velocidade_atual))
        print("Velocidade Maxima: %d KM "%(self.velocidade_maxima))
        print("Cambio do Carro: %d marcha"%(self.cambio))


def main():

    mobi = Carro(51660125158, "Fiat", "Mobi", "Gasolina", 0, "Desligado", 0, 200, 1, 50)


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
            quantidade = int(input("Qual a quantidade de litros para abastecimento?"))
            mobi.Abastecer(quantidade)
        elif resp == 7:
            mobi.Mostrar_Status()
        else:
            break


if __name__=='__main__':
    main()
