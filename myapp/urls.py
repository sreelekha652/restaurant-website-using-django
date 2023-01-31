from django.urls import path
from myapp import views

urlpatterns=[
    path('first/',views.first,name="first"),
    path('firstpage/',views.firstpage,name="firstpage"),
    path('addemployee/',views.addemployee,name="addemployee"),
    path('adminsave/',views.adminsave,name="adminsave"),
    path('displayemp/', views.displayemp, name="displayemp"),
    path('editemp/<int:dataid>/',views.editemp,name="editemp"),
    path('updateemp/<int:dataid>/',views.updateemp,name="updateemp"),
    path('deleteemp/<int:dataid>/', views.deleteemp, name="deleteemp"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('catesave/', views.catesave, name="catesave"),
    path('displaycate/', views.displaycate, name="displaycate"),
    path('editcate/<int:dataid>/',views.editcate,name="editcate"),
    path('updatecate/<int:dataid>/', views.updatecate, name="updatecate"),
    path('deletecate/<int:dataid>/', views.deletecate, name="deletecate"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('productsave/', views.productsave, name="productsave"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('adlogin/', views.adlogin, name="adlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout")







]