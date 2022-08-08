from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models_home import Expense, Income
from datetime import date,datetime

# Create your views here.
def v_index(request, comment=""):
    return render(request, 'index.html', {'comment' : comment } )

def v_home(request,sdate):
    if request.method== 'GET':
        ddate=datetime.strptime(sdate,"%Y-%m-%d")
        
        ex = Expense.objects.filter(userid= request.user, exp_date=ddate)
        totexp=sum( [e.exp_amount for e in ex ] )

        inc = Income.objects.filter(userid = request.user, inc_date=ddate)
        totinc = sum( [i.inc_amount for i in inc] )

        inc_all = Income.objects.filter(userid = request.user) 
        exp_all = Expense.objects.filter(userid= request.user)
        inc_mon = sum([i.inc_amount for i in inc_all if i.inc_date.month == ddate.month])
        exp_mon = sum([i.exp_amount for i in exp_all if i.exp_date.month == ddate.month])

        bal = inc_mon - exp_mon
        context = { 
            'exps':ex,          'incs': inc,        'appdate':sdate, 
            'totexp':totexp,    'totinc':totinc,    'expone': False,
            'bal_amt' : bal ,
            }
        return render(request,'homepage.html',context)
      


def v_add(request,expense, amount,desc,expdate):
    mon_list = ['None','Jauary', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'] 
    dexpdate=datetime.strptime(expdate,"%Y-%m-%d")
    mon = mon_list[dexpdate.month]
    yr = dexpdate.year
    objExp=Expense(userid=request.user,exp_date=dexpdate,exp_name=expense,exp_desc=desc , exp_amount=amount , exp_month = mon,exp_year = yr )
    objExp.save()
    return redirect(f"/home/{expdate}")

def v_add_inc(request,inc, amount,desc,incdate):
    mon_list = ['None','Jauary', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'] 
    dincdate=datetime.strptime(incdate,"%Y-%m-%d")
    mon = mon_list[dincdate.month]
    yr = dincdate.year
    objInc=Income(userid=request.user,inc_date=dincdate,inc_name=inc,inc_desc=desc , inc_amount=amount , inc_month = mon,inc_year = yr )
    objInc.save()
    return redirect(f"/home/{incdate}")


def v_update(request,eid, expense, amount,desc,expdate):
    mon_list = ['None','January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'] 
    dexpdate=datetime.strptime(expdate,"%Y-%m-%d")
    mon = mon_list[dexpdate.month]
    yr = dexpdate.year
    objExp=Expense(userid=request.user,id=eid,exp_date=dexpdate,exp_name=expense,exp_desc=desc , exp_amount=amount , exp_month = mon,exp_year = yr )
    objExp.save()
    return redirect(f"/home/{expdate}")


def v_update_inc(request,iid, inc, amount,desc,incdate):
    mon_list = ['None','January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'] 
    dincdate=datetime.strptime(incdate,"%Y-%m-%d")
    mon = mon_list[dincdate.month]
    yr = dincdate.year
    objInc=Income(userid=request.user,id=iid,inc_date=dincdate,inc_name=inc,inc_desc=desc , inc_amount=amount , inc_month = mon,inc_year = yr )
    objInc.save()
    return redirect(f"/home/{incdate}")


def v_delete(request,expid,expdate):
    exp = Expense.objects.filter(id=expid)
    exp.delete()
    return redirect(f"/home/{expdate}")


def v_delete_inc(request,incid,incdate):
    inc = Income.objects.filter(id=incid)
    inc.delete()
    return redirect(f"/home/{incdate}")


def v_report(request,mon,yr):
    exps = Expense.objects.filter(userid = request.user, exp_month = mon, exp_year = yr)
    incs = Income.objects.filter(userid = request.user, inc_month = mon, inc_year = yr)
    mon_dict = {'January' : '01', 'February' : '02', 'March': '03', 'April' : '04', 'May' : '05', 'June' : '06', 
    'July' : '07', 'August' : '08', 'September' : '09', 'October' : '10', 'November' : '11', 'December':'12', } 
    page_date = yr +"-" + mon_dict[mon]
    exps_o = exps.order_by('exp_date')
    incs_o = incs.order_by('inc_date')
    exp_list = [e.exp_amount for e in exps]
    inc_list = [i.inc_amount for i in incs]
    totexp = sum(exp_list)
    totinc = sum(inc_list)
    vals = {    'exps' : exps_o, 'totexp' : totexp, 'page_date': page_date ,
                'incs' : incs_o, 'totinc' : totinc }
    return render(request,'reports.html', vals)

def v_find(request,p_txn_name = " "):
    if p_txn_name == " ":
        txn_cmt="Empty"
        return render(request,"findexp.html", { 'txn_cmt' : txn_cmt })
    exps = Expense.objects.filter(userid = request.user, exp_name = p_txn_name)           
    incs = Income.objects.filter(userid = request.user, inc_name = p_txn_name)
    txns = list(exps) + list(incs)
    
    if len(txns) ==0 :
        txt_cmt = "404"
        return render(request,"findexp.html", { 'txn_cmt' : txt_cmt })    
    else:
        if incs.count() !=0 and exps.count() !=0 :    
            return render(request,"findexp.html", { 'incs' : incs , 'exps' : exps, 'txn_cmt' : '200' }) 
        elif incs.count() == 0 and exps.count() !=0:
            return render(request,"findexp.html", { 'exps' : exps , 'txn_cmt' : '200'})
        elif exps.count() == 0 and incs.count() !=0:
            return render(request,"findexp.html", { 'incs' : incs , 'txn_cmt' : '200' })       
        return render(request,"findexp.html", { 'txn_cmt' : '404' })    
