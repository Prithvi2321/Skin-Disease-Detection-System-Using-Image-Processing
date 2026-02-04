# Skin Disease Detection Using Image Processing and Machine Learning

## Overview

Skin diseases are widespread and early diagnosis is essential for effective treatment. However, traditional diagnosis depends heavily on dermatologists and is not always accessible, especially in rural or underserved areas.

This project presents an automated system for detecting and classifying non-cancerous skin diseases using image processing and machine learning techniques. Deep learning models such as Convolutional Neural Networks (CNNs) are used to analyze skin images and assist in fast and accurate diagnosis.

---

## Objectives

- To automate the detection of skin diseases from medical images  
- To preprocess skin images for improved quality and consistency  
- To classify skin diseases using machine learning and deep learning models  
- To improve accessibility to dermatological diagnosis through technology  

---

## Dataset

The dataset consists of labeled images of various non-cancerous skin diseases such as eczema, psoriasis, and benign lesions. All images are resized and preprocessed before training to ensure uniformity and better model performance.

### Dataset Link
https://www.kaggle.com/datasets/ismailpromus/skin-diseases-image-dataset
---

## Methodology

- Image preprocessing using noise removal, resizing, and contrast enhancement  
- Feature extraction based on color, texture, and shape  
- Classification using traditional machine learning models such as SVM, KNN, and Decision Trees  
- Deep learning using CNN architectures and transfer learning techniques  

---

## Folder Structure

```
├── 📁 SkinDiseaseDetection
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py
│   ├── 🐍 settings.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
├── 📁 detection
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   ├── 🐍 0002_skindiseasedetection_severity.py
│   │   ├── 🐍 0003_remove_skindiseasedetection_severity.py
│   │   └── 🐍 __init__.py
│   ├── 📁 static
│   │   ├── 📁 css
│   │   │   ├── 📁 js
│   │   │   │   └── 📁 images
│   │   │   │       ├── 🖼️ ai_detection.jpg
│   │   │   │       ├── 🖼️ atopic_dermatitis.jpg
│   │   │   │       ├── 🖼️ bcc.jpg
│   │   │   │       ├── 🖼️ benign_keratosis.jpg
│   │   │   │       ├── 🖼️ comprehensive_reports.jpg
│   │   │   │       ├── 🖼️ easy_to_use.jpg
│   │   │   │       ├── 🖼️ eczema.jpg
│   │   │   │       ├── 🖼️ logo.png
│   │   │   │       ├── 🖼️ melanocytic_nevi.jpg
│   │   │   │       ├── 🖼️ melanoma.jpg
│   │   │   │       ├── 🖼️ psoriasis.jpg
│   │   │   │       ├── 🖼️ seborrheic_keratoses.jpg
│   │   │   │       ├── 🖼️ skin_disease_info.jpg
│   │   │   │       ├── 🖼️ tinea.jpg
│   │   │   │       └── 🖼️ warts.jpg
│   │   │   └── 🎨 style.css
│   │   ├── 📁 images
│   │   │   └── 🖼️ 3964906.jpg
│   │   └── 📁 videos
│   │       ├── 🎬 background.mp4
│   │       └── 🎬 background1.mp4
│   ├── 📁 templates
│   │   ├── 📁 detection
│   │   │   ├── 🌐 detect.html
│   │   │   ├── 🌐 detection.html
│   │   │   ├── 🌐 home.html
│   │   │   ├── 🌐 login.html
│   │   │   ├── 🌐 report_template.html
│   │   │   ├── 🌐 results.html
│   │   │   └── 🌐 signup.html
│   │   ├── 🌐 about.html
│   │   ├── 🌐 common_diseases.html
│   │   └── 🌐 contact.html
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 forms.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📁 media
│   ├── 📁 histograms
│   │   ├── 🖼️ histogram_Ganesh.png
│   │   └── 🖼️ histogram_Prithviraj_Rajendra_Patil.png
│   └── 📁 uploads
│       ├── 🖼️ ISIC_0000130_downsampled.jpg
│       ├── 🖼️ ISIC_0010493.jpg
│       ├── 🖼️ ISIC_0010498.jpg
│       ├── 🖼️ ISIC_0014943_downsampled.jpg
│       ├── 🖼️ ISIC_0026298.jpg
│       ├── 🖼️ ISIC_6664275.jpg
│       ├── 🖼️ ISIC_6676508.jpg
│       ├── 🖼️ ISIC_6824744.jpg
│       └── 🖼️ t-eczema-hand-10.jpg
├── 📁 uploads
├── 📄 db.sqlite3
└── 🐍 manage.py
```
---

## Output
<img width="942" height="1108" alt="image" src="https://github.com/user-attachments/assets/54bd0ddd-9ddd-4071-9273-e9838776779a" />

<img width="941" height="1291" alt="image" src="https://github.com/user-attachments/assets/52ee2075-a67c-473d-9f7b-f582c946c229" />

<img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/400f827a-2e2a-4182-80b3-f83fe2d39229" />

<img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/37594044-49b8-4355-84fd-bd53cf30a899" />

<img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/692d7243-6743-4b95-95c1-7e139d9019fe" />

<img width="940" height="945" alt="image" src="https://github.com/user-attachments/assets/51798583-e6d0-4e4a-9069-be55fdc13b61" />

---




