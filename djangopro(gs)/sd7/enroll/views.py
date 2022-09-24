from django.shortcuts import render

from django.core.cache import cache

## Per View Caching 87
# from django.views.decorators.cache import cache_page
# @cache_page(20)
def home(request):
    return render(request, 'enroll/course.html')
def contact(request):
    return render(request, 'enroll/course.html')

## Low Level Cache API 89
# def LowLevelCache(request):
#     mv = cache.get('movie', 'has expired')
#     if mv == 'has expired':
#         cache.set('movie', 'Ms.Maravel', 20)
#         mv = cache.get('movie')
#     return render(request, 'enroll/LowLevelCache.html', {'fm':mv})

# def LowLevelCache(request):
#     # mv = cache.get_or_set('fees', 2000, 10)
#     mv = cache.get_or_set('fees', 3000, 10, version=2)
#     return render(request, 'enroll/LowLevelCache.html', {'fm':mv})

# def LowLevelCache(request):
#     data = {'name':'SD Goraya','roll':101}
#     cache.set_many(data, 20)
#     sv = cache.get_many(data)
#     return render(request, 'enroll/LowLevelCache.html', {'stu':sv})

def LowLevelCache(request):
    # cache.delete('fees', version=2)
    # cache.delete('fees')
    # cache.delete_many(['name','roll'])
    cache.clear()
    return render(request, 'enroll/LowLevelCache.html')

## cache.incr(key, delta=1, version=None)
## cache.decr(key, delta=1, version=None)
