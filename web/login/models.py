from django.db import models

class details(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	ph = models.CharField(max_length=100)
	mail = models.EmailField()
	department = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	emp_pic = models.ImageField(upload_to = 'photo/', default = 'photo/no-img.jpg')
	resume = models.FileField(upload_to = 'resume/')
	basic = models.IntegerField(default=0)
	pf = models.IntegerField(default=0)
	esi = models.IntegerField(default=0)
	da = models.IntegerField(default=0)
	ta = models.IntegerField(default=0)
	hra = models.IntegerField(default=0)
	
	def __str__(self):
		return self.first_name