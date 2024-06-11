
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # Add your video downloading logic here
        return render(request, 'index.html', {'downloaded': True})
    return render(request, 'index.html', {'downloaded': False})
