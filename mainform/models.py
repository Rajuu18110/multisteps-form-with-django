from django.db import models
# Create your models here.

class studentdata(models.Model):
    
    fee = (
    ("yes", "yes"),
    ("no", "no"),
    )
    
    fullname = models.CharField(max_length=100)
    adds = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    mob = models.CharField(max_length=100)
    mail = models.CharField(max_length=250)
    dob = models.CharField(max_length=100, verbose_name='birth')
    perimg = models.ImageField(upload_to='media/profile_pic')
    education = models.CharField(max_length=100)
    field = models.CharField(max_length=250)
    university = models.CharField(max_length=250)
    passyr = models.CharField(max_length=100)
    oneradio = models.CharField(max_length=100, choices = fee, default = 'no')
    applicationdate = models.CharField(max_length=100)
    secradio = models.CharField(max_length=100, choices = fee, default = 'no')
    itservice = models.CharField(max_length=250)
    langservice = models.CharField(max_length=250)
    thirdradio = models.CharField(max_length=100, choices = fee, default = 'no')
    feedata = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'studentdata'
        verbose_name_plural = 'Student Details'
        

class itservices(models.Model):
    itser = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'itservices'
        verbose_name_plural = 'Checkbox IT services'

class langservices(models.Model):
    langser = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'services'
        verbose_name_plural = 'Checkbox Lang services'

class frontendchanges(models.Model):
    fevi = models.ImageField(upload_to='media/fevi')
    title = models.CharField(max_length=100)
    backgroundimg = models.ImageField(upload_to='media/backimg')
    logo = models.ImageField(upload_to='media/logo')
    mainname = models.CharField(max_length=100)
    firsttitle = models.CharField(max_length=150, verbose_name='First Page Title')
    sectitle = models.CharField(max_length=150, verbose_name='Second Page Title')
    thirdtitle = models.CharField(max_length=150, verbose_name='Third Page Title')
    forthtitle = models.CharField(max_length=150, verbose_name='Forth Page Title')
    fifthtitle = models.CharField(max_length=150, verbose_name='Fifth Page Title')
    queone = models.TextField(verbose_name='Question one')
    quesec = models.TextField(verbose_name='Question second')
    quethird = models.TextField(verbose_name='Question third')
    firstsertitle = models.CharField(max_length=100, verbose_name='Fisrt Service Title')
    secsertitle = models.CharField(max_length=100, verbose_name='Second Service Title')
    queforth = models.TextField(verbose_name='Question Forth')
    
    class Meta:
        verbose_name = 'frontendchanges'
        verbose_name_plural = 'Front-end Changes'