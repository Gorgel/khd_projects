from django.contrib import admin
from models import UserProfile, Project, Category, SubCategory, DifficultyLevel, FAQ, InformationArticle

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(DifficultyLevel)
admin.site.register(FAQ)
#admin.site.register(InformationArticle)

class InformationArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'id')

admin.site.register(InformationArticle, InformationArticleAdmin)