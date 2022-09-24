# from distutils.log import error
# from unicodedata import name
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm

from course.models import Course,Course_Page_Title
from news.models import News
from contact.models import Contact
from blog.models import Blog,PageTitle

from django.core.paginator import Paginator

# Sending Email(2) / Email Multi Alternatives(1)
# from django.core.mail import send_mail,EmailMultiAlternatives

def home(request):

    # Sending Email(3)
    # send_mail(
    # 'Testing mail',
    # 'Here is the message.',
    # 'ashrafshahzad063@gmail.com',
    # ['naveedashraf9471763@gmail.com'],
    # fail_silently=False,
    # )

    # Email Multi Alternatives(1)
    # subject = 'Testing Mail'
    # from_email = 'ashrafshahzad063@gmail.com'
    # to = 'naveedashraf9471763@gmail.com'
    # text_msg = '<p style="text-align: center;color:#0f6ccd;">This is testing mail form <b>Mr.SD</b></p>'
    # msg = EmailMultiAlternatives(subject, text_msg, from_email, [to])
    # msg.content_subtype = "html"  # Main content is now text/html
    # msg.send()

    newsData = News.objects.all()
    data = {
        'newsData': newsData
    }
    return render(request, "index.html",data)

def newsDetails(request,slug):
    newsDetails = News.objects.get(news_slug=slug)
    return render(request, "newsdetails.html",{'news':newsDetails})

def aboutUs(request):
    # redirect page data
    # if request.method == "GET":
    #     output = request.GET['output']
    # --
    # return render(request, "about-us.html",{'output':output})
    return render(request, "about-us.html")

def blogs(request):
    blogData = Blog.objects.all()
    pagetitle = PageTitle.objects.all()
    data = {
        'blogData': blogData,
        'pagetitle': pagetitle
    }
    return render(request, "blogs.html",data)
def blogDetails(request, courseid):
    return HttpResponse(courseid)

def contact(request):
    # save form data
    msg = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Contact(contact_name=name, contact_email=email , contact_messsage=message)
        data.save()
        msg = 'ThankS For Connecting Us!'

    return render(request, "contact.html",{'msg':msg})

def courses(request):
    pagetitle = Course_Page_Title.objects.all()
    courseData = Course.objects.all()

    # Pagination  
    paginator = Paginator(courseData,2)
    page_number = request.GET.get('page')
    FinalcourseData = paginator.get_page(page_number)
    totalpage = FinalcourseData.paginator.num_pages

    # Filter
    if request.method == "GET":
        ct = request.GET.get('course_name')
        if ct != None:
            # courseData = Course.objects.filter(course_title=ct)
            courseData = Course.objects.filter(course_title__icontains=ct)
    
    data = {
        'title': pagetitle,
        'coursePage': FinalcourseData,
        'lastpage': totalpage,
        'pageslist': [n+1 for n in range(totalpage)]
    }

    return render(request, "courses.html",data)


#----------------------------------------------------------#
# ////////////////////  GET Method ////////////////////////#
#----------------------------------------------------------#    
# def userForm(request):
#     data = None
#     try:
#         # if request.method == 'get':
#         name = request.GET.get('name')
#         email = request.GET['email']
#         message = request.GET['message']
#         data = dict(name = name, email = email, message = message)
#     except:
#         pass
    
#     return render(request, "userform.html", data)


#----------------------------------------------------------#
# ////////////////////  GET Method ////////////////////////#
#----------------------------------------------------------#   
def userForm(request):
    # data = {}
    # try:
    #     if request.method == "POST":
    #         name = request.POST['name']
    #         email = request.POST['email']
    #         message = request.POST['message']
    #         # d = name +' / '+ email +' / '+ message
    #         data = {
    #             'name' : name, 
    #             'email' : email, 
    #             'message' : message
    #             }
    #         # redirect page
    #         # url = "/about-us/?output={}".format(d)
    #         # # return HttpResponseRedirect(url)
    #         # return redirect(url)
    # except:
    #     pass
    # return render(request, "userform.html", data)
    return render(request, "userform.html")


#----------------------------------------------------------#
# ////////////////////  Submit User Form ///////////////////////#
#----------------------------------------------------------#
def submitForm(request):
    data = {}
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            d = name +' / '+ email +' / '+ message
            data = {
                'name' : name, 
                'email' : email, 
                'message' : message
                }
            return HttpResponse(d)
    except:
        pass
    # return HttpResponse(request)

#----------------------------------------------------------#
# /////////////////  FORM in Django ///////////////////////#
#----------------------------------------------------------#  
def djForms(request):
    fn = usersForm()
    data = {'form':fn}
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            # message = request.POST['message']
            # d = name +' / '+ email +' / '+ message
            data = {
                'form':fn,
                'name' : name, 
                'email' : email
                }       
    except:
        pass

    return render(request, "djForms.html", data)


#----------------------------------------------------------#
# ////////////////  Build a Calculator ////////////////////#
#----------------------------------------------------------#
def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('n1'))
            n2 = eval(request.POST.get('n2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
            else:
                c = 'Invalid opr...'
    except:
        c = 'Something wrong...'

    return render(request, "calculator.html",{'c':c})

#----------------------------------------------------------#
# ////////////////  Even or Odd Number ////////////////////#
#----------------------------------------------------------#
def evenOdd(request):
    c = ''
    if request.method == "POST":
        # Manual form validation #
        if request.POST.get('n1') == "":
            return render(request, "evenodd.html",{'error':True})

        n = eval(request.POST.get('n1'))
        if n % 2 == 0:
            c = 'Even Number'
        else:
            c = 'Odd Number'

    return render(request, "evenodd.html",{'c':c})


#----------------------------------------------------------#
# ////////////////  Marksheet ////////////////////#
#----------------------------------------------------------#
def marksheet(request):
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            t = s1 + s2 + s3 + s4 + s5
            p = t * 100 / 500
            if p >= 60:
                d = 'First Division'
            elif p >= 48:
                d = 'Second Division'
            elif p >= 35:
                d = 'Third Division'
            else:
                d = 'Fail'
            data =  {
                'total': t,
                'per': p,
                'div': d
            }
            return render(request, "marksheet.html",data)
    except:
        c = 'Something wrong...'

    return render(request, "marksheet.html")