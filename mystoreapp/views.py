from django.shortcuts import render,redirect
from . models import products,user,orders,categories
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import requests


def index(request):
    product=products.objects.all()
    mens_product=products.objects.filter(category='mens')
    women_product=products.objects.filter(category='womens') 
    jewelery_product=products.objects.filter(category='jewelery')    
    print(jewelery_product)
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'products':product,'mproducts':mens_product,'wproducts':women_product,'jproducts':jewelery_product,'propic':profile_pic,'users':current_user[0]}
    else:
        context={'products':product,'mproducts':mens_product,'wproducts':women_product,'jproducts':jewelery_product,}
    return render(request,'index.html',context)


      

def blog(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request,'blog.html',context)
    else:
        return render(request,'blog.html')
def wishlist(request):  
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request, 'wishlist.html', context)
    else:
        return redirect('login')

def checkout(request):  
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request, 'checkout.html', context)
    else:
        return redirect('login')
def blog_detail(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0],}
        return render(request,'blog-details.html',context)
    else:
        return render(request,'blog-detail.html')
    
def contact(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request,'contact.html',context)
    else:
        return render(request,'contact.html')
    
def register(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request,'index.html',context)
    else:
        return render(request,'register.html')

def login(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request,'index.html',context)
    else:
        return render(request,'login.html')
    


def product_detail(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request,'product-details.html',context)
    else:
        return render(request,'product-details.html')
    
def shop_cart(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
        return render(request, 'shop-cart.html', context)
    else:
        return redirect('login')

def shop(request,category_name):
    current_user=None
    urlObject = request.path
    if category_name=='all':
        product=products.objects.all()
    else:
        product=products.objects.filter(category=category_name)
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'products':product,'propic':profile_pic,'users':current_user[0], 'showURL': urlObject}
    else:
        context={'products':product, 'showURL': urlObject}
    return render(request,'shop.html',context)
 
def product(request,product_name):
    current_user=None
    product=products.objects.filter(title=product_name)[0]
    if 'user' in request.session:
        current_user = request.session['user']
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        recently_viewed=None
        if 'recently_viewed' in request.session:        
            if product_name in request.session['recently_viewed']:
               request.session['recently_viewed'].remove(product_name)
            recently_viewed=products.objects.filter(id__in=request.session['recently_viewed'])
            request.session['recently_viewed'].insert(0,product_name)
            if len(request.session['recently_viewed']) >=3:
               request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed']=[product_name]
        request.session.modified=True
        return render(request,'product-details.html',{'product':product,'recently_viewed':recently_viewed,'propic':profile_pic,'users':current_user[0]})
    else:
        context={'product':product}
        return render(request,'product-details.html',context)

def submit_register(request):
    current_user=None
    if 'user' in request.session:
        current_user = request.session['user']
        
        profile_pic=user.objects.filter(name=current_user[0])[0].pic
        context={'propic':profile_pic,'users':current_user[0]}
    if request.method=='POST' and request.FILES['propic']:
        busername=request.POST.get('name')  
        if user.objects.filter(name=busername).count()>0:
            messages.error(request, 'Username Already Exists!')
            return redirect('register') 
        else:
            upassword=request.POST.get('password')
            ucpassword=request.POST.get('cpassword')
            pro=request.FILES['propic']
            if upassword==ucpassword:
                uemail=request.POST.get('email')
                user.objects.create(name=busername,email=uemail,password=upassword,pic=pro)
                messages.success(request, "Your account has been successfully created.")
                return redirect('register')
            else:
                messages.error(request, 'Invalid form submission!')
                return redirect('register')  

def submit_login(request):
    current_user=None
    upassword=request.POST.get('password')
    busername=request.POST.get('name')
    if user.objects.filter(name=busername,password=upassword).exists():
        request.session['user']=[busername]        
        profile_pic=user.objects.filter(name=busername,password=upassword)[0].pic
        current_user=request.session['user']
        return render(request,'index.html',{'users':current_user[0],'propic':profile_pic})
    else:
        messages.error(request, 'Invalid form submission!')
        return redirect('login')
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

def mail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@gmail.com',
        ['vidhyapkishore@gmail.com'],
        fail_silently=False,
    )
    return redirect('index')
