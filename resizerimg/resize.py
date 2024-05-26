from PIL import Image
import os


def resize_images(input_folder, output_folder, size=(224, 224)):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterasi melalui setiap file di folder input
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            # Baca gambar
            img = Image.open(os.path.join(input_folder, filename))
            # Resize gambar
            img_resized = img.resize(size)
            # Simpan gambar yang sudah di-resize ke folder output
            img_resized.save(os.path.join(output_folder, filename))


# Contoh penggunaan
input_folder = 'path/to/input/folder'  # Ganti dengan path folder input Anda
output_folder = 'path/to/output/folder'  # Ganti dengan path folder output Anda

resize_images(input_folder, output_folder)
