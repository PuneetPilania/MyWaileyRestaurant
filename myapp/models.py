from django.db import models

class Location(models.Model):
	loc=models.CharField(max_length=100)

	def __str__(self):
		return str(self.id)

class Restaurant(models.Model):
	location=models.ForeignKey(Location,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=200)
	r_desc=models.CharField(max_length=5000)
	discountCode=models.IntegerField(default=None)
	r_image=models.ImageField(upload_to='myapp/restaurant',default='myapp/restaurant/default.png')

	def __str__(self):
		return self.name

class Menu(models.Model):
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	dishName=models.CharField(max_length=100)
	price=models.IntegerField(default=0)
	m_desc=models.CharField(max_length=5000)
	m_image=models.ImageField(upload_to='myapp/menu',default="myapp/menu/default.png")

	def __str__(self):
		return self.dishName

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    phone=models.IntegerField(default="")

    
 
class Discount(models.Model):
	menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
	offerCode=models.IntegerField(default=None)
	offer_tnc=models.CharField(max_length=6000)
	offerPer=models.IntegerField(default=0)




