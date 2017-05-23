from django.db import models

class employees_company(models.Model):
	emp_name = models.CharField(max_length = 250)
	emp_age = models.CharField(max_length = 50)
	emp_gender = models.CharField(max_length = 10)
	emp_desig = models.CharField(max_length = 100)
	def __str__(self):
		return 'Name: ' +self.emp_name+ 'Age:' +self.emp_age+ 'Gender:' +self.emp_gender+ 'Designition:' +self.emp_desig+ '.'

