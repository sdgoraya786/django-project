from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ParentCategory, ChildCategory


@login_required
def parent_cat_list(request):
    parent_cat = ParentCategory.objects.all()
    return JsonResponse({'data': [{'id': pc.id, 'name': pc.name} for pc in parent_cat]})


@login_required
def child_cat_list(request, parent_category_id):
    child_cat = ChildCategory.objects.filter(parent_category=parent_category_id)
    return JsonResponse({'data': [{'id': cc.id, 'name': cc.name} for cc in child_cat]})
