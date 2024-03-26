import flet as ft


def main(page: ft.Page):

    def addCheckbox(e):
        strToAdd = txtIn.value
        txtIn.value = ""  # lo resetto a zero
        if strToAdd == "":
            return
        page.add(ft.Checkbox(label=strToAdd, value=False))

    # Row 1
    txtIn = ft.TextField(label="Aggiungi un elemento")  # il value glielo da l'utente
    btnAdd = ft.CupertinoButton(text="Add", on_click=addCheckbox)
    row1 = ft.Row([txtIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)


ft.app(target=main)
