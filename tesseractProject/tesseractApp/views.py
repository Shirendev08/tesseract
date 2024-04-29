# ocr_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import pytesseract
from PIL import Image
import io

def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        img = Image.open(io.BytesIO(image))
        text = pytesseract.image_to_string(img)
        return render(request, 'extracted_text.html', {'text': text})
    else:
        return render(request, 'index.html')
