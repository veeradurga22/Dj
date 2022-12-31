from xml.dom.minidom import Document
from django.urls import path,include
from django.contrib import admin
from .import views
# from django.conf.urls.static import static
# from .import settings


urlpatterns = [ 
    # path('admin/',admin.site.urls),
    path('', views.products, name='products'),
    # path('Men/',views.Men,name='Men'),
    # path('Women/',views.Women,name='Women'),
    path('Categories/<int:id>', views.Categories, name='Categories'),
    path('Login/',views.Login,name="Login"),
    path('Login_Page',views.Login_Page,name="Login_Page"),
    path('Signup/',views.Signup,name='Signup'),
    path('Signup_Page/',views.Signup_Page,name="Signup_Page"),
    path('Addcart',views.Addcart,name='Addcart'),
    path('Cart/',views.Cart,name = "Cart"),
    path('logout/',views.Logout,name="logout"),
    path('Rm_item/<int:id>',views.Rm_item,name="Rm_item"),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('address',views.address,name='address'),
    path('profile',views.profile,name='profile'),
    path('summary',views.summary,name='summary'),
    path('order',views.order,name='order'),
    path('myorders',views.myorders,name='myorders'),
    path('updateprofile',views.updateprofile,name='updateprofile'),



    # path('',include('APP.urls'))

#     path('add/', views.add, name='add'),
#     path('add/addrecord/', views.addrecord, name='addrecord'),
#     path('delete/<int:id>', views.delete, name='delete'),
#     path('update/<int:id>', views.update, name='update'),
#     path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
# 
]
    # ]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
