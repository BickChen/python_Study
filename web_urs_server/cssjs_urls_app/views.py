from django.shortcuts import render,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('500 一次！')

def login(request):
    return render(request, 'Untitled-2.html')

# def img(request):
#     return render(request, 'timg.jpg', content_type='image/gif')