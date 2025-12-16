
import flet as ft
import subprocess
import os

def main(page: ft.Page):

    page.title = "Compilador C++ com Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    arquivo_input = ft.TextField(label="Caminho do arquivo C++", width=400)
    saida_input = ft.TextField(label="Nome do executável (padrão: programa)", width=400)
    output_area = ft.Text(value="", selectable=True)
    
    def compilar_click(e):
        caminho = arquivo_input.value.strip()
        saida = saida_input.value.strip() or "programa"

        if not os.path.isfile(caminho):
            output_area.value = f"Arquivo não encontrado: {caminho}"
            page.update()
            return

        comando = ["g++", caminho, "-o", saida]
        try:
            resultado = subprocess.run(comando, capture_output=True, text=True)
            if resultado.returncode == 0:
                output_area.value = f"Compilação concluída!\nExecutável: {saida}"
            else:
                output_area.value = f"Erro na compilação:\n{resultado.stderr}"
        except FileNotFoundError:
            output_area.value = "g++ não encontrado. Instale o compilador e tente novamente."
        
        page.update()

    def rodar_click(e):
        executavel = saida_input.value.strip() or "programa"
        if not os.path.isfile(executavel):
            output_area.value = f"Executável não encontrado: {executavel}"
        else:
            try:
                if os.name == "nt":
                    subprocess.run([f"{executavel}.exe"])
                else:
                    subprocess.run([f"./{executavel}"])
            except Exception as ex:
                output_area.value = f"Erro ao executar: {ex}"
        page.update()

    compilar_btn = ft.ElevatedButton("Compilar", on_click=compilar_click)
    rodar_btn = ft.ElevatedButton("Rodar", on_click=rodar_click)

    page.add(
        arquivo_input,
        saida_input,
        ft.Row([compilar_btn, rodar_btn], spacing=10),
        output_area
    )

ft.app(target=main)
