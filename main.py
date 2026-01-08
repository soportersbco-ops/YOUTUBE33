from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/descargar')
def descargar():
    video_url = request.args.get('url')
    
    # Configuración para convertir a MP3 directamente
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'descarga_rsb.mp3',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    return send_file('descarga_rsb.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run()
