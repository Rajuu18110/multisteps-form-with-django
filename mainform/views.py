from django.shortcuts import render
from .models import studentdata, itservices, langservices, frontendchanges

# Create your views here.

def index(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        adds = request.POST['adds']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        mob = request.POST['mob']
        mail = request.POST['mail']
        dob = request.POST['dob']
        perimg = request.FILES['perimg']
        education = request.POST['education']
        field = request.POST['field']
        university = request.POST['university']
        passyr = request.POST['passyr']
        oneradio = request.POST['oneradio']
        applicationdate = request.POST['applicationdate']
        secradio = request.POST['secradio']
        itservice = request.POST.getlist('itservice[]')
        langservice = request.POST.getlist('langservice[]')
        thirdradio = request.POST['thirdradio']
        feedata = request.POST['feedata']
        
        Studentdata = studentdata(fullname=fullname, adds=adds, city=city, state=state, zip=zip, mob=mob, mail=mail, dob=dob, perimg=perimg, education=education, field=field, university=university, passyr=passyr, oneradio=oneradio, applicationdate=applicationdate, secradio=secradio, itservice=itservice, langservice=langservice, thirdradio=thirdradio, feedata=feedata)
        Studentdata.save()
        
    itsers = itservices.objects.all()
    langsers = langservices.objects.all()
    fronts = frontendchanges.objects.all()
    context = {'itsers':itsers, 'langsers':langsers, 'fronts':fronts}
    return render(request, "index.html", context)