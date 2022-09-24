from django.http import HttpResponse
from django.shortcuts import render

# def simple_middleware(get_response):
#     # One-time configuration and initialization.
#     print('One-time configuration')

#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print('This is before view')

#         response = get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.
#         print('This is after view')

#         return response

#     return middleware


# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#         print('One-time configuration')

#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print('This is before view')

#         response = self.get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.
#         print('This is after view')

#         return response


# class BrotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One-time Brother configuration')
#     def __call__(self, request):
#         print('This is Brother before view')
#         response = self.get_response(request)
#         print('This is Brother after view')
#         return response

# class FatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One-time Father configuration')
#     def __call__(self, request):
#         print('This is Father before view')
#         response = self.get_response(request)
#         # response = HttpResponse('Father Respose Send.....')
#         print('This is Father after view')
#         return response

# class MotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One-time Mother configuration')
#     def __call__(self, request):
#         print('This is Mother before view')
#         response = self.get_response(request)
#         print('This is Mother after view')
#         return response

# # Middleware Hooks
# class MyProcessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(request, *args, **kwargs):
#         # return HttpResponse('This is before view')
#         return None

# class MyExceptionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request, exception):
#         msg = exception
#         msg2 = ''
#         class_name = exception.__class__.__name__
#         if class_name == 'ZeroDivisionError':
#             msg2 = exception.__class__.__name__ +' : '+'Cannot Divide by Zero...'
#         print(class_name)
#         print(msg)
#         return HttpResponse(msg2)

# class MyTemplateResponseMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_template_response(self, request, response):
#         print('Process Template Response From Middleware')
#         response.context_data['name'] = 'Sherazi Doctor'
#         print(response.template_name)
#         return response


## Site Under Construction Django 95 ##
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return render(request, 'SiteUnderConstruction/siteuc.html')

# class UnderConstructionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(request, *args, **kwargs):
#         return HttpResponse('Site Under Construction')