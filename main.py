import flet as ft
import threading
import os

def main(page: ft.Page):
    page.title = "Assistente Baixar Video"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

    link_input = ft.TextField(
        label="Cole o link do YouTube ou Kwai",
        width=350,
    )
    status = ft.Text(
        "Pronto para baixar...",
        size=16,
    )

    def baixar(e):
        link = link_input.value.strip() if link_input.value else ""
        if not link:
            status.value = "Cole um link primeiro!"
            page.update()
            return
        status.value = "Baixando... aguarde..."
        page.update()
        threading.Thread(target=fazer_download, args=(link,), daemon=True).start()

    def fazer_download(link):
        try:
            import yt_dlp
            pasta = "/storage/emulated/0/Download/AssistenteVideos"
            os.makedirs(pasta, exist_ok=True)
            opcoes = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(opcoes) as ydl:
                ydl.download([link])
            status.value = "Baixado! Pasta Download/AssistenteVideos"
        except Exception as ex:
            status.value = f"Erro: {str(ex)[:100]}"
        page.update()

    def falar(e):
        status.value = "Fale: baixar video + cole o link e clique em BAIXAR"
        page.update()

    page.add(
        ft.Text("ASSISTENTE DE DOWNLOAD", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
        ft.Text("Fale ou cole o link", size=16, text_align=ft.TextAlign.CENTER),
        link_input,
        ft.ElevatedButton("BAIXAR VIDEO", on_click=baixar, width=350, bgcolor="green", color="white"),
        ft.ElevatedButton("FALAR COMANDO", on_click=falar, width=350, bgcolor="blue", color="white"),
        status,
    )

ft.app(target=main)