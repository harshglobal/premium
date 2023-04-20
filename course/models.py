
from django.db import models

# Create your models here.

class Course(models.Model):
    LANGUAGE_CHOICES = (
        ('English','English'),
        ('Hindi','Hindi'),
        ('Marathi','Marathi'),
    )
    name=models.CharField( max_length=250,blank=True,null=True)
    name_slug=models.SlugField(null=True)

    author=models.CharField( max_length=250,blank=True,null=True)
    author_name=models.CharField( max_length=100,blank=True,null=True)

    category = models.CharField(max_length=75,blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    discounted_price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)

    long_desc = models.TextField( max_length=2000,blank=True,null=True)
    
    course_image = models.ImageField(upload_to='CoursesImages',default='default_course.jpg',null=True)        #upload directly to media folder
    original_link = models.URLField(max_length=500,blank=True,null=True)
    created = models.DateField(auto_now_add=True,blank=True,null=True)
    updated = models.DateField(auto_now=True,blank=True,null=True)
    language = models.CharField(max_length = 20,choices = LANGUAGE_CHOICES,default = 'English',null=True)
    author_image = models.ImageField(upload_to='AuthorsImages',default='default_author.jpg',null=True)
    #upload directly to media folder

    def get_discount_percentage(self):
        return round(self.dicounted_price-self.price)/100

    def __str__(self):
        return self.name


     


