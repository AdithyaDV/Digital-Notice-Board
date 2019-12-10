from django.shortcuts import render
from .models import Text
from datetime import datetime
from datetime import timedelta as td
# Create your views here.

def textpage(request):
    textlines = Text.objects
    data_list = list(textlines.values())
    data_list_1 = []
    print(data_list)
    for i in range(len(data_list)):
        vec = data_list[i]
        if vec['screenNo']==1:
            print(i)
            data_list_1.append(data_list[i])
    print(data_list_1)
    new_list = sorted(data_list_1, key=lambda i: i['time'], reverse = 1)
    i=0;
    while True:
        dict = new_list[i]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dict['time']  = dict['time'] + td(0, 0, 0, 0, 30, 5, 0)
        dict['endtime'] = dict['endtime'] + td(0, 0, 0, 0, 30, 5, 0)
        uploading_time = dict['time'].strftime("%H:%M:%S")
        end_time = dict['endtime'].strftime("%H:%M:%S")
        print(current_time)
        print(uploading_time)
        if (current_time < uploading_time)or(current_time > end_time):
            i = i+1
        else:
            break
    return render(request, 'Textpage.html',  {'user': dict['user'], 'text': dict['text'],'time': dict['time']})


def textpage1(request):
    textlines = Text.objects
    data_list = list(textlines.values())
    data_list_1 = []
    print(data_list)
    for i in range(len(data_list)):
        vec = data_list[i]
        if vec['screenNo']==2:
            print(i)
            data_list_1.append(data_list[i])
    print(data_list_1)
    new_list = sorted(data_list_1, key=lambda i: i['time'], reverse = 1)
    i=0;
    while True:
        dict = new_list[i]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dict['time']  = dict['time'] + td(0, 0, 0, 0, 30, 5, 0)
        dict['endtime'] = dict['endtime'] + td(0, 0, 0, 0, 30, 5, 0)
        uploading_time = dict['time'].strftime("%H:%M:%S")
        end_time = dict['endtime'].strftime("%H:%M:%S")
        print(current_time)
        print(uploading_time)
        if (current_time < uploading_time)or(current_time > end_time):
            i = i+1
        else:
            break
    return render(request, 'Textpage1.html',  {'user': dict['user'], 'text': dict['text'],'time': dict['time']})
# Create your views here.
