import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, FloatingActionButton, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption
from flet.controls import page
from flet.controls.border_radius import horizontal
from flet.controls.material.icons import Icons


class Maquiagem:
    def __init__(self, nome, marca, cor, tamanho, valor):
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.valor = valor


def main(page: flet.Page):
    page.title = "Exemplo de listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.CIRCLE),
                    title=item.nome,
                    subtitle=item.marca,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE,
                                          on_click=lambda _, maquiagem=item: ver_detalhes(maquiagem)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))
                        ],
                    ),
                ),
            )

    def ver_detalhes(maquiagem):
        text_nome.value = maquiagem.nome
        text_marca.value = maquiagem.marca
        text_cor.value = maquiagem.cor
        text_tamanho.value = maquiagem.tamanho
        text_valor.value = maquiagem.valor

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatório"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatório"

        if input_tamanho.value:
            input_tamanho.error = None
        else:
            tem_erro = True
            input_tamanho.error = "Campo obrigatório"

        if input_valor.value:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatório"

        if not tem_erro:
            maquiagem = Maquiagem(
                nome=input_nome.value,
                marca=input_marca.value,
                cor=input_cor.value,
                tamanho=input_tamanho.value,
                valor=input_valor.value,
            )

            lista_dados.append(maquiagem)

            input_nome.value = ""
            input_marca.value = ""
            input_cor.value = ""
            input_tamanho.value = ""
            input_valor.value = ""

        montar_lista_padrao()

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    AppBar(
                        title="Maquiagens",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_marca,
                        input_cor,
                        input_tamanho,
                        input_valor,
                        btn_salvar
                    ]
                )
            )

        elif page.route == "/form_detalhes":
            page.views.append(
                View(
                    route="/form_detalhes",
                    controls=[
                        AppBar(
                            title="Detalhes",
                        ),
                        text_nome,
                        text_marca,
                        text_cor,
                        text_tamanho,
                        text_valor,
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="Nome", hint_text="Digite o nome")
    input_marca = TextField(label="Tipo", hint_text="EX: Dior")
    input_cor = Dropdown(
        label="Cor",
        editable=True,
        options=[
            DropdownOption("Preto"),
            DropdownOption("Laranja"),
            DropdownOption("Rosa"),
            DropdownOption("Vermelho"),
            DropdownOption("Outro(a)"),
        ],
        width=400,
    )
    input_tamanho = TextField(label="Tamanho", hint_text="EX: Grande")
    input_valor = TextField(label="Valor", hint_text="EX: 5000")

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    text_nome = Text()
    text_marca = Text()
    text_cor = Text()
    text_tamanho = Text()
    text_valor = Text()

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
