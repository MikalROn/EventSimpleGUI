import PySimpleGUI as sg
from requests import get
from pysimpleevent import EventSimpleGUI


def get_cep_api(cep: str) -> dict:
    url = f'https://viacep.com.br/ws/{cep}/json/'
    r = get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise ValueError(r.status_code, r.text)


app = EventSimpleGUI()

lay = [
    [sg.Frame(
        'Encontre info pelo cep',
        [
            [sg.Text('Cep -> '), sg.Input(k='CEP')],
            [sg.Button('Buscar')]

        ]
  )],
    [
        sg.Frame('info', [], key='info')
    ]
]
win = sg.Window('Info cep', lay)

@app.event('Buscar')
def event_buscar(event, values, window: sg.Window):
    def cria_lay_com_dicio(dicionario: dict) -> list:
        return [
            [
            sg.Text(key, expand_x=True),
            sg.I(value, expand_x=True)
            ]
            for key, value in dicionario.items()
        ]

    Cep = values['CEP'].replace(' ', '')
    info: sg.Frame = window.find_element('info')


    dados = get_cep_api(Cep)
    for row in cria_lay_com_dicio(dados):
        window.extend_layout(info, [row])
    return Cep



if __name__ == '__main__':
    app.run_window(win, debug=True)