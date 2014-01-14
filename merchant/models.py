from django.db import models

# Create your models here.
class Cbd(models.Model):
	cbd_name = models.CharField(max_length=20)

class City(models.Model):
	city_name = models.CharField(max_length=20)

class Merchant(models.Model):
	merchant_name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255,blank=True,null=True)
	telephone = models.CharField(max_length = 50,blank=True,null=True)
	summary = models.CharField(max_length = 255,blank=True,null=True)
	create_time = models.DateField(auto_now=True)
	cbd_id = models.ForeignKey(Cbd)
	city_id = models.ForeignKey(City)

	def __str__(self):
		return 'mer_nam:%s,cbd:%s,city:%s' % (self.merchant_name,self.cbd_id,self.city_id)



