from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q, Avg, Sum, Min, Max, Count
from datetime import date, time


# Create your views here.
def home(request):
    """ Ye query set return krta he aur is query set ke ander objects hen """

    ################### All These Methods Return New QuerySets 96 ################

    st_data = Student.objects.all()

    # st_data = Student.objects.filter(marks=70)

    # st_data = Student.objects.exclude(marks=70)

    # st_data = Student.objects.order_by('name') # in ASC - unicode se order kr ga
    # st_data = Student.objects.order_by('marks') # in ASC 
    # st_data = Student.objects.order_by('-marks')  # in DESC
    # st_data = Student.objects.order_by('?')  # in RAND() ASC

    # st_data = Student.objects.order_by('id').reverse()[:3] # last 3 but in desc
    # st_data = Student.objects.order_by('-id').reverse()[4:8]
    # st_data = Student.objects.order_by('-id').reverse()[1:5] # 2,3,4,5

    # st_data = Student.objects.values() # return dict.
    # st_data = Student.objects.values('name','city')

    # st_data = Student.objects.values_list() # return tuple
    # st_data = Student.objects.values_list('id','name')
    # st_data = Student.objects.values_list('id', 'name', named=True) # for this (id=1, name='Maha') ese bna de ag
    
    # st_data = Student.objects.using('default')

    # st_data = Student.objects.dates('pass_date', 'month')


    ################## Second Tables 'Teacher' Started #####################

    # sq1 = Student.objects.values_list('id', 'name', named=True)
    # sq2 = Teacher.objects.values_list('id', 'name', named=True)
    # # st_data = sq2.union(sq1)  # select only distinct values
    # st_data = sq1.union(sq2)  # select only distinct values
    # # st_data = sq2.union(sq1, all=True)

    # sq1 = Student.objects.values_list('id', 'name', named=True)
    # sq2 = Teacher.objects.values_list('id', 'name', named=True)
    # st_data = sq2.intersection(sq1)  # select only common values

    # sq1 = Student.objects.values_list('id', 'name', named=True)
    # sq2 = Teacher.objects.values_list('id', 'name', named=True)
    # # st_data = sq2.difference(sq1)  # (sq2-sq1) select sq2 table-2 data not in sq1 table-1 data
    # st_data = sq1.difference(sq2)  # (sq1-sq2) select sq1 table-1 data not in sq2 table-2 data


    ##################### AND OR Operator ####################3

    # st_data = Student.objects.filter(pk=1) & Student.objects.filter(marks=90)
    # st_data = Student.objects.filter(pk=1, marks=90)
    # st_data = Student.objects.filter(Q(id=1) & Q(marks=90))

    # st_data = Student.objects.filter(pk=1) | Student.objects.filter(marks=90)
    # st_data = Student.objects.filter(Q(id=1) | Q(marks=90))

    print()
    print('Return :', st_data)
    print()
    print('SQL Query : ', st_data.query) # return sql query only work with query set
    data = {
        'students':st_data,
        'key': 'Return QuerySets'
    }
    return render(request, 'school/home.html', data)



"""*****************************************************************************
        QuerySet API Methods that do not return new QuerySets 97
*****************************************************************************"""
################## Retreving(Return) a single Object ####################

def home2(request):

    st_data = Student.objects.get(pk=1) # it return single unique data

    # st_data = Student.objects.first()
    # st_data = Student.objects.order_by('name').first()

    # st_data = Student.objects.last()

    # st_data = Student.objects.latest('pass_date')

    # st_data = Student.objects.earliest('pass_date') # oldest data by date

    # print(Student.objects.all().exists())
    # one_data = Student.objects.get(pk=1)
    # print(Student.objects.filter(pk=one_data.pk).exists())

    # st_data = Student.objects.create(roll_no=111, name='Atif', city='Lahore', marks=66, pass_date='2022-05-09')
    
    # st_data, created = Student.objects.get_or_create(roll_no=111, name='Atif', city='Lahore', marks=66, pass_date='2022-05-09')
    # st_data, created = Student.objects.get_or_create(roll_no=112, name='Mr.SD', city='Lahore', marks=66, pass_date='2022-05-09')
    # print()
    # print('Return :', st_data, created)

    # st_data = Student.objects.filter(id=12).update(name='MS', marks=95)
    # st_data = Student.objects.filter(marks=90).update(division='First')
    # st_data, created = Student.objects.update_or_create(id=12, name='MS', defaults={'name':'Mahi'})
    # print(created)

    # obj = [
    #     Teacher(emp_no=107, name='Ali', city='Sahiwal', salary=2000, join_date='2022-04-09'),
    #     Teacher(emp_no=108, name='Husnain', city='Multan', salary=2500, join_date='2022-02-04'),
    #     Teacher(emp_no=109, name='Mubasher', city='Lahore', salary=3000, join_date='2022-05-01')
    # ]
    # st_data = Teacher.objects.bulk_create(obj) 

    # all_stu_data = Student.objects.all()
    # for stu in all_stu_data:
    #     stu.city = 'MMMM'
    # st_data = Student.objects.bulk_update(all_stu_data['city'])

    # st_data = Student.objects.in_bulk([1,2])
    # print(st_data[1].name)
    # print(st_data[2].name)
    # st_data = Student.objects.in_bulk([])
    # st_data = Student.objects.in_bulk()
    # print(st_data)

    # st_data = Student.objects.get(pk=11).delete()
    # st_data = Student.objects.filter(marks=50).delete()
    # st_data = Student.objects.all().delete()

    # st_data = Student.objects.all()
    # print(st_data.count())

    print()
    print('Return :', st_data)

    data = {
        'students':st_data,
        'key': 'Not Return QuerySets'
    }
    return render(request, 'school/home.html', data)




