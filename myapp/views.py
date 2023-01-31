from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import employeedb,categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def first(request):
    return HttpResponse("HELLO")
def firstpage(request):
    return render(request, "index.html")
def addemployee(request):
    return render(request,"add_empcate.html")
def adminsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('designation')
        em = request.POST.get('email')
        ph = request.POST.get('phone number')
        img = request.FILES['image']

        obj = employeedb(name=na, designation=des, email=em,phone=ph, image=img)
        obj.save()
        return redirect(addemployee)
def displayemp(request):
    data=employeedb.objects.all()
    return render(request,"display_emp.html",{'data':data})
def editemp(request,dataid):
    data = employeedb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_emp.html", {'data': data})
def updateemp(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('designation')
        em = request.POST.get('email')
        ph = request.POST.get('phone number')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = employeedb.objects.get(id=dataid).image
        employeedb.objects.filter(id=dataid).update(name=na, designation=des, email=em,phone=ph, image=file)
        return redirect(displayemp)
def deleteemp(request,dataid):
    data = employeedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayemp)
def addcategory(request):
    return render(request,"add_category.html")
def catesave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')

        img = request.FILES['image']

        obj = categorydb(category_name=na, discription=dis,image=img)
        obj.save()
        return redirect(addcategory)
def displaycate(request):
    data=categorydb.objects.all()
    return render(request,"display_cate.html",{'data':data})
def editcate(request,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_cate.html", {'data': data})
def updatecate(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).image
        categorydb.objects.filter(id=dataid).update(category_name=na,discription=dis,image=file)
        return redirect(displaycate)
def deletecate(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycate)
def addproduct(request):
    data = categorydb.objects.all()
    return render(request,"add_product.html",{'data':data})
def productsave(request):
    if request.method == "POST":
        cate = request.POST.get('category')
        na = request.POST.get('productname')
        dis = request.POST.get('discription')
        pri = request.POST.get('productprice')
        img = request.FILES['image']

        obj = productdb(category=cate,productname=na ,discription=dis,productprice=pri,image=img)
        obj.save()
        return redirect(addproduct)
def displayproduct(request):
    data=productdb.objects.all()
    return render(request,"display_pro.html",{'data':data})
def editproduct(request,dataid):
    data = productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    print(data)
    return render(request, "edit_product.html", {'data': data,'da':da})
def updateproduct(request,dataid):
    if request.method == "POST":
        cate = request.POST.get('category')
        pn = request.POST.get('productname')
        dis = request.POST.get('discription')
        pp = request.POST.get('productprice')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(category=cate, productname=pn, discription=dis, productprice=pp, image=file)
        return redirect(displayproduct)
def deleteproduct(request,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
def adlogin(request):
    return render(request,"admin_login.html")
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(firstpage)
            else:
                return redirect(adlogin)
        else:
            return redirect(adlogin)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adlogin)


