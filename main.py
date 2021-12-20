from os import system
from tkinter.constants import CENTER
import PySimpleGUI as sg
from random import choice

class TelaSenha:

    def __init__(self):
        sg.theme('Reds')

        layout = [
            [sg.Text('Site/App:', size=(15,1)), sg.Input(key='site', size=(30,1))],
            [sg.Text('E-mail/Usuário:',size=(15,1)), sg.Input(key='usuario', size=(30,1))],
            [sg.Text('Qtde de caracteres:', size=(15,1)), sg.Combo(values=list(range(1,30)),key='char', default_value=1,size=(3,0))],
            [sg.Output(size=(46,5))],
            [sg.Button('Gerar Senha', size=(42,1) )],
        ] 

        self.janela = sg.Window('Gerador de Senha', layout)

    def Iniciar(self):

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED:
                system('cls')
                break

    def gerar_senha(self):
        pass

    def salvar_senha(self):
        pass

tela = TelaSenha()
tela.Iniciar()


