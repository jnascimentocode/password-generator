from os import system
from tkinter.constants import CENTER
import PySimpleGUI as sg
import random

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
                break
            if event == 'Gerar Senha':
                new_pass = self.gerar_senha(values)
                print(f'Senha Gerada: {new_pass}')
                self.salvar_senha(new_pass, values)
                

    def gerar_senha(self, values):
        lista = 'ABCDEFGHIJKLMNOPQRSTUVXZabcdefghijklmnopqrstuvxz123456789!@#$&*'
        chars = random.choices(lista, k=int(values['char']))
        passwd = ''.join(chars)
        return passwd

    def salvar_senha(self, new_pass, values):
        with open('senhas.txt','a', newline='') as arquivo:
            arquivo.write(f'site: {values["site"]}, usuario: {values["usuario"]}, nova senha: {new_pass}')
        print('Senha salva no arquivo senhas.txt.')

tela = TelaSenha()
tela.Iniciar()



