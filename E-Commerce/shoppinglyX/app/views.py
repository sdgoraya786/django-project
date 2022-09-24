from django.shortcuts import render,redirect
from . import models as mymodel
from django.views import View
from.forms import CustomerRegistration, CustomerLogin, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm, CustomerAddAddressForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView, PasswordChangeDoneView, PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string

# 3 dynamic products --- is ko mzaeed best kro
class ProductView(View):
    def get(self, request):
        products = mymodel.Product.objects.all()
        topwears = mymodel.Product.objects.filter(child_category__child_cat__icontains="Men's top wear")
        bottomwears = mymodel.Product.objects.filter(child_category__child_cat__icontains="Men's Bottom Wear")
        mobiles = mymodel.Product.objects.filter(child_category__child_cat__icontains="Mobile")
        context = {
            'products': products,
            'topwears': topwears,
            'bottomwears': bottomwears,
            'mobiles': mobiles
        }
        return render(request, 'app/home.html', context)
# 4
class ProductDetailView(View):
    def get(self, request, pk):
        product = mymodel.Product.objects.get(pk=pk)

        # 14
        # is_exist = [p for p in mymodel.Cart.objects.filter(product=product.id) if p.user == request.user]
        # if is_exist:
        #     for cp in is_exist:
        #         print(cp.product.id)
        is_exist = False
        if request.user.is_authenticated:
            is_exist = mymodel.Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        
        context = {
            'product': product,
            'is_exist': is_exist
        }
        return render(request, 'app/productdetail.html', context)

# 5
def CategorizedProducts(request, **kwargs):
    searchBrand = request.GET.get('b')
    productbrands = mymodel.Brand.objects.filter(child_category__child_cat_slug__icontains=kwargs['childCat'])
    if searchBrand == None:
        catProducts = mymodel.Product.objects.filter(child_category__child_cat_slug__icontains=kwargs['childCat'])
    else:
        catProducts = mymodel.Product.objects.filter(child_category__child_cat_slug__icontains=kwargs['childCat']).filter(brand__name__icontains=searchBrand)
    context = {
        'parent_category':kwargs['parentCat'],
        'child_category':kwargs['childCat'],
        'catProducts': catProducts,
        'productbrands': productbrands,
    }
    return render(request, 'app/categorizedproducts.html', context)

# Filter Data
def filter_data(request):
    brands = request.GET.getlist('brand[]')
    categories = request.GET.getlist('category[]')
    allproducts = mymodel.Product.objects.all().order_by('-id')
    if len(brands)>0:
        allproducts = mymodel.Product.objects.filter(brand__id__in=brands)
    if len(categories)>0:
        allproducts = mymodel.Product.objects.filter(child_category__id__in=categories)
    t = render_to_string('app/ajax/product_list.html',{'catProducts':allproducts})
    return JsonResponse({'data':t})

# 6
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistration()
        context = {
            'form':form
        }
        return render(request, 'app/customerregistration.html', context)
    def post(self, request):
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerRegistration()
            messages.success(request, _("Your Registration Successfully Completed. Now You can Login"))
        else:
            messages.error(request, _("Please correct the error below."))
        context = {
            'form':form
        }
        return render(request, 'app/customerregistration.html', context)

# 7
class CustomerLoginView(LoginView):
    template_name='app/login.html'
    authentication_form=CustomerLogin
class CustomerLogoutView(LogoutView):
    template_name='app/logout.html'
# 8
@method_decorator(login_required, name='dispatch')
class MyChangePasswordView(PasswordChangeView):
    template_name = 'app/changepassword.html'
    form_class = MyPasswordChangeForm

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'app/password_change_done.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'app/password_reset.html'
    form_class = MyPasswordResetForm

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'app/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'app/password_reset_confirm.html'
    form_class = MySetPasswordForm

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'app/password_reset_complete.html'    

# 9
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        context = {
            'pro_active': 'btn-primary' 
        }
        return render(request, 'app/profile.html', context)

# 10
@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        # customer_address = mymodel.CustomerAddress.objects.filter(user=request.user)
        customer_address = mymodel.CustomerAddress.objects.filter(user_id=request.user.id)
        form = CustomerAddAddressForm()
        context = {
            'form':form,
            'customer_address':customer_address,
            'ad_active': 'btn-primary'
        }
        return render(request, 'app/address.html', context)

    def post(self, request):
        form = CustomerAddAddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            Zipcode = form.cleaned_data['Zipcode']
            # data = mymodel.CustomerAddress(user=request.user,name=name, state=state, city=city, address=address, Zipcode=Zipcode)
            data = mymodel.CustomerAddress(user_id=request.user.id,name=name, state=state, city=city, address=address, Zipcode=Zipcode)
            data.save()
            messages.success(request, _("New Address added."))
        return redirect('address')

# ajax load dependent city for state
def load_city(request):
    state_id = request.GET.get('state')
    city = mymodel.City.objects.filter(state_id=state_id)
    return render(request, 'app/city_dropdown_list.html', {'city': city})

# 11
@login_required
def add_to_cart(request):
    user  = request.user
    id = request.GET.get('product_id')
    product = mymodel.Product.objects.get(id=id)
    mymodel.Cart(user=user, product=product).save()
    return redirect('show_cart')

@login_required
def show_cart(request):
    user  = request.user
    cart = mymodel.Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in mymodel.Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            total_amount = amount + shipping_amount
        context = {
            'carts': cart,
            'total_cart_products': len(cart_product),
            'amount': amount,
            'shipping_amount': shipping_amount,
            'total_amount': total_amount,
        }
        return render(request, 'app/addtocart.html', context)
    else:
        return render(request, 'app/emptycart.html')

@login_required
def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = mymodel.Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in mymodel.Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            total_amount = amount + shipping_amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = mymodel.Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        # if c.quantity > 1:
        #     c.quantity -= 1
        #     c.save()
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in mymodel.Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            total_amount = amount + shipping_amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = mymodel.Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 0.0
        cart_product = [p for p in mymodel.Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            shipping_amount = 70.0
        data = {
            'amount': amount,
            'shipping_amount': shipping_amount,
            'total_amount': amount + shipping_amount,
            'total_cart_products': len(cart_product),
        }
        return JsonResponse(data)
        
# 12
@login_required
def checkout(request):
    user = request.user
    address = mymodel.CustomerAddress.objects.filter(user=user)
    cart_items = mymodel.Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 0.0
    cart_product = [p for p in mymodel.Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            shipping_amount = 70.0
        context = {
            'cart_items': cart_items,
            'address': address,
            'total_amount': amount + shipping_amount
        }
        return render(request, 'app/checkout.html', context)
    else:
        return render(request, 'app/emptycart.html')

@login_required
def payment_done(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('customerId')
        customer = mymodel.CustomerAddress.objects.get(id=id)
        cart = mymodel.Cart.objects.filter(user=user)
        for c in cart:
            mymodel.OrderPlaced(user=user, customer_address=customer, product=c.product, quantity=c.quantity).save()
            c.delete()
        return redirect('orders')
# 13
@login_required
def orders(request):
    op = mymodel.OrderPlaced.objects.filter(user=request.user)
    context = {
        'place_orders': op,
        'or_active': 'btn-primary'
    }
    return render(request, 'app/orders.html', context)

# 
@login_required
def buy_now(request):
    # firs save data in cart then redirect to checkout page
    context = {
    }
    return render(request, 'app/buynow.html', context)