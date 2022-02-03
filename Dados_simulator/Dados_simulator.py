# Simulador de dado

from _typeshed import Self
import random 
import PySimpleGUI

class SimulatorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        layout = [
               [sg.Text('Jogar o dado?')],
               [sg.Button('S'),sg.Button('N')]
        ]

    def Iniciar(self):

        # Criar uma janela
        self.janela = sg.Windoe("Simulador de Dado", Layout=layout)
        # Ler valores
        self.eventos, self.valores = janela.Read()
        # Fazer algo com valores
        while True:
            try:
                if self.eventos == 'S':
                    self.GerarValorDoDado()
                elif self.eventos == 'N':
                    print("Obrigado pela participação")
                else:
                    print("Digite S ou N")
            except:
                print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randomint(self.valor_minimo,self.valor_maximo))


simulador = SimulatorDado
simulador.Iniciar()
