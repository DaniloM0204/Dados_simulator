# Simulador de dado

import random 


class SimulatorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?"

    def Iniciar(self):
        self.eventos = input(self.mensagem)
        try:
            if self.eventos == 'S':
                self.GerarValorDoDado()
            elif self.eventos == 'N':
                print("Obrigado pela participaçao")
            else:
                print("Digite S ou N")
        except:
             print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randomint(self.valor_minimo,self.valor_maximo))

simulador = SimulatorDado
simulador.Iniciar()
