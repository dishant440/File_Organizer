import os
import shutil
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

pdf_files = []
docx_files = []
video_files = []
image_files = []
xlsx_files = []
audio_files = []
exe_files = []
zip_files = []
other_files = []

parent_dir = downloads_path + "/"

document = "Document FILES"
pdf = "PDF FILES"
images = "IMAGES FILES"
videos = "VIDEOS FILES"
audio = "AUDIO FILES"
xlsx = "XLSX FILES"
exe = "EXECUTABLE FILES"
zip_ = "ZIP FILES"
other = "OTHER FILES"


def move_to_destination_directory(file_type, arr, parent_directory=parent_dir):
    path = os.path.join(parent_directory, file_type)
    if not os.path.exists(path):
        os.mkdir(path)
    source = parent_directory
    destination = path

    for files in arr:
        source_path = os.path.join(source, files)
        destination_path = os.path.join(destination, files)
        try:
            shutil.move(source_path, destination_path)
        except Exception as e:
            print("Error moving file:", e)


for dir_content in os.listdir(parent_dir):
    if os.path.isfile(os.path.join(parent_dir, dir_content)):  # Check if it's a file
        if dir_content.endswith(".pdf"):
            pdf_files.append(dir_content)

        elif dir_content.endswith(".docx"):
            docx_files.append(dir_content)

        elif dir_content.endswith(".xlsx"):
            xlsx_files.append(dir_content)

        elif dir_content.endswith((".mp4", ".mkv")):
            video_files.append(dir_content)

        elif dir_content.endswith((".png", ".jpg", ".jpeg", ".gif", ".JPG")):
            image_files.append(dir_content)

        elif dir_content.endswith((".mp3", ".")):
            audio_files.append(dir_content)

        elif dir_content.endswith(".exe"):
            exe_files.append(dir_content)

        elif dir_content.endswith(".zip"):
            zip_files.append(dir_content)

        else:
            other_files.append(dir_content)

if len(docx_files) != 0:
    move_to_destination_directory(document, docx_files)

if len(pdf_files) != 0:
    move_to_destination_directory(pdf, pdf_files)

if len(image_files) != 0:
    move_to_destination_directory(images, image_files)

if len(audio_files) != 0:
    move_to_destination_directory(audio, audio_files)

if len(video_files) != 0:
    move_to_destination_directory(videos, video_files)

if len(xlsx_files) != 0:
    move_to_destination_directory(xlsx, xlsx_files)

if len(exe_files) != 0:
    move_to_destination_directory(exe, exe_files)

if len(zip_files) != 0:
    move_to_destination_directory(zip_, zip_files)

if len(other_files) != 0:
    move_to_destination_directory(other, other_files)
