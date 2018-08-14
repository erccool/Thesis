from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import SOM

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    all_SOMs = SOM.objects.all()
    context = {
        'all_SOMs' : all_SOMs ,
    }
    return render(request, 'SOM/index.html', context)

#html = ''
 #   for som in all_SOMs:
  #      url = '/SOM/' + str(som.id) + ''
   #     html += '<a href= "' + url + '">' + som.pic_name + '</a><br>'

def detail(request):
    file=request.POST['file_name']
    context = {
        'file':file,
    }
    return render(request, 'SOM/detail.html', context)