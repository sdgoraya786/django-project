from django.shortcuts import render

# Create your views here.
def home(request):
    contaxt = {'home': 'active'}  # best approach for active menu link
    return render(request, 'core/home.html', contaxt)

def contact(request):
    return render(request, 'core/contact.html')