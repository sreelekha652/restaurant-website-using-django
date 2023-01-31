from django.urls import path
from frontend import views

urlpatterns=[
    path('firstweb/',views.firstweb,name="firstweb"),
    path('',views.webindex,name="webindex"),
    path('discategory/<itemCatg>',views.discategory,name="discategory"),
    path('productdetails/<int:dataid>',views.productdetails,name="productdetails"),
    path('about/',views.about,name="about"),
    path('booking/',views.booking,name="booking"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('regdata/',views.regdata,name="regdata"),
    path('customerlog/', views.customerlog, name="customerlog"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cart/',views.cart,name="cart"),




]