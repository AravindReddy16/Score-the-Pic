from django.shortcuts import render,redirect
import random
from .models import *

# Create your views here.

def mainPage(request):
    data = DataPic.objects.all()
    rand_obj1 = random.choice(data)
    rand_obj2 = random.choice(data)
    total_votes = 1
    for vote in list(data):
        total_votes += vote.votes
    if rand_obj1 != rand_obj2:
        rand_data1 = rand_obj1
        rand_data2 = rand_obj2
    else:
        return redirect('mainpage')
    if request.method == 'POST':
        photos = request.FILES.getlist('image')
        print(photos)

        for photo in photos:
            new_obj = DataPic.objects.create(image = photo)
            new_obj.save()
        return redirect('mainpage')
    context = {'data1': rand_data1, 'data2': rand_data2,'data1_votes':(round(((rand_data1.votes/total_votes)*100),1)), 'data2_votes':(round(((rand_data2.votes/total_votes)*100),1))}
    return render(request,'scorepicapp/index.html',context)

def count(request,id):
    data = DataPic.objects.get(id=id)
    data.votes += 1
    data.save()