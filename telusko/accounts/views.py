from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth

from django.contrib import messages

# Create your views here..

def register(request):
  if request.method=='POST':
    
    first_name  = request.POST['fname']
    last_name   = request.POST['lname']
    username    = request.POST['username']
    email       = request.POST['email']
    password1   = request.POST['password1']
    password2   = request.POST['password2']
    
    if password1 == password2:
      
      if User.objects.filter(username=username).exists():
        print("Username Taken")
        messages.info(request, 'Username Taken')
        return redirect('register')
      
      elif User.objects.filter(email=email).exists():
        print("Email Exits")
        messages.info(request, 'Email Exits')
        return redirect('register')
      
      else:
        user =User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print("User Created")
        messages.info(request, 'User Created')
        return redirect('login')
    
    else: 
      print("Password Not Matching")
      messages.info(request, 'Password Not Matching')
      return redirect('register')
  
  else:  
    return render(request,'register.html')


def login(request):
  if request.method == 'POST':

    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username = username , password = password)

    if user is not None:
      auth.login(request,user)
      messages.info(request, 'Login Successfully')
      return redirect('/travello')

    else:
      messages.error(request, 'Username / Password Not Match')
      return redirect('login')

  else:
    return render(request,'login.html')  


def logout(request):
  # pass
  auth.logout(request)
  messages.error(request, 'Logout Succesfully')
  return redirect('/travello')

