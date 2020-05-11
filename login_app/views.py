from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_index.html')
def signin(request):
    if 'userID' in request.session:
        return redirect('/dashboard')
    return render(request, 'signin.html')
def register(request):
    return render(request, 'register.html')
def validateNewUser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password_initial']
        hashword=bcrypt.hashpw(password.encode(), bcrypt.gensalt(14)).decode()
        if len(User.objects.all())==0:
            user_level=9
        else:
            user_level=0
        User.objects.create(first_name=first_name, last_name=last_name, email=email, hashword=hashword, user_level=user_level)
        messages.success(request, "User Created")
        # redirect to a success route
        print("~~~~~~~~~~~~~~~~creating USER, first name: "+first_name+"~~~~~~~~~~~~~~~~~~~~~~~~~")
        if 'userID' not in request.session:
            request.session['userID']=User.objects.get(email=email).id
            request.session['username']=User.objects.get(email=email).first_name
        return redirect('/dashboard')
def validateExistingUser(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.hashword.encode()):
            request.session['userID'] = logged_user.id
            request.session['username'] = logged_user.first_name
            return redirect('/dashboard')
    messages.error(request, 'Invalid username or password')
    return redirect('/signin')
def addNewUser(request):
    return render(request, 'add_user.html')
def editUser(request, my_id):
    editingUser = User.objects.get(id=my_id)
    username=request.session.get('username','no username in session')
    userID=request.session.get('userID', 'no userID in sesison')
    content={
        'users':User.objects.all(),
        'username':username,
        'userID': userID,
        'activeUserLevel':User.objects.filter(id=userID)[0].user_level,
        'editingUser':editingUser
    }
    return render(request, 'edit_user.html', content)
def validateEditUserName(request, my_id):
    errors = User.objects.edit_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/myAccount/'+str(my_id))
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        editUser = User.objects.get(id=my_id)
        editUser.first_name=first_name
        editUser.last_name=last_name
        editUser.email=email
        editUser.save()
        return redirect('/home')
def logout(request):
    request.session.flush()
    return redirect('/')