import flet as ft
#aprecie demorei 1 trilhao de horas pra completar ficaria grato se voce apreciase
usuarios = {}
#CRIANDO A PAGINA
def main(page: ft.Page):
    page.title = "Blog do Akira"
    page.bgcolor = "orange"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.favicon = "icone.png"
#INFORMAÇOES TEXTOS E ETC
    status_text = ft.Text("", size=20, color="white", text_align=ft.TextAlign.CENTER)
    login_input = ft.TextField(label="Logim", width=200)
    senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=200)

    def mostrar_login():
        page.controls.clear()
        login_input.value = ""
        senha_input.value = ""
        status_text.value = ""
        page.add(login_form)
        page.update()

    def registrar(e):
        login = login_input.value.strip()
        senha = senha_input.value.strip()
        if not login or not senha:
            status_text.value = "Preencha login e senhs"
        elif login in usuarios:
            status_text.value = "Usuário já existe"
        else:
            usuarios[login] = senha
            status_text.value = "Usuário registrado com sucessp kkk"
        page.update()

    def entrar(e):
        login = login_input.value.strip()
        senha = senha_input.value.strip()
        if login in usuarios and usuarios[login] == senha:
            mostrar_blog()
        else:
            status_text.value = "Login ou senha incorretos!"
            page.update()

    login_form = ft.Column(
        controls=[
            ft.Text("    \nLogin / Registro\n(registre o usuarioo dps voce pode logar)", size=30, color="black", weight="bold"),
            login_input,
            senha_input,
            ft.Row(
                controls=[
                    ft.ElevatedButton("Registrar", on_click=registrar),
                    ft.ElevatedButton("Entrar", on_click=entrar)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            status_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(login_form)

    def mostrar_blog():
        page.controls.clear()
        info_extra = ft.Text("", size=20, color="black", text_align=ft.TextAlign.CENTER)

        def fatos(e):
            info_extra.value = (
                "Akira Toriyama nasceu em 5 de abril de 1955, em Nagoya, Japão. "
                "Antes de se tornar mangaká famoso, trabalhou como designer de roupas e ilustrador. "
                "Ele criou o mangá Dr. Slump em 1980 e Dragon Ball em 1984, que se tornaram sucessos mundiais. "
                "Toriyama é conhecido por seu estilo único que mistura humor e ação, e por desenhar muitos carros e máquinas. "
                "Seus trabalhos influenciaram vários mangakás modernos e muitos de seus personagens foram inspirados na mitologia chinesa. "
                "Apesar da fama, Toriyama é uma pessoa reservada e tímida, evitando entrevistas sempre que possível."
            )
            page.update()

        def mangas(e):
            info_extra.value = (
                "Principais mangás de Akira Toriyama:\n\n"
                "1. Dragon Ball (1984-1995)\n"
                "2. Dr. Slump (1980-1984)\n"
                "3. Cowa! (1997)\n"
                "4. Kajika (1998)\n"
                "5. Sand Land (2000)"
            )
            page.update()

        def jogos(e):
            info_extra.value = (
                "Akira Toriyama trabalhou no design de personagens de vários jogos famosos:\n\n"
                "- Dragon Quest I a XI\n- Chrono Trigger\n- Blue Dragon\n- V-Jump games e crossovers de Dragon Ball"
            )
            page.update()

        def vida_controv(e):
            info_extra.value = (
                "Vida pessoal e controvérsias:\n\n"
                "- Toriyama é reservado, raramente concede entrevistas.\n"
                "- Vive no Japão e mantém a vida pessoal longe dos holofotes.\n"
                "- Algumas polêmicas: atrasos em mangás ou capítulos curtos.\n"
                "- Muito respeitado pelos fãs."
            )
            page.update()

        botao_fatos = ft.ElevatedButton("Fatos", on_click=fatos)
        botao_mangas = ft.ElevatedButton("Mangás", on_click=mangas)
        botao_jogos = ft.ElevatedButton("Jogos", on_click=jogos)
        botao_vida = ft.ElevatedButton("Vida Pessoal / Controvérsias", on_click=vida_controv)
        botao_logout = ft.ElevatedButton("Sair", on_click=lambda e: mostrar_login())

        container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Olá, hoje falarei sobre Akira Toriyama!", size=30, color="blue", weight="bold"),
                    ft.Text(
                        "Akira foi criador de vários animes; o mais famoso deles foi Dragon Ball Z.",
                        size=25,
                        color="black",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Row(
                        controls=[botao_fatos, botao_mangas, botao_jogos, botao_vida],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    info_extra,
                    botao_logout
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=30,
            border_radius=20,
            bgcolor="#FF7802",
            alignment=ft.alignment.center
        )

        page.add(container)
        page.update()

ft.app(target = main)
#obrigado por tudo