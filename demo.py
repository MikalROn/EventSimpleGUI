import PySimpleGUI as sg
from pysimpleevent import EventSimpleGUI
import re


app = EventSimpleGUI()


@app.event('_NOME')
def verificar_nome(event, values, window):
    element = window.find_element('_NOME_ERRO')
    if len(values[event]) > 20:
        element.update('limite 20 exedido!')
    else:
        element.update('✔')


@app.event('_EMAIL')
def verifica_email(event: str, values, window: sg.Window):
    elememt = window.find_element('_EMAIL_ERRO')
    re_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(re_email, values[event]):
        elememt.update('✔')
    else:
        elememt.update('Email invalido')


@app.event('_SENHA')
def enviar_informacao(event, values, window):
    senha = values[event]
    element = window.find_element('_SENHA_ERRO')
    if 5 < len(senha) < 30:
        element.update('✔')
    else:
        element.update(f'Senha invalida {len( senha )}')






form = [

    [sg.Text('Nome'), sg.Push(), sg.Input('', k='_NOME', expand_x=True, enable_events=True), sg.T('', k='_NOME_ERRO')],

    [sg.Text('Email'), sg.Push(), sg.Input('', k='_EMAIL', expand_x=True, enable_events=True), sg.T('', k='_EMAIL_ERRO')],

    [sg.Text('Senha'), sg.Push(), sg.Input('', k='_SENHA', expand_x=True, enable_events=True, password_char="*"),  sg.T('', k='_SENHA_ERRO')],

    [sg.Button('Enviar', key='__ENVIAR', expand_x=True)]
]

layout = [
    [sg.Frame('Cadastro ->', form,expand_x=True, expand_y=True)],
]

window = sg.Window('Janela', layout, resizable=True, scaling=2)

if __name__ == '__main__':
    app.run_window(window)
