from django.shortcuts import render
from datetime import datetime

def home(request):
    time = datetime.now()
    time_day = time.strftime('%A')
    context = {
        'time': time,
        'time_day': time_day
    }
    return render(request, 'home.html', context)