from datetime import datetime

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton, \
    TextButton


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT # ou ThemeMode.Light
    page.window.widht = 400
    page.window.height = 700


    # Funções

    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"

    def verificar_parimpar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_parimpar.value = f"O {numero} é par"
        else:
            text_parimpar.value = f"O {numero} é impar"

    def calcular_idade():
        ano_nascimento = int(input_data_nascimento.value)
        idade = datetime.now().year - ano_nascimento

        if idade >= 18:
            text_idade.value = f'Você tem {idade} anos e é maior de idade'
        else:
            text_idade.value = f'Você tem {idade} anos e é menor de idade'

    # Componentes
    text = Text()
    text_parimpar = Text()
    text_idade = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Digite um numero")
    input_data_nascimento = TextField(label="Digite o ano de nascimento")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = ElevatedButton("Verificar", on_click=verificar_parimpar)
    btn_calcular = TextButton("Calcular idade", on_click=calcular_idade)



    # Construção da tela

    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text,
                input_numero,
                btn_verificar,
                text_parimpar,
                input_data_nascimento,
                btn_calcular,
                text_idade

            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )




flet.run(main)