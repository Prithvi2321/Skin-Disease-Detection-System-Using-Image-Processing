import matplotlib
matplotlib.use('Agg')  # Disable GUI
from mpl_toolkits.mplot3d import Axes3D
import json
from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm 
from django.utils import timezone
from django.core.files.storage import default_storage
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from django.conf import settings
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from django.urls import reverse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import pdfkit  # Install using: pip install pdfkit
import os





# Create your views here.

def home(request):
    return render(request, 'detection/home.html')


def common_diseases(request):
    diseases = [
        {
            "name": "Eczema",
            "image": "css/js/images/eczema.jpg",
            "description": "A condition causing inflamed, itchy, cracked, and rough skin.",
            "link": "https://www.aad.org/public/diseases/eczema"
        },
        {
            "name": "Melanoma",
            "image": "css/js/images/melanoma.jpg",
            "description": "A dangerous form of skin cancer that develops from pigment-producing cells.",
            "link": "https://www.cancer.org/cancer/melanoma-skin-cancer.html"
        },
        {
            "name": "Atopic Dermatitis",
            "image": "css/js/images/atopic_dermatitis.jpg",
            "description": "A chronic condition that makes your skin red and itchy.",
            "link": "https://www.aad.org/public/diseases/eczema/atopic-dermatitis"
        },
        {
            "name": "Basal Cell Carcinoma (BCC)",
            "image": "css/js/images/bcc.jpg",
            "description": "The most common form of skin cancer, caused by prolonged sun exposure.",
            "link": "https://www.aad.org/public/diseases/skin-cancer/basal-cell-carcinoma"
        },
        {
            "name": "Melanocytic Nevi (NV)",
            "image": "css/js/images/melanocytic_nevi.jpg",
            "description": "Common moles that are usually harmless but can develop into melanoma.",
            "link": "https://www.skincancer.org/skin-cancer-information/melanoma/moles/"
        },
        {
            "name": "Benign Keratosis-like Lesions",
            "image": "css/js/images/benign_keratosis.jpg",
            "description": "Non-cancerous growths that appear as rough, scaly patches on the skin.",
            "link": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10188172/"
        },
        {
            "name": "Psoriasis",
            "image": "css/js/images/psoriasis.jpg",
            "description": "An autoimmune disease that causes red, scaly patches on the skin.",
            "link": "https://www.aad.org/public/diseases/psoriasis"
        },
        {
            "name": "Seborrheic Keratoses",
            "image": "css\js\images\seborrheic_keratoses.jpg",
            "description": "Non-cancerous, wart-like growths that appear on the skin as people age.",
            "link": "https://dermnetnz.org/topics/seborrhoeic-keratosis"
        },
        {
            "name": "Tinea (Ringworm, Candidiasis)",
            "image": "css/js/images/tinea.jpg",
            "description": "A group of fungal infections that affect the skin, hair, and nails.",
            "link": "https://www.cdc.gov/ringworm/about/?CDC_AAref_Val=https://www.cdc.gov/fungal/diseases/ringworm/index.html"
        },
        {
            "name": "Warts, Molluscum, and Viral Infections",
            "image": "css/js/images/warts.jpg",
            "description": "Viral skin infections that cause growths or sores on the skin.",
            "link": "https://www.ncbi.nlm.nih.gov/books/NBK441898/"
        }
    ]
    disease_counts = {
        "Eczema": 150,
        "Psoriasis": 120,
        "Acne": 300,
        "Rosacea": 80,
        "Melanoma": 50,
        "Vitiligo": 70,
        "Hives": 100,
        "Dermatitis": 130,
        "Ringworm": 90,
        "Cold Sores": 110
    }

    
    # return render(request, "common_diseases.html", {"diseases": diseases,"disease_counts": disease_counts})
    return render(request, "common_diseases.html", {
    "diseases": diseases,
    "disease_counts": json.dumps(disease_counts)  # Convert dictionary to JSON string
})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Trying to authenticate {username}...")  # Debugging line
            user = authenticate(username=username, password=password)
            
            if user is not None:
                print(f"Authentication successful for {username}. Redirecting...")  # Debugging line
                login(request, user)
                return redirect('detect')  # Ensure 'detect' is correctly named in urls.py
            
            else:
                print("Authentication failed")  # Debugging line
        else:
            print("Form is not valid")  # Debugging line
            print(form.errors)  # Debugging line
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'detection/login.html', {'form': form})

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')  # Ensure 'login_user' exists in urls.py
    else:
        form = UserCreationForm()
    return render(request, 'detection/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login_user')  # Ensure 'login_user' exists in urls.py

def detect_page(request):
    return render(request, 'detect.html')



@login_required
def detect_page(request):
    # if request.method == "POST":
    #     uploaded_image = request.FILES['image']
    #     # Process the image (your ML model code here)
    #     return render(request, 'result.html', {'image': uploaded_image})
    
    return render(request, 'detection/detect.html')




