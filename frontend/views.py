from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import categorydb,productdb
from frontend.models import CustomerDetails
from django.contrib import messages
# Create your views here.

def firstweb(request):
    return HttpResponse("hello")
def webindex(request):
    data = categorydb.objects.all()
    return render(request,"indexweb.html",{'data':data})
def discategory(request,itemCatg):
    data = categorydb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products = productdb.objects.filter(category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }

    return render(request,"discategory.html",context)
def productdetails(request,dataid):
    datas = productdb.objects.get(id=dataid)
    data = categorydb.objects.all()
    return render(request, "product_details.html", {'dat': datas,'data':data})
def about(request):
    data = categorydb.objects.all()
    return render(request,"about_html.html",{'data':data})
def booking(request):
    data = categorydb.objects.all()
    return render(request,"bootable.html",{'data':data})
def customerlogin(request):
    data = categorydb.objects.all()
    return render(request,"customlogin.html",{'data':data})

def regdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if password==confirm_password:
            obj=CustomerDetails(username=username,email=email,password=password,confirm_password=confirm_password)
            obj.save()
            return redirect(customerlogin)
        else:
            messages.warning(request, "password and confirm password does not match")
    return render(request, "customlogin.html")
def customerlog(request):
    if request.method=='POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r,password=password_r).exists():
            data=CustomerDetails.objects.filter(username=username_r,password=password_r).values('email','id').first()
            request.session['username']=username_r
            request.session['password']=password_r


            return redirect(webindex)
        else:
            messages.warning(request,"sorry invalid user")
    return render(request,"customlogin.html")
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(webindex)
def cart(request):

    data=itemcart.objects.all()
    return render(request,"website_cart.html", {'data': data})
def cartsave(request):
    if request.method == "POST":
        pro = request.POST.get('product')
        qua = request.POST.get('qty')
        tpri = request.POST.get('totalprice')
        obj = itemcart(product=pro, quantity=qua,totalprice=tpri)
        obj.save()
        return redirect(cart)

