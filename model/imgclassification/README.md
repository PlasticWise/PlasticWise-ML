# Plastic Recycle Classification

## Overview

Proyek ini bertujuan untuk mengklasifikasikan gambar sampah plastik berdasarkan kode daur ulangnya (misalnya, PET, HDPE, PVC, LDPE, PP, PS). Proyek ini menggunakan teknik pembelajaran mesin, khususnya model konvolusi neural network (CNN) yang dilatih menggunakan MobileNetV2.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Training the Model](#training-the-model)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)

## Dataset

Dataset harus diatur dalam struktur folder sebagai berikut:

```
dataset/
    PET/
        Botol Minyak/
        Botol Plastic/
        tempat makan ovenproof/
    HDPE/
        Botol Susu (kecil)/
        Botol Jus/
        Kemasan Mentega/
    PVC/
        Botol Detergen/
        Shampoo/
        Pipa/
        Mika/
    LDPE/
        Kresek/
        botol yang ditekan/
    PP/
        pembukus biscuit/
        Botol Obat/
        Sedotan/
        Botol Minuman/
        Susu Bayi/
    PS/
        CD/
        Styrofoam/
        wadah makanan beku/
```

## Prerequisites

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal perangkat lunak dan library berikut:

- Python 3.6 atau lebih baru
- Jupyter Notebook
- TensorFlow
- Keras
- Pillow
- Numpy
- Pandas

Untuk menginstal library yang diperlukan, Anda bisa menjalankan:

```bash
pip install tensorflow keras pillow numpy pandas
```

## Setup

1. Clone repository ini:

   ```bash
   git clone https://github.com/PlasticWise/PlasticWise-ML.git
   cd model/imgclassification
   ```

2. Atur struktur folder dataset seperti yang dijelaskan di bagian [Dataset](#dataset).

3. Pindahkan gambar ke folder yang sesuai berdasarkan tipe objeknya dengan menggunakan script yang disediakan dalam notebook.

## Training the Model

1. Buka Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Buka file `ResourceModel.ipynb`.

3. Jalankan sel-sel dalam notebook secara berurutan untuk:
   - Mengatur struktur folder dan memetakan gambar.
   - Memuat dan meng-augmentasi dataset.
   - Melatih model menggunakan MobileNetV2.
   - Mengevaluasi model.

## Evaluation

Untuk mengevaluasi model, jalankan bagian evaluasi dalam notebook. Pastikan Anda memiliki dataset testing yang terpisah untuk mengevaluasi performa model.

## Results

Hasil pelatihan model akan mencakup metrik akurasi dan loss untuk dataset training dan validation. Evaluasi akhir akan memberikan akurasi pada dataset testing.

## Contributing

Jika Anda ingin berkontribusi dalam proyek ini, silakan buat pull request atau buka issue baru di repository ini.