# ✅ Load Model
MODEL_PATH = r"C:\Projects\DJANGO\Diploma\training\trains\optimized_skin_disease_cnn_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Get Correct Input Size from Model
correct_input_size = model.input_shape[1:3]  # Extract (height, width)
import re

# ✅ Fixed Class Labels
class_labels = [
    '1. Eczema 1677', 
    '10. Warts Molluscum and other Viral Infections - 2103', 
    '2. Melanoma 15.75k', 
    '3. Atopic Dermatitis - 1.25k', 
    '4. Basal Cell Carcinoma (BCC) 3323', 
    '5. Melanocytic Nevi (NV) - 7970', 
    '6. Benign Keratosis-like Lesions (BKL) 2624', 
    '7. Psoriasis pictures Lichen Planus and related diseases - 2k', 
    '8. Seborrheic Keratoses and other Benign Tumors - 1.8k', 
    '9. Tinea Ringworm Candidiasis and other Fungal Infections - 1.7k'
]
clean_labels = [re.sub(r'^\d+\.\s*|\s*[-\d.kK]+$', '', label).strip() for label in class_labels]
from .models import SkinDiseaseDetection  # Import the existing model
from django.contrib.auth.models import User  # Import User model if needed

import matplotlib.pyplot as plt
import numpy as np
import os
import json
from django.conf import settings
from django.core.files.storage import default_storage
import tensorflow as tf
from django.shortcuts import render, redirect
from .models import SkinDiseaseDetection  # Import the existing model
from django.contrib.auth.models import User  # Import User model if needed

def process_image(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        if not image:
            return redirect('detect')

        # ✅ Save Image
        file_path = default_storage.save(os.path.join('uploads', image.name), image)
        full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        uploaded_image_url = settings.MEDIA_URL + file_path  

        # ✅ Load and Preprocess Image
        img = tf.keras.preprocessing.image.load_img(full_file_path, target_size=correct_input_size)
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  
        img_array = img_array / 255.0  

        # ✅ Make Prediction
        predictions = model.predict(img_array)[0]

        # ✅ Format Predictions
        disease_labels = class_labels  # List of disease names
        disease_probabilities = [round(pred * 100, 2) for pred in predictions]  # Convert to percentage

        # ✅ Determine Most Probable Disease
        max_index = np.argmax(predictions)
        predicted_disease = class_labels[max_index]
        prediction_confidence = disease_probabilities[max_index]

        

        # ✅ Store Detection in Database
        user = request.user if request.user.is_authenticated else None
        SkinDiseaseDetection.objects.create(
            user=user,
            name=name,
            dob=dob,
            gender=gender,
            contact=contact,
            uploaded_image=file_path,
            predicted_disease=predicted_disease,
            prediction_confidence=prediction_confidence
        )

        # ✅ Generate Simple Histogram (Additional)
        plt.figure(figsize=(10, 5))
        plt.bar(disease_labels, disease_probabilities, color='blue', alpha=0.7)
        plt.xlabel('Skin Diseases')
        plt.ylabel('Probability (%)')
        plt.title('Predicted Disease Probabilities')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # ✅ Save the Histogram Image
        histogram_filename = f"histogram_{name.replace(' ', '_')}.png"
        histogram_path = os.path.join(settings.MEDIA_ROOT, 'histograms', histogram_filename)
        os.makedirs(os.path.dirname(histogram_path), exist_ok=True)  # Ensure directory exists
        plt.savefig(histogram_path)
        plt.close()

        # ✅ Store in Session
        request.session['name'] = name
        request.session['dob'] = dob
        request.session['gender'] = gender
        request.session['contact'] = contact
        request.session['predictions'] = json.dumps(disease_probabilities)  # Store as JSON string
        request.session['disease_labels'] = json.dumps(disease_labels)
        request.session['predicted_disease'] = predicted_disease
        request.session['prediction_confidence'] = f"{prediction_confidence:.2f}%"
        request.session['uploaded_image_url'] = f"/media/{file_path}"
        request.session['histogram_path'] = f"/media/histograms/{histogram_filename}"  # Add histogram path

        return render(request, 'detection/results.html', {
            'name': name, 'dob': dob, 'gender': gender, 'contact': contact,
            'predictions': json.dumps(disease_probabilities),  # Pass JSON to template
            'disease_labels': json.dumps(disease_labels),
            'predicted_disease': predicted_disease,
            'prediction_confidence': f"{prediction_confidence:.2f}%",
            'uploaded_image_url': uploaded_image_url,
            'histogram_path': f"/media/histograms/{histogram_filename}"  # Pass histogram path to template
        })

    return redirect('detect')




def results_page(request):
    return render(request, 'detection/results.html')
def results_page(request):
    return render(request, 'detection/results.html')

import re
import json
import io
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


import base64
from django.conf import settings
import os

def generate_pdf(request):
    # Existing session data
    session_data = {
        'name': request.session.get('name', 'Unknown').strip(),
        'dob': request.session.get('dob', 'Unknown'),
        'gender': request.session.get('gender', 'Unknown'),
        'contact': request.session.get('contact', 'Unknown'),
        'predictions': request.session.get('predictions', '[]'),
        'disease_labels': request.session.get('disease_labels', '[]'),
        'predicted_disease': request.session.get('predicted_disease', 'Unknown'),
        'prediction_confidence': request.session.get('prediction_confidence', '0.00%'),
        'uploaded_image_url': request.session.get('uploaded_image_url', '')
    }

    # Get base64 image if exists
    image_data = ''
    if session_data['uploaded_image_url']:
        image_path = os.path.join(settings.MEDIA_ROOT, session_data['uploaded_image_url'].replace('/media/', ''))
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                image_data = base64.b64encode(img_file.read()).decode('utf-8')

    # Clean and prepare data
    safe_name = re.sub(r'[^\w\s-]', '', session_data['name']).replace(" ", "_")
    predictions = json.loads(session_data['predictions'])
    disease_labels = json.loads(session_data['disease_labels'])

    def clean_label(label):
        return re.sub(r'^\d+\.\s*', '', str(label)).strip()

    cleaned_labels = [clean_label(label) for label in disease_labels]
    cleaned_predicted_disease = clean_label(session_data['predicted_disease'])
    disease_data = list(zip(cleaned_labels, predictions))

    # Context with base64 image
    context = {
        "name": session_data['name'],
        "dob": session_data['dob'],
        "gender": session_data['gender'],
        "contact": session_data['contact'],
        "disease_data": disease_data,
        "predicted_disease": cleaned_predicted_disease,
        "prediction_confidence": session_data['prediction_confidence'],
        "uploaded_image_base64": image_data
    }

    # Render and create PDF
    html_content = render_to_string("detection/report_template.html", context)
    buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)

    if pisa_status.err:
        return HttpResponse("Error generating PDF", content_type="text/plain")

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{safe_name}_diagnosis_report.pdf")

