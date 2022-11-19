sd1 => Serializer and Serializertion

sd2 => DeSerialization and Insert Data in database

sd3 => Function Based View and Class Based View - CRUD API - Long code

sd4 => Validation

sd5 => Class based Model Serializer with Validation - less code then (sd3) (serializers.py) - CRUD API

sd6 => Function Based API View - less code then (sd5 and above) - CRUD API

sd7 => Class Based APIView - less code then (sd5 and above) - CRUD API

sd8 = > GenericAPIView and Model Mixins - less code then (sd6,sd7 and above) - CRUD API

sd9, sd10 => Concrete View Class - CRUD API - Short Code - Less then all above code

=====================================================================================

sd11 => ViewSet CRUD API

sd12 => ModelViewSet CRUD API - Less then all above code in 3 lines

=======================================================================================
Class Based API CRUD Authentication and Permission
sd13 => Basic Authentication and Permission Class
        [IsAuthenticated,AllowAny, IsAdminUser] set globally and localy
        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

sd14 => Session Authentication and Permission
        [IsAuthenticated,AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly]
        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

sd15 => Custom Permission
        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

========================================================================================
Function Based API CRUD Authentication and Permission
sd16 => Authentication and Permission in Function Based View

========================================================================================
Class Based Token Authentication
sd17 => Token Authentication
     >>> 4 Methods of Token Generate
        1 > Generate Token using Admin Application
        2 > Generate Token using Command Line - python manage.py drf_create_token username
        3 > Generate Token by exposing an API Endpoint/ How Client can ask or Create Token
                urls.py > from rest_framework.authtoken.views import obtain_auth_token - urlpatterns = [ ... path('get-token/', obtain_auth_token) ]
                install httpie for Post request in Command line
                http POST http://127.0.0.1:8000/get-token/ username="admin" password="admin123456"
        username: superuser, admin,       user1 
        password: superuser, admin123456, user123456

sd18 => More Customize Token Authentication - Method 3
        you may return additional user information beyond the token value Create Custom Token - auth.py

sd19 => Generate Token using Signals - Method 4
        and use Token Authentication for API CRUD
        Get > http http://127.0.0.1:8000/studentapi/ 'Authorization: Token fb982d475532417476e3be6126c3452af4a00e90'
        Post > http -f POST http://127.0.0.1:8000/studentapi/ name=Adnan roll=105 city=Lahore 'Authorization: Token fb982d475532417476e3be6126c3452af4a00e90'
        PUT > http PUT http://127.0.0.1:8000/studentapi/5/ name='Adnan Ashraf' roll=105 city=Lahore 'Authorization: Token fb982d475532417476e3be6126c3452af4a00e90'
        Delete > http DELETE http://127.0.0.1:8000/studentapi/5/ 'Authorization:Token fb982d475532417476e3be6126c3452af4a00e90'

sd20 => Custom Authentication

sd21 => JSON Web Token and Simple JWT
        pip install djangorestframework-simplejwt
        in urls > from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
                path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
                path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
        
        In Terminal for Token:
                Get Toke: http POST http://127.0.0.1:8000/get-token/ username="admin" password="admin123456"
                Refresh Token: http POST http://127.0.0.1:8000/refresh-token/ refresh="token"
                Verify Token: http POST http://127.0.0.1:8000/verify-token/ token=""
        In Terminal for API CRUD:
                Get API: http http://127.0.0.1:8000/studentapi/ 'Authorization: Bearer  token'
                Post: http -f POST http://127.0.0.1:8000/studentapi/ name=Adnan roll=105 city=Lahore 'Authorization: Bearer token'
                PUT: http PUT http://127.0.0.1:8000/studentapi/5/ name='Adnan Ashraf' roll=105 city=Lahore 'Authorization: Bearer token'
                Delete: http DELETE http://127.0.0.1:8000/studentapi/5/ 'Authorization: Bearer token'

=====================================================================================
sd22 => Throttling
        for anonymous user send request pr day 
        and register user send request pr hour
        set DEFAULT_THROTTLE_CLASSES,DEFAULT_THROTTLE_RATES in setting.py
        and localy set DEFAULT_THROTTLE_CLASSES in views
        [AnonRateThrottle,UserRateThrottle]
        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

sd23 => ScopedRateThrottle
        API ke alg alg part ko Throttled krye ga

======================================================================================
Filtering and django filter
sd24 => Filtering by curren login 
sd25 => django filter by django_filters packeg 
        localy and globally
        pip install django-filter
        Then add 'django_filters' to your INSTALLED_APPS.

sd26 => Search Filter
        By default, the search parameter is named 'search', but this may be overridden with the SEARCH_PARAM setting.

        Ordering Filter

        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

=======================================================================================
sd27 => Pagination - PageNumberPagination, LimitOffsetPagination, CursorPagination
        1 >> PageNumberPagination
                globally in setting.py and localy(per view) in views.py
sd28 => 2 >> LimitOffsetPagination
                globally in setting.py and localy(per view) in views.py
sd29 => 3 >> CursorPagination

        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

========================================================================================
sd30 => Serializer Relations
        Nested Serializer

        Writable nested serializers(not work on it)
        write-operations to a nested serializer field you'll need to create create() and/or update() methods

sd31 => Hyperlinked Model Serializer
        
        username: superadmin, admin,       user1 
        password: superadmin, admin123456, user123456

=========================================================================================
crud3 => Django API Project
        API for CRUD
        Disable Browsable API in Production
                in setting.py
                REST_FRAMEWORK = {
                        'DEFAULT_RENDERER_CLASSES': [
                                'rest_framework.renderers.JSONRenderer',
                        ],
                }