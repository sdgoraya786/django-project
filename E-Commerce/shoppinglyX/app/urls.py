from django.urls import path
from app import views

# 3
from django.conf import settings
from django.conf.urls.static import static

# 1 Front-End
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cat/<slug:parentCat>/<slug:childCat>/', views.CategorizedProducts, name='catproducts'),
    path('filter-data/', views.filter_data, name='filter-data'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', views.CustomerLoginView.as_view(), name='login'),
    path('accounts/logout/', views.CustomerLogoutView.as_view(), name='logout'),
    # path('accounts/logout/', views.CustomerLogoutView.as_view(next_page='login'), name='logout'),
    
    path('accounts/password_change/', views.MyChangePasswordView.as_view(), name='changepassword'),
    path('accounts/password_change_done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    
    path('accounts/password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset_done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('accounts/orders/', views.orders, name='orders'),
    path('accounts/address/', views.AddressView.as_view(), name='address'),
    path('ajax/load-city/', views.load_city, name='load_city'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('buy/', views.buy_now, name='buy-now'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
