
from django import shortcuts
from django.contrib.messages.api import error
from django.db.models.query import RawQuerySet
from django.db.models.query_utils import refs_expression
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from vacc.models import details
from django.contrib import messages
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
import re
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['Name']
        aad = request.POST['Aadhar_number']
        phone = request.POST['Phone_number']
        vacc = request.POST['Vaccine']
        gen = request.POST['Gender']
        age = request.POST['Age']
        dat = request.POST['Date']
        dos = request.POST.get('doseage')
        dis = request.POST.get('Disability')
        group  = request.POST.get('Group')
        first_3 = name[:3]
        last_4 = aad[-4:]
        ref = first_3+last_4
        state = request.POST['State']
        district = request.POST['District']
        addr = request.POST['Aadress']
        pin = request.POST['Pin']
        nu = "+91"+phone
        my_number = phonenumbers.parse(nu)
        rr = phonenumbers.is_valid_number(my_number) # moblie number validataion
        s = aad
        s1 = s[:4]+" "+s[4:8]+" "+s[-4:]
        def isValidAadharNumber(str):
            regex = ("^[2-9]{1}[0-9]{3}\\" +
                "s[0-9]{4}\\s[0-9]{4}$")
            p = re.compile(regex)
            if (str == None):
                return False
            if(re.search(p, str)):
                return True
            else:
                return False
        aa = isValidAadharNumber(s1)
        if(len(aad) != 12 or aa != True or aad.isnumeric() == False):
            messages.error(request,"Enter valid Aadhar number")
            return render(request,'index.html')
        elif(len(phone) != 10 or rr != True or phone.isnumeric() == False):
            messages.info(request, "Enter valid mobile numebr")
            return render(request,'index.html')
               
        elif(len(pin) != 6):
            messages.info(request,"Entercorrect pincode")
            return render(request,'index.html')
        
        elif details.objects.filter(Aadhar_number = aad).exists():
            messages.info(request,"aadhar present already")
            return render(request,'index.html')
        elif (dos is None or dis is None or group is None):
            messages.info(request,"Fill all entries properly and check for blank")
            return render(request,'index.html')
        else:
            sa = details(Name = name,Aadhar_number = aad,Phone_number =phone,
                Vaccine = vacc,Gender =gen,Age = age,Date = dat,doseage = dos,Disability = dis,Ref_token = ref,
                Group = group,State = state,District = district,Aadress = addr,Pin = pin)
            sa.save()
            messages.success(request,"Registration is succesful..!!and Ref_token is : "+ref)
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def retrive(request):
    try :
        if 'Q' in request.GET:
            q = request.GET['Q']
            p = details.objects.filter(Ref_token__icontains = q)
            return render(request,'retrive.html',{'p':p})
        else:
            return render(request,'retrive.html')
    except details.DoesNotExist:
        return render(request,'retrive.html')

def updation(request,id):
    re = details.objects.get(id =id)
    re1 = request.POST.get('Status')
    re2 = request.POST.get('Rec_Date')
    if(re1 is None or re2 is None):
        messages.error(request,'Message: Fill all entries before submission')
        return render(request,'edit.html',{'details':re})
    else:
        re.Status= re1
        re.Rec_Date = re2
        re.save()
        messages.success(request,' Status Updates')
        return render(request,'edit.html')

        

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        doctorid = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        if password == password1:
            if User.objects.filter(username = doctorid).exists():
                messages.error(request,'DoctorID already present')
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username = doctorid,password = password,email = email,first_name  =first_name,last_name = last_name,)
                user.save()
                messages.success(request,'successfuly registered')
                return render(request,'login.html')
        else:
            return render(request,'register.html')


    else:
        return render(request,'register.html')
    
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Welcome Doctor  ' +username)
            return render(request,"retrive.html")
        else:
            messages.error(request,'invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def status(request):
    if 'Q' in request.GET:
       
        q = request.GET['Q']
        if len(q) != 12:
            messages.error(request,'Please enter correct number')
            return render(request,'status.html')
        else:
            p = details.objects.filter(Aadhar_number= q)
            return render(request,'status.html',{'p':p})
    else:
        return render(request,'status.html')
    
def delet(request):
    try:
        if 'Q' in request.GET:
            q = request.GET['Q']
            p = details.objects.filter(Status__icontains = q)
            return render(request,'delet.html',{'p':p})
        else:
            return render(request,'delet.html')
        
    except details.DoesNotExist:
        messages.info(request,'No data')
        return render(request,'delet.html')


def delition(request,id):
    try:
        re = details.objects.get(id =id)
        re.delete()
        messages.success(request,'deleted')
        return render(request,'delet.html')
    except details.DoesNotExist:
        messages.info(request,'No data found')
        return render(request,'delet.html')
    