import asyncio
from django.shortcuts import render
from django.http import HttpResponse
from .services import process_request
from .models import DocHistory

def index(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        student = request.POST.get('student')
        dtype = request.POST.get('dtype')
        pages = int(request.POST.get('pages', 5))
        
        # Asinxron funksiyani sinxron Django ichida chaqirish
        try:
            file_io, filename = asyncio.run(process_request(topic, pages, dtype, student))
            
            # Tarixga yozish
            DocHistory.objects.create(
                web_user_ip=request.META.get('REMOTE_ADDR'),
                doc_type=dtype,
                topic=topic,
                pages=pages
            )
            
            response = HttpResponse(file_io.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        except Exception as e:
            return render(request, 'index.html', {'error': f"Xatolik: {str(e)}"})

    return render(request, 'index.html')