from django.contrib import admin
from models import UserProfile, Project, Category, SubCategory, DifficultyLevel

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(DifficultyLevel)

class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/path/to/your/tinymce_setup.js',
    ]