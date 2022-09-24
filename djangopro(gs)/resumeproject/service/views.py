from django.shortcuts import render

# Create your views here.
def services(request):
    contaxt = {'services': 'active'}  # best approach for active menu link
    return render(request, 'services/services.html', contaxt)