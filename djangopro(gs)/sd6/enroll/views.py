from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
"""*****************************************************
                        Cookies 81
*****************************************************"""
# def setcookie(request):
#     response = render(request, 'enroll/cookie/setcookie.html')  # response obect any names
#     # response.set_cookie('name','SD Goraya', max_age=60)  # max_age=60 in seconds
#     response.set_cookie('name','SD Goraya', expires=datetime.utcnow()+timedelta(days=2))  
#     return response

# def getcookie(request):
#     # name = request.COOKIES['name']  # it return error if name cookie not set
#     # name = request.COOKIES.get('name')  # it return None if name cookie not set
#     # name = request.COOKIES.get('name', 'MS')  # it return default value if name cookie not set
#     name = request.COOKIES.get('name', 'Guest')  # it return default value if name cookie not set
#     return render(request, 'enroll/cookie/getcookie.html', {'name':name})

# def delcookie(request):
#     response = render(request, 'enroll/cookie/delcookie.html')  # response obect any names
#     response.delete_cookie('name')
#     return response




"""*****************************************************
                    Signed Cookies 81
*****************************************************"""

def setcookie(request):
    response = render(request, 'enroll/signedcookie/setcookie.html')  # response obect any names
    # response.set_signed_cookie('name', 'SD Goraya', salt='name', max_age=60)  # max_age=60 in seconds
    response.set_signed_cookie('name', 'SD Goraya', salt='name', expires=datetime.utcnow()+timedelta(days=2))  
    return response

def getcookie(request):
    name = request.get_signed_cookie('name', default='Guest' ,salt='name')
    return render(request, 'enroll/signedcookie/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'enroll/signedcookie/delcookie.html')  # response obect any names
    response.delete_cookie('name')
    return response



"""*******************************************************************
----------------------------------------------------------------------
*******************************************************************"""


"""*******************************************************************
                    Session Framework 82
*******************************************************************"""
''''''''''''''''''''' Database_backend Session '''''''''''''''''''''
# def setsession(request):
#     request.session['fname'] = 'M'
#     request.session['lname'] = 'SD Goraya'
#     return render(request, 'enroll/session/setsession.html')

# def getsession(request):
#     # name = request.session['name']
#     fname = request.session.get('fname', default='Guest')
#     lname = request.session.get('lname', default='Guest')
# ##  Session Methods - keys(), items(), setDefault(), clear(), flush() ##
#     keys = request.session.keys() # only return keys
#     items = request.session.items() # return keys and value
#     age = request.session.setdefault('age','26') # if key not in session then it set and get
#     return render(request, 'enroll/session/getsession.html', {'fname':fname, 'lname':lname, 'keys':keys, 'items':items, 'age':age})


# def delsession(request):
#     # if 'fname' and 'lname' in request.session:
#     #     del request.session['fname']
#     #     del request.session['lname']
#     #     return render(request, 'enroll/session/delsession.html')
#     # else:
#     #     return HttpResponse('Seesion already deleted...')

#     request.session.flush()
#     return render(request, 'enroll/session/delsession.html')


##---- Some more Methods - get_session_cookie_age(), set_expiry(), 
##---- get_expiry_age(), get_expiry_date(), get_rxpire_at_browser_close(), clear_expired()
# def setsession(request):
#     request.session['name'] = 'M SD Goraya'
#     # request.session.set_expiry(60)
#     # request.session.set_expiry(0) # session expir on browser close 
#     return render(request, 'enroll/session/setsession.html')

# def getsession(request):
#     # name = request.session['name']
#     name = request.session.get('name', default='Guest')
#     return render(request, 'enroll/session/getsession.html', {'name':name})


# def delsession(request):
#     # request.session.flush()
#     request.session.clear_expired()
#     return render(request, 'enroll/session/delsession.html')


## ----- Check Browser support Cookie - set_test_cookie(), 
## ----- test_cookie_worked(), delete_test_cookie()
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'enroll/session/testcookie/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'enroll/session/testcookie/checktestcookie.html')


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'enroll/session/testcookie/deltestcookie.html')




"""*******************************************************************
----------------------------------------------------------------------
*******************************************************************"""


"""*******************************************************************
                    Page Session Expired if not modifie 83
*******************************************************************"""
# def setsession(request):
#     request.session['name'] = 'M SD Goraya'
#     return render(request, 'enroll/PageSessionExpired/setsession.html')

# def getsession(request):
#     if 'name' in request.session:
#         name = request.session['name']
#         request.session.modified = True
#         return render(request, 'enroll/PageSessionExpired/getsession.html', {'name':name})
#     else:
#         return HttpResponse('491 - Your Session has Expired....')


# def delsession(request):
#     # request.session.flush()
#     request.session.clear_expired()
#     return render(request, 'enroll/PageSessionExpired/delsession.html')



"""*******************************************************************
----------------------------------------------------------------------
*******************************************************************"""

"""*******************************************************************
                    File Based Session 84
*******************************************************************"""
def setsession(request):
    request.session['name'] = 'M SD Goraya'
    return render(request, 'enroll/PageSessionExpired/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'enroll/PageSessionExpired/getsession.html', {'name':name})
    else:
        return HttpResponse('491 - Your Session has Expired....')


def delsession(request):
    # request.session.flush()
    request.session.clear_expired()
    return render(request, 'enroll/PageSessionExpired/delsession.html')