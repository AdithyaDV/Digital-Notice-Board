from django.shortcuts import render
from .models import Video
from datetime import datetime
from datetime import timedelta as td

def videopage(request):
    posts = Video.objects
    data_list = list(posts.values())
    data_list_1 = []
    print(data_list)
    for i in range(len(data_list)):
        vec = data_list[i]
        if vec['screenNo'] == 1:
            print(i)
            data_list_1.append(data_list[i])
    print(data_list_1)
    new_list = sorted(data_list_1, key=lambda i: i['time'], reverse=1)
    i = 0;
    while True:
        dict = new_list[i]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dict['time'] = dict['time'] + td(0, 0, 0, 0, 30, 5, 0)
        uploading_time = dict['time'].strftime("%H:%M:%S")
        print(current_time)
        print(uploading_time)
        if current_time < uploading_time:
            i = i + 1
        else:
            break
    return render(request, 'videopage.html', {'user': dict['user'], 'videourl': dict['file'], 'time': dict['time'], 'duration': dict['durationInSeconds']})


def videopage1(request):
    posts = Video.objects
    data_list = list(posts.values())
    data_list_1 = []
    print(data_list)
    for i in range(len(data_list)):
        vec = data_list[i]
        if vec['screenNo'] == 2:
            print(i)
            data_list_1.append(data_list[i])
    print(data_list_1)
    new_list = sorted(data_list_1, key=lambda i: i['time'], reverse=1)
    i = 0;
    while True:
        dict = new_list[i]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dict['time'] = dict['time'] + td(0, 0, 0, 0, 30, 5, 0)
        uploading_time = dict['time'].strftime("%H:%M:%S")
        print(current_time)
        print(uploading_time)
        if current_time < uploading_time:
            i = i + 1
        else:
            break
    return render(request, 'videopage1.html', {'user': dict['user'], 'videourl': dict['file'], 'time': dict['time'], 'duration':dict['durationInSeconds']})
