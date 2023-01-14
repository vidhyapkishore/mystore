from django.db import models
import datetime

class categories(models.Model):
    name=models.CharField(max_length=60, primary_key=True, default='none')
    @staticmethod
    def get_all_categories():
        return categories.objects.all()
  
    def __str__(self):
        return self.name

class user(models.Model):
    name=models.CharField(max_length=60, primary_key=True, default='customer')
    password=models.CharField(max_length=60, null=True)
    pic = models.ImageField(upload_to="img/profile", null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.name

    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return user.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if user.objects.filter(email=self.email):
            return True
  
        return False

class products(models.Model):
    title=models.CharField(max_length=200, primary_key=True, default='product')
    price=models.FloatField(max_length=200,null=True)
    description=models.TextField(max_length=2000,null=True)
    image=models.ImageField(max_length=200,null=True)
    image1=models.ImageField(max_length=200,null=True,default='none')
    image2=models.ImageField(max_length=200,null=True,default='none')
    image3=models.ImageField(max_length=200,null=True,default='none')
    image4=models.ImageField(max_length=200,null=True,default='none')
    image5=models.ImageField(max_length=200,null=True,default='none')
    image6=models.ImageField(max_length=200,null=True,default='none')
    category=models.ForeignKey(categories, on_delete=models.CASCADE, default=None)
    rating=models.FloatField(max_length=60, null=True)
    count=models.IntegerField( null=True)
    
    def __str__(self):
        return self.title+' '+str(self.price)
    
    @staticmethod
    def get_products_by_id(ids):
        return products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return products.objects.filter(category=category_id)
        else:
            return products.get_all_products()


class orders(models.Model):
    customer_id=models.ForeignKey(user,on_delete=models.CASCADE,default=None)
    product=models.ForeignKey(products,on_delete=models.CASCADE,default=None)
    quantity=models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer):
        return orders.objects.filter(customer_id=customer).order_by('-date')

