
from django.db import models

# Create your models here.
class Services(models.Model):
	service_id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=30,blank=False, null=False)
	description=models.CharField(max_length=200,blank=False, null=False,help_text="Description must be exactly 127 characters long.")
	images= models.FileField(upload_to = "service")
	is_active=models.BooleanField(default=True)
	class Meta:
		ordering = ['name']
	def save(self, *args, **kwargs):
		self.name = self.name.upper()  # Convert name to uppercase
		super().save(*args, **kwargs)
	def __str__(self):
		return self.name

class Brands(models.Model):
	brand_id=models.AutoField(primary_key=True)
	brand_images= models.FileField(upload_to = "brands")
	is_active=models.BooleanField(default=True)

class RecentWorks(models.Model):
	work_id=models.AutoField(primary_key=True)
	work_images= models.FileField(upload_to = "recent_job")
	is_active=models.BooleanField(default=True)

class Contactus(models.Model):
	email= models.EmailField(max_length = 254)
	first_name = models.CharField(max_length =50)
	subject = models.CharField(max_length =500,null = True, blank =True)
	companyname = models.CharField(max_length =100,null = True, blank =True)
	mobile=models.CharField(max_length =100,null = True, blank =True)

class Testimonials(models.Model):
	t_id=models.AutoField(primary_key=True)
	testimonial_images= models.FileField(upload_to = "testimonials")
	is_active=models.BooleanField(default=True)




from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField

from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    header_image = models.ImageField(upload_to='bolog/',blank=True,null=True)
    content = RichTextField(blank=True,null=True)
    author = models.CharField(max_length=100,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from = 'title', editable = True, max_length = 260)
   
    class Meta:
        ordering = ('-created_on',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs', kwargs={"slug": self.slug})


class Feedback(models.Model):
	CUSTOMER_TYPE_CHOICES = [
		('Company', 'Company'),
		('Personal', 'Personal'),
	]

	SATISFACTION_CHOICES = [
		('Very Satisfied', 'Very Satisfied'),
		('Satisfied', 'Satisfied'),
		('Neutral', 'Neutral'),
		('Dissatisfied', 'Dissatisfied'),
		('Very Dissatisfied', 'Very Dissatisfied'),
	]

	CONDITION_CHOICES = [
		('Excellent', 'Excellent'),
		('Good', 'Good'),
		('Fair', 'Fair'),
		('Poor', 'Poor'),
	]

	FRIENDLINESS_CHOICES = [
		('Very Friendly', 'Very Friendly'),
		('Friendly', 'Friendly'),
		('Neutral', 'Neutral'),
		('Unfriendly', 'Unfriendly'),
		('Very Unfriendly', 'Very Unfriendly'),
	]

	PRICE_RATING_CHOICES = [
		('Very high', 'Very high'),
		('High', 'High'),
		('Medium', 'Medium'),
		('Low', 'Low'),
		('Very low', 'Very low'),
	]

	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES)
	service_satisfaction = models.CharField(max_length=20, choices=SATISFACTION_CHOICES)
	vehicle_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
	staff_friendliness = models.CharField(max_length=20, choices=FRIENDLINESS_CHOICES)
	price_rating = models.CharField(max_length=20, choices=PRICE_RATING_CHOICES)
	additional_feedback = models.TextField(blank=True, null=True)
	submitted_at = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)  # Ensure this line is present

	def __str__(self):
		return f'{self.name} - {self.phone}'
