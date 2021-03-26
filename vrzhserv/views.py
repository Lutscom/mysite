from django.shortcuts import render
from django.http import HttpResponse


def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def html1(request):
    return render(request, 'vrzhserv/cat.html')

def html2(request):
    return render(request, 'vrzhserv/dog.html')
def index(request):
    return render(request, 'vrzhserv/1.html')
def index1(request):
    remote_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    ip = remote_address
    user_info = request.META.get('HTTP_USER_AGENT')
    return render(request, 'vrzhserv/2.html', locals())