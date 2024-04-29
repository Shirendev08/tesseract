# ocr_app/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pytesseract
from PIL import Image
import io
import base64
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        image_base64 = base64.b64encode(image).decode('utf-8')
        # text = pytesseract.image_to_string(Image.open(io.BytesIO(image)))      
        return render(request, 'index.html', {'text': image_base64})
    else:
        return render(request, 'index.html')



@csrf_exempt
def base64_to_text(request):
    if request.method == 'POST':
        try:
            json_data = request.POST.get('data')
            print(json_data)
            if json_data:
                data = json.loads(json_data)
                if data.get('action') == 'base64toText':
                    base64_data = data.get('data')
                    if base64_data:
                        # Decode the base64 string to bytes
                        image_bytes = base64.b64decode(base64_data)
                        # Process the image with Tesseract
                        text = base64(image_bytes)
                        return JsonResponse({'data': text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)






