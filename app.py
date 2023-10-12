from flask import Flask, render_template, request, send_file, redirect, url_for, jsonify
import os
import pytube
from moviepy.editor import *
from spleeter.separator import Separator
import multiprocessing
import sys
import shutil

if sys.platform.startswith('darwin'):
    multiprocessing.set_start_method('fork', force=True)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads/")
STEMS_FOLDER = os.path.join(BASE_DIR, "stems/")
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["STEMS_FOLDER"] = STEMS_FOLDER

separator = Separator('spleeter:5stems-16kHz')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        yt_link = request.form['yt_link']
        yt = pytube.YouTube(yt_link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(output_path=DOWNLOAD_FOLDER)
        video_path = os.path.join(DOWNLOAD_FOLDER, video.default_filename)
        mp3_path = video_path.replace(".mp4", ".mp3")

        with VideoFileClip(video_path) as clip:
            clip.audio.write_audiofile(mp3_path)

        separator.separate_to_file(mp3_path, STEMS_FOLDER)
        stem_folder_path = os.path.join(STEMS_FOLDER, os.path.basename(mp3_path).replace('.mp3', ''))
        return jsonify({"status": "success", "foldername": os.path.basename(stem_folder_path)})

    return render_template('index.html')

@app.route('/downloads/<foldername>/')
def download_folder(foldername):
    stem_folder_path = os.path.join(STEMS_FOLDER, foldername)

    if not os.path.exists(f"{stem_folder_path}.zip"):
        try:
            shutil.make_archive(stem_folder_path, 'zip', stem_folder_path)
        except Exception as e:
            return f"Error while creating the archive: {e}"

    if not os.path.exists(f"{stem_folder_path}.zip"):
        return "Zip file wasn't created or isn't accessible!"

    response = send_file(f"{stem_folder_path}.zip", as_attachment=True)
    os.remove(f"{stem_folder_path}.zip")
    shutil.rmtree(stem_folder_path)
    mp3_path = os.path.join(DOWNLOAD_FOLDER, foldername + ".mp3")
    if os.path.exists(mp3_path):
        os.remove(mp3_path)
    video_path = mp3_path.replace(".mp3", ".mp4")
    if os.path.exists(video_path):
        os.remove(video_path)

    return response

if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    if not os.path.exists(STEMS_FOLDER):
        os.makedirs(STEMS_FOLDER)
    app.run(debug=True)
