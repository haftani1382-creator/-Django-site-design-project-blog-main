from django.shortcuts import render
from django.contrib import messages , auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from bloggers.models import Blogger

def register(request):

 if request.method == 'POST':
    #get form variable 


    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    #check if password match
    if password == password2:
       # check username
       if User.objects.filter(username=username).exists():
          messages.error(request , 'این نام کاربری در دسترس نیست')
          return redirect('register')
       else:
        if User.objects.filter(email=email).exists():
          messages.error(request ,'این ایمیل قبلا استفاده شده')
          return redirect('register')
          
        else:
           #its ok  
           user = User.objects.create_user(username=username , password=password , email=email , first_name=name)
           # create blogger
           blooger = Blogger.objects.create(name= name , user=user , email=email )
           # login after registration
           auth.login(request , user)
           messages.success(request , 'ثبت نام با موفقیت انجام شد')
           
           return redirect('index1')

    else:
       messages.error(request , 'رمز های عبور وارد شده مطابق نیستند')   
       return redirect('register')

 else: 
    return render(request , 'accounts/register.html')

def login(request):

 if request.method == 'POST':
    # login user
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username = username , password=password)

    if user is not None:
       auth.login(request , user)
       messages.success(request , 'شما وارد سایت شدید')
       return redirect('index')
    else :
       messages.error(request , 'رمز اشتباه وارد شده لطفا دوباره امتحان کنید')
       return redirect('login')

    
 else:   
    return render(request , 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       messages.success(request , 'شما از حساب کاربری خارج شدید')
       return redirect('index')
    else:
        return redirect('index')


    