import requests
from django.shortcuts import render
from .models import registertable
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from .models import registertable


# Create your views here.
#funcyion name can be anyname
def login(request):
    return render(request,'login.html')
def dashboard(request):
    records = {}
    url = requests.get("https://floodinfo.000webhostapp.com/API/dashboard.php")
    data = url.json()
    print(data)
    wlvalue = data["waterlevel_value"]
    wlvalue = int(wlvalue)

    if wlvalue>300:
        records['status'] = "you need to leave the place"


        # Fetch all registered email addresses from the database
        registered_users = registertable.objects.all()
        to_emails = [user.email for user in registered_users]

        # Email Sending Logic
        email_subject = "Flood Alert - Evacuate Immediately"
        email_message = "The water level is dangerously high. Please evacuate immediately for your safety."
        # from_email = "projectprachi13@gmail.com"  # Replace with your email address
        from_email = "infoyou1234 @ gmail.com"
        send_mail(email_subject, email_message, from_email, to_emails)

    else:
        records['status'] = "you are safe"

    records['dashboard'] = data
    print(records)

    rlvalue = data["raindrop_value"]
    rlvalue = int(rlvalue)

    if rlvalue == 0:
        records['status1'] = "it's raining"
    else:
        records['status1'] = "it's not raining"

    records['dashboard'] = data
    print(records)

    ulvalue = data["ultrasonic_value"]
    ulvalue = int(ulvalue)

    if ulvalue>100:
        records['status2'] = "danger"
    else:
        records['status2'] = "safe"

    records['dashboard'] = data
    print(records)

    return render(request,'dashboard.html',records)
def register(request):
    return render(request,'pages-register.html')
def contact(request):
    return render(request,'contact.html')
def error(request):
    return render(request,'error.html')
def wl(request):
    records = {}
    url = requests.get("https://floodinfo.000webhostapp.com/API/waterlevel_sensor_fetch.php")
    data = url.json()
    records['waterlevel_sensor_fetch'] = data
    return render(request,'waterlevel.html',records)
def rl(request):
    records = {}
    url = requests.get("https://floodinfo.000webhostapp.com/API/raindrop_sensor_fetch.php")
    data = url.json()
    records['raindrop_sensor_fetch']=data
    return render(request,'raindrop.html',records)
def ul(request):
    records = {}
    url = requests.get("https://floodinfo.000webhostapp.com/API/ultrasonic_sensor_fetch.php")
    data = url.json()
    records['ultrasonic_sensor_fetch'] = data
    return render(request,'ultrasonic.html',records)



def fetchdata(request):
    if request.method == 'POST':
        username=request.POST.get("uname")
        usermail=request.POST.get("umail")
        userphone=request.POST.get("uphone")
        userpass=request.POST.get("upass")

        insertdataquery = registertable(name=username,email=usermail,phone=userphone,password=userpass)
        insertdataquery.save()
        messages.success(request,"you are registered now")
    else:
        pass
    return render(request,"pages-register.html")
def fetchlogindata(request):
    if request.method == 'POST':
        usermail = request.POST.get("umail")
        userpass = request.POST.get("upass")
        try:
            userdetails = registertable.objects.get(email=usermail,password=userpass)
            request.session["name"] = userdetails.name
            request.session["id"] = userdetails.id
            request.session.save()
        except:
            userdetails = None

        if userdetails is not None:
            return render(request,"dashboard.html")
        else:
            messages.error(request,"incorrect details")
    else:
        pass
    return render(request,"login.html")

def logout(request):
    try:
        del request.session["name"]
        del request.session["id"]
    except:
        pass
    return render(request,"login.html")