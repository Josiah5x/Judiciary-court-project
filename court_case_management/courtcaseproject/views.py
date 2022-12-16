from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models.query_utils import Q
from .models import Admin, ClientForm
from django.contrib.auth.models import User, auth
import datetime


# Create your views here.
def register(request):
    if request.method == 'POST':
        register = ClientForm()
        register.first_name = request.POST['firstname']
        register.middle_name = request.POST['middlename']
        register.last_name = request.POST['lastname']
        register.dateofbirth = request.POST['dateofbirth']
        register.address = request.POST['address']
        register.file_id = request.POST['fileid']
        register.complaint = request.POST['complaint']
        register.gender = request.POST['gender']
        register.date = request.POST['date']
        register.save()
    return render(request, "admindashboard.html")


def home(request):
    title = 'Log By: '
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user.is_superuser:
            return redirect('/courtcaseproject/admindashboard')
        elif user:
        
            return redirect("/home")
        else:
            print("wrong choice")
    else:
        template_name = 'index.html'
        return render(request, template_name, )

        # checkuser = Admin.objects.all()
        # for user in checkuser:
            
        #     if username == user.name and password == user.password:
        #         usersessionf = request.session['name'] = user.name
        #         # usersessionl = request.session['last_name'] = user.last_name
        #         all = ClientForm.objects.all()
                
        #         return redirect('/courtcaseproject/admindashboard', { 'title': title, 'usersessionf': usersessionf, 'all': all})
            
    # return render(request,'index.html')

def deleteUser(request, pk):
    student = ClientForm.objects.get(id=pk)
    student.delete()
    allclient = ClientForm.objects.all()
    return render(request, "allclient.html", {"allclient": allclient})
    # return render(request, "allclient.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def presearchclient(request):
    return render(request, "searchclient.html")

def adminboard(request):
    return render(request, "admindashboar.html")

    
def searchclients(request):
    if request.method == "GET":
        clientfileid = request.GET.get('clientfileid')
        print(clientfileid)
        searchclientss = ClientForm.objects.filter(Q(file_id__icontains=clientfileid))
    return render(request, "allclient.html", {'allclient': searchclientss})

def updateclient(request, pk):
    clients = ClientForm.objects.get(id=pk)
    if request.method == 'POST':
        # register = ClientForm()
        clients.first_name = request.POST['firstname']
        clients.middle_name = request.POST['middlename']
        clients.last_name = request.POST['lastname']
        clients.dateofbirth = request.POST['dateofbirth']
        clients.address = request.POST['address']
        clients.file_id = request.POST['fileid']
        clients.complaint = request.POST['complaint']
        clients.gender = request.POST['gender']
        clients.date = request.POST['date']
        clients.save()
        return redirect('/courtcaseproject/admindashboard')
    datenow = datetime.datetime.now().date()
    context33 = {'datenow': datenow, 'clients':clients}
    return render(request, "updateclient.html", context33)

def allclient(request):
    allclient = ClientForm.objects.all()
    return render(request, "allclient.html", {"allclient": allclient})

def adminboard(request):
    title = 'Login by: '

    if request.method == 'POST':
        register = ClientForm()
        register.first_name = request.POST['firstname']
        register.middle_name = request.POST['middlename']
        register.last_name = request.POST['lastname']
        register.dateofbirth = request.POST['dateofbirth']
        register.address = request.POST['address']
        register.file_id = request.POST['fileid']
        register.complaint = request.POST['complaint']
        register.gender = request.POST['gender']
        register.date = request.POST['date']
        register.save()
        return redirect('/courtcaseproject/allclient')
    countclient = ClientForm.objects.all().count()
    all = ClientForm.objects.all()[:8]
    count = all.count()
    return render(request, "admindashboard.html",  {'title':title,'all': all, 'total_client':countclient})
def services(request):
    return render(request, "services.html")

def about_us(request):
    return render(request, "about-us.html")

def contact_us(request):
    return render(request, "contact-us.html")

def portfolio(request):
    return render(request, "portfolio.html")

def blog(request):
    return render(request, "blog.html")

