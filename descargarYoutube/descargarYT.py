#!/bin/python3
import os
import yt_dlp
import argparse

def descargarAudioYVideo(link, directorio):
    try:
        ydl_opts = {
            'outtmpl': f'{directorio}/%(title)s.%(ext)s',
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  
            'merge_output_format': 'mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Hecho")

    except Exception as e:
        print(f"Error: {e}")

def descargarAudio(link, directorio):
    try:
        ydl_opts = {
            'outtmpl': f'{directorio}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
            
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print('Hecho')

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Otro script del admin para descargar vídeos y audios de Youtube. Mel no estuvo aquí.")
    parser.add_argument("--audio", action="store_true", help="Descarga el audio de un vídeo de Youtube.")
    parser.add_argument("--video", action="store_true", help = "Descarga el audio y vídeo de un vídeo de Youtube en máxima calidad.")

    args = parser.parse_args()

    if not args.audio and not args.video:
        parser.print_help()
        return

    directorioActual = os.getcwd()
    link = input("Link: ")
    if args.video:
        descargarAudioYVideo(link, directorioActual)
    if args.audio:
        descargarAudio(link, directorioActual)

if __name__ == "__main__":
    main()
