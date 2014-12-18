from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
#from django.contrib.auth import authenticate, login, logout
from django import forms
from models import UserProfile, User, Category, Project
from forms import ProjectForm, UserForm, UserProfileForm
#from django.contrib.auth.decorators import login_required
from khd_projects.settings import BASE_DIR, MEDIA_URL
#import subprocess
import os
from django.utils.text import slugify
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):

    new_projects = Project.objects.all().order_by('-pub_date')[:10]
    likes_projects = Project.objects.all().order_by('-likes')[:10]

    categories = Category.objects.all()

    context = {'new_projects' : new_projects, 'likes_projects' : likes_projects, 'categories' : categories}
    return render(request, 'index.html', context)

def profile_page(request, username):

    profile_user = User.objects.get(username=username)

    try:
        profile_user_profile = UserProfile.objects.get(user=profile_user)

    except:
        profile_user_profile = None

    projects = Project.objects.all()

    profile_user_projects = []
    for project in projects:
        if project.user == profile_user:
            profile_user_projects.append(project)

    context = {'profile_user_projects' : profile_user_projects, 'profile_user': profile_user, 'profile_user_profile' : profile_user_profile}


    return render(request, 'profile_page.html', context)

def category_page(request, category):

    category = Category.objects.filter(category=category)

    projects_list = Project.objects.filter(category=category).order_by('-pub_date')

    paginator = Paginator(projects_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    context = {'projects' : projects, 'category' : category[0]}

    return render(request, 'category_page.html', context)

def project_viewer(request, id, category, slug):

    project = Project.objects.get(pk=id)
    #project_html = 'content/' + user + '/' + slug + '.html'
    #filename = 'content/' + user + '/' + slug + '.ipynb'

    context = {'project' : project}

    return render(request, "project.html", context)


def like_project(request):

    if request.method == 'GET':
        project_id = request.GET['project_id']

    if project_id:
        Project.objects.filter(id=int(project_id)).update(likes=F('likes')+1)
    else:
        test='hej'

    project = Project.objects.filter(id=int(project_id))

    likes = 'Likes: ' + str(project[0].likes)

    return HttpResponse(likes)


def twitter_license(request):

    return render(request, "twitter_license.html")

def django_license(request):

    return render(request, "django_license.html")


