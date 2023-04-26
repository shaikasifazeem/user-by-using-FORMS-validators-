from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':

        TD=TopicForm(request.POST)
        if TD.is_valid():
            # TD.save()
            return HttpResponse('TOPIC DATA is inserted successfully!!!!')
        else:
            return HttpResponse('DATA is NOT VALID !!!')


    return render(request,'insert_topic.html',d)

# Create your views here.
