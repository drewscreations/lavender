from django.shortcuts import render, redirect
from login_app.models import User, UserManager
from django.contrib import messages
from .models import EntranceSignal, SignalManager
# Create your views here.
def index(request):
    username=request.session.get('username','no username in session')
    userID=request.session.get('userID', 'no userID in sesison')
    content={
        'users':User.objects.all(),
        'username':username,
        'userID': userID,
        'activeUserLevel':User.objects.filter(id=userID)[0].user_level
    }
    return render(request, 'dashboard_index.html', content)
def data(request):
    username=request.session.get('username','no username in session')
    userID=request.session.get('userID', 'no userID in sesison')
    content={
        'signals':EntranceSignal.objects.all(),
        'username':username,
        'userID': userID,
        'activeUserLevel':User.objects.filter(id=userID)[0].user_level
    }
    return render(request, 'data_index.html', content)
def addDataPage(request):
    return render(request, 'add_data.html')
def validateNewData(request):
    errors = EntranceSignal.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/addData')
    else:
        name=request.POST['name']
        desc=request.POST['desc']
        timestamp=request.POST['timestamp']
        EntranceSignal.objects.create(name=name, desc=desc, timestamp=timestamp)
        messages.success(request, "Data Created")
    return redirect('/dashboard')
    