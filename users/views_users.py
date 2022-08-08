from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models_users import  UserImage
from home.models_home import Expense, Income
from datetime import date,datetime
# Create your views here.


def v_login(request):
    if request.method == 'POST':
        uname = request.POST['txt_username']
        passwd = request.POST['pwd_login']
        user = authenticate(username=uname,password=passwd)
        formdate = date.today()
        if user is not None:
            if user.is_active:
                login(request,user)
                exp = Expense.objects.filter(exp_date=formdate)
                return redirect(f"/home/{str(formdate)}",{'user':user, 'exps':exp, 'appdate' : formdate})
            else:
                return render(request,'login.html',{ 'comment' :'Please check your Uesrname and Password '} )
        else:
            return render(request,'login.html', {'comment' : 'User not found ! '})
    elif request.method == 'GET':
        return render(request,'login.html')

def v_register(request):
    if request.method == 'POST':
        ufname = request.POST['txt_firstname']
        ulname = request.POST['txt_lastname']
        passwd = request.POST['pwd_signin']
        confirm_passwd = request.POST['pwd_signin_2']
        umail = request.POST['txt_email']
        username = request.POST['txt_username']
        formdate = date.today()
        if User.objects.filter(username = username).exists():
            comment = 'Username is taken! Please choose a different username !'
            return render(request,'register.html', {'title': 'Sign In', 'comment': comment})
        elif User.objects.filter(email=umail).exists():
            comment = 'Email is taken! Please check the email once again or login with the current email'
            return render(request,'register.html', {'title': 'Sign In', 'comment': comment})
        else:
            if 8 <= len(passwd) <= 12:
                if passwd == confirm_passwd:
                    paswd = make_password(passwd)
                    usr = User(username=username, password=paswd,first_name=ufname,last_name = ulname,email=umail)
                    usr.save()
                    comment = 'Successfully signed in!'
                    messages.success(request, "Successfully signed in!")
                    formdate = date.today()
                    login(request,usr)
                    exp = Expense.objects.filter(exp_date=formdate)
                    return redirect(f"/home/{str(formdate)}",{'user':usr, 'exps':exp, 'appdate' : formdate})
                                
                else:
                    return render(request,'register.html', {'title': 'Sign In', 'comment':'Passwords are not matching!' })
            else:
                return render(request,'register.html', 
                {'title': 'Sign In', 'comment':'Passwords length is not matching! It should be within 8 to 12 characters.' })
    else:
        return render(request,'register.html', {'title': 'Sign In'})



def v_profile(request):
    if request.method=='GET':
        return render(request, "profile.html")
    elif request.method == 'POST':
        my_user = User.objects.filter(id=request.user.id)
        my_user = my_user[0]

        my_profile_pic = UserImage.objects.filter(id=my_user.id)
        u_img = request.POST.get('profile_pic')
        my_user.first_name = request.POST.get('txt_ufname', my_user.first_name)
        my_user.last_name = request.POST.get('txt_ulname', my_user.last_name)
        my_user.username = request.POST.get('txt_username', my_user.username )
        my_user.email = request.POST.get('txt_email',my_user.email )

        my_user.save()

        if my_profile_pic :
            my_profile_pic = my_profile_pic[0]
            my_profile_pic.userimage = u_img
            my_profile_pic.save()
        else:
            user_pro_pic = UserImage(userid=my_user, userimage=u_img)
            user_pro_pic.save()

        text = {'my_user': my_user, 'cmt': 'All working fine !'}
        return render(request, "profile.html", text )
    else:
        usr_img = UserImage.objects.filter(userid=request.user.id)
        if usr_img:
            propic = usr_img[0]
        else:
            propic = 'imgs/default.jpg'

        return render(request, "profle.html",  {'cmt': 'Unknown Method', 'user_img' : propic} )


def v_logout(request):
    auth.logout(request)
    return redirect("Index")