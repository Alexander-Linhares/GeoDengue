import os
import pandas as pd
import flet as ft 


def main(page: ft.Page):
    page.title = "File picker"

    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e)
    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    "Selecionar arquivo",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        dialog_title="Selecione uma planilha do excel da dengue ",
                        allowed_extensions=["xlsx"],
                        allow_multiple=True
                    )
                )
            ]
        )
    )

if __name__ == "__main__":
    print("Olá mundo!")
    ft.app(target=main)