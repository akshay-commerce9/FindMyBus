from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from . forms import *


# Create your views here.
def base_home(request):
    return render(request,'basehome.html')

def home(request):
    places = Places.objects.all()
    buses = Bus.objects.all()
    return render(request, 'guesthome.html',{"places":places,"buses":buses})

def adminhome(request):
    places = Places.objects.all()
    buses = Bus.objects.all()
    if 'admin' in request.session:
        return render(request,'adminhome.html',{"places":places,"buses":buses})
    else:
        return redirect('guest_home')
def passengerhome(request):
    places = Places.objects.all()
    buses = Bus.objects.all()
    if 'user' in request.session:
        return render(request, 'passengerhome.html',{"places":places,"buses":buses})
    else:
        return redirect('guest_home')
def ownerhome(request):
    places = Places.objects.all()
    buses = Bus.objects.all()
    if 'owner' in request.session:
        return render(request, 'ownerhome.html',{"places":places,"buses":buses})
    else:
        return redirect('guest_home')
def formpage(request):
    return render(request,'registration.html')

def user_reg(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    if User_reg.objects.filter(email=email).count()>0 or Owner_reg.objects.filter(email=email).count()>0:
        messages.error(request, "User Already Exist..")
        return redirect("formpage")
    else:
        user=User_reg(name=name,email=email,password=password)
        user.save()
        messages.success(request, "User Registered Successfully..")
        return redirect("formpage")

def owner_reg(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    if Owner_reg.objects.filter(email=email).count()>0 or User_reg.objects.filter(email=email).count()>0:
        messages.error(request, "Owner Already Exist..")
        return redirect("formpage")
    else:
        owner=Owner_reg(name=name,email=email,password=password)
        owner.save()
        messages.success(request, "Owner Registered Successfully..")
        return redirect("formpage")

def login(request):
    email=request.POST['email']
    password=request.POST['password']

    check_user=User_reg.objects.filter(email=email,password=password)
    check_owner=Owner_reg.objects.filter(email=email,password=password)
    if email=="admin@gmail.com" and password=="admin":
        request.session['admin'] = email
        return redirect("adminhome")
    else:
        if check_user:
            request.session['user']=email
            return redirect("passengerhome")
        elif check_owner:
            request.session['owner']=email
            return redirect("ownerhome")
    messages.error(request, "Login Failed : Invalid Username or Password..")
    return redirect("formpage")

def logout(request):
        if 'user' in request.session:
            del request.session['user']
        elif 'admin' in request.session:
            del request.session['admin']
        else:
            del request.session['owner']
        return redirect('guest_home')

def give_complaint(request):
    numbers = Bus.objects.all()
    if request.method=="POST":
        bus_no = request.POST.get('bus_no')
        complaint = request.POST.get('complaint')
        a = Complaint(bus_no=bus_no,complaint=complaint)
        a.save()
        messages.success(request, "Complaint Submited..")
        return redirect(give_complaint)
    else:
        return render(request,"give_complaint.html",{"numbers":numbers})

def view_complaint(request):
    data=Complaint.objects.all()
    return render(request,"view_complaint.html",{'data':data})

def del_complaint(request,id):
    d=Complaint.objects.get(id=id)
    d.delete()
    return redirect("view_complaint")

def view_users(request):
    passengers=User_reg.objects.all()
    owners=Owner_reg.objects.all()
    return render(request,"view_users.html",{'passengers':passengers,'owners':owners})

def del_passenger(request,id):
    d=User_reg.objects.get(id=id)
    d.delete()
    messages.error(request, "Passenger Deleted Successfully..")
    return redirect("view_users")

def del_owner(request,id):
    d=Owner_reg.objects.get(id=id)
    d.delete()
    messages.error(request, "Owner Deleted Successfully..")
    return redirect("view_users")

def get_owner(request):
    if 'owner' in request.session:
        current_oem = request.session['owner']
        return Owner_reg.objects.get(email=current_oem)

def add_bus(request):
    if request.method=="POST":
        current_owner = get_owner(request)
        f=Busform(request.POST,request.FILES)
        if f.is_valid():
            bus_name = f.cleaned_data['bus_name']
            bus_no = f.cleaned_data['bus_no']
            bus_img = f.cleaned_data['bus_img']
            a = Bus(bus_name=bus_name,bus_no=bus_no,bus_img=bus_img,oid=current_owner)
            a.save()
            messages.success(request, "Bus Added Successfully..")
            return redirect("view_bus")
    else:
        return render(request,"add_bus.html")



def view_bus(request):
    current_owner = get_owner(request)
    data=Bus.objects.filter(oid=current_owner)
    return render(request,"view_bus.html",{"data":data})

def del_bus(request,id):
    d=Bus.objects.get(id=id)
    d.delete()
    messages.error(request, "Bus Removed Successfully..")
    return redirect("view_bus")

def add_route(request,id):
    current_bus=Bus.objects.get(id=id)
    places =Places.objects.all()
    bdata = Bus.objects.get(id=id)
    if request.method == "POST":
        stop=[]
        time=[]
        first_st = request.POST.get("first_st")
        if Places.objects.filter(place=first_st).count()==0:
            p=Places(place=first_st)
            p.save()
        last_st = request.POST.get("last_st")
        first_ti = request.POST.get("first_ti")
        last_ti = request.POST.get("last_ti")
        for i in range(1,50):
            if request.POST.get("stop_"+str(i))!=None:
                stp=request.POST.get("stop_"+str(i))
                stop.append(stp)
                if Places.objects.filter(place=stp).count() == 0:
                    p = Places(place=stp)
                    p.save()
            if request.POST.get("time_"+str(i))!=None:
                stp=request.POST.get("time_"+str(i))
                time.append(stp)
        if Places.objects.filter(place=last_st).count() == 0:
            p = Places(place=last_st)
            p.save()
        a=Route(bus_id=current_bus,first_st=first_st,stops=stop,last_st=last_st,first_ti=first_ti,times=time,last_ti=last_ti)
        a.save()
        messages.success(request,"Route Added Successfully..")
        return redirect(view_route,id)
    else:
        return render(request,"add_route.html",{"places":places,"bdata":bdata})


def view_route(request,id):
    data=Route.objects.filter(bus_id=id)
    bdata=Bus.objects.get(id=id)

    return render(request,"view_route.html",{"data":data,"bsid":id,"bdata":bdata})


def del_route(request,id,bsid):
    d=Route.objects.get(id=id)
    d.delete()
    messages.error(request,"Route Removed Successfully..")
    return redirect(view_route,bsid)

def findbus(request):
    from_st=request.POST['from']
    to_st=request.POST['to']
    routes=Route.objects.all()
    return render(request,"bus_result.html",{"from_st":from_st,"to_st":to_st,"routes":routes})

def owner_complaint(request):
    data=Complaint.objects.all()
    current_owner = get_owner(request)
    bus = Bus.objects.filter(oid=current_owner)
    return render(request,"owner_complaint.html",{'data':data,'bus':bus})

def track_bus(request):
    if request.method=="POST":
        bus_no = request.POST.get('bus_no')
    bdata = Bus.objects.get(bus_no=bus_no)
    bid=bdata.id
    data = Route.objects.filter(bus_id=bid)
    return render(request, "track_bus.html", {"data": data, "bdata": bdata})

