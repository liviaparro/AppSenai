import asyncio
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, Row


def main(page: flet.Page):
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700


    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def salvar_dados():
        text_tipo.value = input_tipo.value
        text_marca.value = input_marca.value
        text_cor.value = input_cor.value
        text_valor.value = input_valor.value

        tem_erro = False

        if input_tipo.value:
            input_tipo.error = None
        else:
            tem_erro = True
            input_tipo.error = "Campo obrigatório"

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

        if input_valor.value:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatório"

        if not tem_erro:
            input_tipo.value = ""
            input_marca.value = ""
            input_cor.value = ""
            input_valor.value = ""
            navegar("/segunda_tela")

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Maquiagem",
                        bgcolor=Colors.PINK_100
                    ),
                    Text("Digite o tipo :"),
                    input_tipo,

                    Text("Marca do cosmético :"),
                    input_marca,

                    Text("Cor do objeto :"),
                    input_cor,

                    Text("Valor do produto :"),
                    input_valor,
                    OutlinedButton("Salvar", on_click=salvar_dados)
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="Maquiagem",
                            bgcolor=Colors.PINK_100
                        ),
                        Row([text_label_tipo, text_tipo]),
                        Row([text_label_marca, text_marca]),
                        Row([text_label_cor, text_cor]),
                        Row([text_label_valor, text_valor]),
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
    text = Text()
    input_tipo = TextField(label="Nome do produto")
    input_marca = TextField(label="Marca")
    input_cor = TextField(label="Cor")
    input_valor = TextField(label="Valor")

    text_tipo = Text()
    text_label_tipo = Text("Tipo: ", weight=FontWeight.BOLD)
    text_marca = Text()
    text_label_marca = Text("Marca: ", weight=FontWeight.BOLD)
    text_cor = Text()
    text_label_cor = Text("Cor: ", weight=FontWeight.BOLD)
    text_valor = Text()
    text_label_valor = Text("Valor: ", weight=FontWeight.BOLD)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