# def generate_pdf(request):
#     # Retrieve stored session data
#     session_data = {
#         'name': request.session.get('name', 'Unknown').strip(),
#         'dob': request.session.get('dob', 'Unknown'),
#         'gender': request.session.get('gender', 'Unknown'),
#         'contact': request.session.get('contact', 'Unknown'),
#         'predictions': request.session.get('predictions', '[]'),
#         'disease_labels': request.session.get('disease_labels', '[]'),
#         'predicted_disease': request.session.get('predicted_disease', 'Unknown'),
#         'prediction_confidence': request.session.get('prediction_confidence', '0.00%'),
#         'uploaded_image_url': request.session.get('uploaded_image_url', '')
#     }

#     # Sanitize filename
#     safe_name = re.sub(r'[^\w\s-]', '', session_data['name']).replace(" ", "_")

#     # Parse JSON data
#     predictions = json.loads(session_data['predictions'])
#     disease_labels = json.loads(session_data['disease_labels'])
    
#     # Clean disease names by removing numbers and dots
#     def clean_label(label):
#         return re.sub(r'^\d+\.\s*', '', str(label)).strip()
    
#     cleaned_labels = [clean_label(label) for label in disease_labels]
#     cleaned_predicted_disease = clean_label(session_data['predicted_disease'])
    
#     # Zip cleaned data together
#     disease_data = list(zip(cleaned_labels, predictions))

#     # Prepare context
#     context = {
#         "name": session_data['name'],
#         "dob": session_data['dob'],
#         "gender": session_data['gender'],
#         "contact": session_data['contact'],
#         "disease_data": disease_data,
#         "predicted_disease": cleaned_predicted_disease,
#         "prediction_confidence": session_data['prediction_confidence'],
#         "uploaded_image_url": session_data['uploaded_image_url']
#     }

#     # Load the HTML template
#     html_content = render_to_string("detection/report_template.html", context)

#     # Generate PDF
#     buffer = io.BytesIO()
#     pisa_status = pisa.CreatePDF(html_content, dest=buffer)

#     if pisa_status.err:
#         return HttpResponse("Error generating PDF", content_type="text/plain")

#     buffer.seek(0)
#     return FileResponse(
#         buffer,
#         as_attachment=True,
#         filename=f"{safe_name}_diagnosis_report.pdf",
#         content_type='application/pdf'
#     )


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Contact Page View
def contact(request):
    return render(request, 'contact.html')

# Contact Form Submission View
def submit_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send email (Optional)
        send_mail(
            f"Contact Form Submission from {name}",
            message,
            email,
            ['prithvirajpatil495@gmail.com'],  # Replace with your email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirect back to contact page

    return render(request, 'contact.html')

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')




