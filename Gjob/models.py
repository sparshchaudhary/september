from django.db import models

# Create your models here.

class GovJobPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---- by ----  ' + self.category

class BookPost1 (models.Model):
    sno = models.AutoField(primary_key=True)
    CategoryHeader1 = models.CharField(max_length=150)
    BookPost1Image1 = models.ImageField(upload_to="Index/images", default="")
    BookPost1Image2 = models.ImageField(upload_to="Index/images", default="")
    BookPost1Image3 = models.ImageField(upload_to="Index/images", default="")

class BookPost2 (models.Model):
    sno = models.AutoField(primary_key=True)
    CategoryHeader2 = models.CharField(max_length=150)
    BookPost2Image1 = models.ImageField(upload_to="Index/images", default="")
    BookPost2Image2 = models.ImageField(upload_to="Index/images", default="")
    BookPost2Image3 = models.ImageField(upload_to="Index/images", default="")

class BookPost3 (models.Model):
    sno = models.AutoField(primary_key=True)
    CategoryHeader3 = models.CharField(max_length=150)
    BookPost3Image1 = models.ImageField(upload_to="Index/images", default="")
    BookPost3Image2 = models.ImageField(upload_to="Index/images", default="")
    BookPost3Image3 = models.ImageField(upload_to="Index/images", default="")


