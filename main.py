import time

import flet as ft


def main(page: ft.Page):  # page è un oggetto che contiene gli elementi grafici

    txtIn = ft.Text(value="Hello world!")  # gli oggetti che vengono aggiunti hanno un value che rappresenta il
    # contenuto, ci sono altri campi che modificano gli aspetti grafici
    page.controls.append(txtIn)  # aggiungo l'oggetto alla pagina
    page.update()  # aggiorno la pagina
# si può aggiornare la pagina in un altro momento

    txtOut = ft.Text(value="Counter", color="red", size=24)
    page.add(txtOut)  # è un istruzione che fa sia append che update!

    # for i in range(1, 100):
    #     txtOut.value = "Counter: " + str(i)
    #     txtOut.update()
    #     time.sleep(1)

# STRUTTURA:
    def handleButton(e):  # la funzione del button ha un oggetto event che si crea al click
        txtOut.value = ""  # pulisco il valore di txtOut
        time.sleep(1)
        txtOut.value = "Pulsante cliccato!"  # lo aggiorno
        page.update()  # ogni metodo che modifica la grafica deve fare update

    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleButton)  # il bottone ha testo e funzione per il click
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=24)
    page.add(row1, txtOut)

# usa la documentazione sul sito di flet!!!


ft.app(target=main, view=ft.AppView.FLET_APP)
# sintassi di flet dove alla fine del programma io "lancio la visualizzazione"
# flat istanzia l'applicazione in una finestra del pc, posso cambiare questa cosa con view
# view è tutto il quaderno che contiene pages

# MVG
'''
Multi view graph, è una logica di programmazione che rispetta dei pattern di design
per la sicurezza e l'accessibilità del codice

il codice viene diviso in tre classi: View (che implementa tutte le funzionalità
delle interfacce grafiche), Model (gestisce tutti i dati e le funzioni dell'app),
Controller (fa da tramite e conosce lo stato dell'interfaccia grafica, quando cambia
comunica con il model per cambiare lo stato dei dati)
'''
