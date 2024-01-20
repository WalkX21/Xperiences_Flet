import flet as ft
#That's just a way to do it

def main(page: ft.Page):
    text = ft.Text(value = "what's up nigga", color="black")
    page.controls.append(text)
    page.update()

ft.app(target=main)