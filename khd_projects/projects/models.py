import os
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

def upload_path(self, filename):

    return os.path.join('content/', self.user.username, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to=upload_path, blank=True)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    category = models.CharField(max_length=120)

    def __unicode__(self):
        return self.category

class SubCategory(models.Model):
    sub_category = models.CharField(max_length=120)

    def __unicode__(self):
        return self.sub_category

class DifficultyLevel(models.Model):
    difficulty_level = models.CharField(max_length=120)

    def __unicode__(self):
        return self.difficulty_level

class Project(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    difficulty_level = models.ForeignKey(DifficultyLevel)
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(max_length=200, blank=True)
    article = models.TextField(max_length = 60000, blank=True)
    slug = AutoSlugField(populate_from='title', unique = True)
    #slug = models.SlugField(unique=True)
    likes = models.IntegerField(default=0)


    def get_absolute_url(self):
        return "/%s/%s/" % (self.user, self.slug)

    def __unicode__(self):
        return self.title



