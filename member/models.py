from django.db import models

# Create your models here.
class member(models.Model):
	user_name = models.CharField(max_length = 50)
	user_pwd = models.CharField(max_length = 255)
	nick_name = models.CharField(max_length = 255,blank=True,null=True)
	head_img = models.CharField(max_length = 255,blank=True,null=True)
	telephone = models.CharField(max_length = 255,blank=True,null=True)
	qq_no = models.CharField(max_length = 20,blank=True,null=True)
	remark1 = models.CharField(max_length = 255,blank=True,null=True)
	remark2 = models.CharField(max_length = 255,blank=True,null=True)

	def __str__(self):
		return 'username:%s' % self.user_name
