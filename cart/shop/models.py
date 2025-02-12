from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=800)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images" , default="")

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80 , default="")
    phone = models.CharField(max_length=80 , default="")
    desc = models.CharField(max_length=800 , default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_signature = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        # return self.update_desc[0:7] + "..."
        return self.order_id
        
    
