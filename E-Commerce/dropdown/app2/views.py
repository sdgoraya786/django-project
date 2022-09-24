from django.shortcuts import render
from .models import ChildCategory, Product
from django.views import View
from .forms import ProductForm
# Create your views here.

class HomeView(View):
    def get(self, request):
        fm = ProductForm()
        return render(request, 'app/h.html', {'form': fm})

def load_child_cat(request):
    print(request.GET.get('parent_category'))
    parent_category_id = request.GET.get('parent_category')
    child_cat = ChildCategory.objects.filter(parent_category_id=parent_category_id)
    return render(request, 'app/cat_dropdown_list.html', {'child_cat': child_cat})