"""*****************************************************************************
                    QuerySet API Field Lookups 98
*****************************************************************************"""
################## Return New QuerySets ####################

def home3(request):
    st_data = Student.objects.all()

    # st_data = Student.objects.filter(name__exact='Maha')
    # st_data = Student.objects.filter(name__iexact='maha')

    # st_data = Student.objects.filter(name__contains='ah')
    # st_data = Student.objects.filter(name__icontains='Af')

    # st_data = Student.objects.filter(name__in=['Maha','Mahi'])
    # st_data = Student.objects.filter(marks__in=[90,80])
    # st_data = Student.objects.filter(id__in=[1, 2, 5])

    # st_data = Student.objects.filter(marks__gt=70)
    # st_data = Student.objects.filter(marks__gte=70)

    # st_data = Student.objects.filter(marks__lt=70)
    # st_data = Student.objects.filter(marks__lte=70)

    # st_data = Student.objects.filter(name__startswith='S')
    # st_data = Student.objects.filter(name__istartswith='s')

    # st_data = Student.objects.filter(name__endswith='a')
    # st_data = Student.objects.filter(name__iendswith='A')
    
    # st_data = Student.objects.filter(pass_date__range=('2022-01-1', '2022-02-1'))

    # st_data = Student.objects.filter(admission_data_time__date=date(2020, 1, 1))
    # st_data = Student.objects.filter(admission_data_time__date__gte=date(2020, 1, 1))

    # st_data = Student.objects.filter(admission_data_time__year=2020) # pass_date
    # st_data = Student.objects.filter(admission_data_time__month=1)
    # st_data = Student.objects.filter(admission_data_time__day=1)
    # st_data = Student.objects.filter(admission_data_time__week=27)
    # st_data = Student.objects.filter(admission_data_time__week_day=4) # sun, mon, wen, th,fri,sat
    # st_data = Student.objects.filter(admission_data_time__quarter=1)   # month(1,2,3).1 - month(4,5,6).2 - month(7,8,9).3 - month(10,11,12).4
 
    # st_data = Student.objects.filter(admission_data_time__time=time(8,00))
    # st_data = Student.objects.filter(admission_data_time__time__gt=time(6,00))
    # st_data = Student.objects.filter(admission_data_time__hour__gt=9)
    # st_data = Student.objects.filter(admission_data_time__minute__gt=40)
    # st_data = Student.objects.filter(admission_data_time__second__gt=30)

    # st_data = Student.objects.filter(roll_no__isnull=True)
    # st_data = Student.objects.filter(roll_no__isnull=False)

    print()
    print('SQL Query : ', st_data.query)
    print()
    print('Return :', st_data)

    data = {
        'students':st_data,
        'key': 'Field Lookups'
    }
    return render(request, 'school/home.html', data)



"""*****************************************************************************
                    QuerySet API Aggregation 99
*****************************************************************************"""
################## Return a single Object(data) ####################

def home4(request):
    st_data = Student.objects.all()

    avg = st_data.aggregate(Avg('marks'))
    total = st_data.aggregate(Sum('marks'))
    minimum = st_data.aggregate(Min('marks'))
    maximum = st_data.aggregate(Max('marks'))
    totalcount = st_data.aggregate(Count('marks'))

    print('SQL Query : ', st_data.query)
    print()
    print('Return :', st_data)

    data = {
        'students':st_data,
        'avg': avg,
        'total': total,
        'minimum': minimum,
        'maximum': maximum,
        'totalcount': totalcount,
        'key': 'Aggregation'
    }
    return render(request, 'school/home.html', data)



"""*****************************************************************************
                   Q Objects 100
*****************************************************************************"""
################## Return New QuerySets ####################

def home5(request):
    # st_data = Student.objects.filter(Q(id=1) & Q(marks=90))
    # st_data = Student.objects.filter(Q(id=1) | Q(marks=80))
    # st_data = Student.objects.filter(Q(id=1) | Q(marks__in=[90,50]))
    st_data = Student.objects.filter(~Q(marks__in=[70,60,75,65,85,66]))

    print('SQL Query : ', st_data.query)
    print()
    print('Return :', st_data)

    data = {
        'students':st_data,
        'key': 'Q Objects'
    }
    return render(request, 'school/home.html', data)


"""*****************************************************************************
                   Limiting QuerySet 101
*****************************************************************************"""
################## Return New QuerySets ####################

def home6(request):
    st_data = Student.objects.all()[:5] # first 5
    # st_data = Student.objects.all()[5:10] #  6 to 10
    # st_data = Student.objects.all()[:10:2]
    # st_data = Student.objects.all()[:10:3] 

    print('SQL Query : ', st_data.query)
    print()
    print('Return :', st_data)

    data = {
        'students':st_data,
        'key': 'Limiting QuerySet'
    }
    return render(request, 'school/home.html', data)