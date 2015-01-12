from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from models import UserProfile, User, Category, Project, SubCategory, DifficultyLevel
from forms import ProjectForm, UserForm, UserProfileForm, CheckboxesForm, RadioboxForm, ProjectEditForm, CategoryFilterForm
from django.contrib.auth.decorators import login_required
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

    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    user_projects = Project.objects.filter(user=user)

    form = UserProfileForm()

    context = {'user' : user, 'user_profile' : user_profile, 'user_projects' : user_projects, 'form' : form}

    return render(request, 'profile_page.html', context)

@login_required
def edit_profile(request):

    user = User.objects.get(username=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.user = user
            model_instance.id = user.id
            if request.FILES:
                model_instance.picture = request.FILES['picture']
            else:
                user_profile = UserProfile.objects.filter(user=user)[0]
                model_instance.picture = user_profile.picture

            if request.POST['description']:
                model_instance.description = request.POST['description']
            else:
                user_profile = UserProfile.objects.filter(user=user)[0]
                model_instance.description = user_profile.description

            model_instance.save()

            message = 'Your edit was successful!'

            context = {'message' : message, 'model_instance' : model_instance}
            return render(request, "thanks.html", context)
    else:
        form = UserProfileForm()

    context = { 'form' : form}

    return render(request, "edit_profile.html", context)

def category_page(request, category):

    category = Category.objects.filter(category=category)

    projects = Project.objects.filter(category=category).order_by('-pub_date')

    if request.method == "POST":
        form = CategoryFilterForm(request.POST)
        if form:
            if request.POST['sub_category'] and request.POST['difficulty_level']:
                sub_category_id = request.POST['sub_category']
                difficulty_level_id = request.POST['difficulty_level']
                sub_category = SubCategory.objects.filter(pk=sub_category_id)
                difficulty_level = SubCategory.objects.filter(pk=difficulty_level_id)
                projects = Project.objects.filter(category=category).filter(sub_category=sub_category).filter(difficulty_level=difficulty_level)

            else:
                if request.POST['sub_category']:
                    sub_category_id = request.POST['sub_category']
                    sub_category = SubCategory.objects.filter(pk=sub_category_id)
                    projects = Project.objects.filter(category=category).filter(sub_category=sub_category)

                elif request.POST['difficulty_level']:
                    difficulty_level_id = request.POST['difficulty_level']
                    difficulty_level = DifficultyLevel.objects.filter(pk=difficulty_level_id)
                    projects = Project.objects.filter(category=category).filter(difficulty_level=difficulty_level)

            form = CategoryFilterForm()
            context = { 'category' : category[0], 'projects' : projects , 'form' : form}
            return render(request, "category_page.html", context)



    form = CategoryFilterForm()

    paginator = Paginator(projects, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    context = {'projects' : projects, 'category' : category[0], 'form' : form}

    return render(request, 'category_page.html', context)

def project_viewer(request, id, category, slug):

    project = Project.objects.get(pk=id)

    context = {'project' : project}

    return render(request, "project.html", context)

@login_required
def delete_projects(request):

    user = User.objects.get(username=request.user)
    user_projects = Project.objects.filter(user=user)

    if request.method == 'POST':

        choices = request.POST.getlist('choices')
        for project_id in choices:
            Project.objects.filter(id=project_id).delete()

        context = {'user' : user, 'user_projects' : user_projects}
        return render(request, 'delete_projects.html', context)

    else:
        form = CheckboxesForm()
        context = {'user' : user, 'user_projects' : user_projects, 'form' : form}
        return render(request, 'delete_projects.html', context)

@login_required
def add_project(request):

    user = User.objects.get(username=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.user = user
            model_instance.save()

            message = 'Thanks for adding a project!'

            context = {'message' : message}
            return render(request, "thanks.html", context)
    else:
        form = ProjectForm()

    context = { 'form' : form}

    return render(request, "add_project.html", context)

@login_required
def edit_project(request, id):

    project_id = int(id)
    user = User.objects.get(username=request.user)
    user_projects = Project.objects.filter(user=user)

    id_list = []
    for project in user_projects:
        id_list.append(int(project.id))

    if project_id in id_list:

        if request.method == "POST":
            form = ProjectEditForm(request.POST)

            if form.is_valid():
                Project.objects.filter(id=project_id).delete()
                model_instance = form.save(commit=False)
                model_instance.user = user
                model_instance.save()

                message = 'Your project was edited successfully!'

                context = context = {'message' : message}
                return render(request, "thanks.html", context)

            else:
                context = {'form' : form }
                return render(request, 'edit_project.html', context)

        project = Project.objects.filter(id=project_id)
        data = { 'title' : project[0].title, 'description' : project[0].description, 'article' : project[0].article }
        form = ProjectForm(initial=data)
        context = {'form' : form}
        return render(request, 'edit_project.html', context)

    else:
        message = 'You can only change you own projects!'
        context = { 'message' : message , 'id' : id, 'id_list': id_list}
        return render(request, 'thanks.html', context)

@login_required
def edit_projects_page(request):

    user = User.objects.get(username=request.user)
    user_projects = Project.objects.filter(user=user)

    form = RadioboxForm()
    context = {'user' : user, 'user_projects' : user_projects, 'form' : form, 'request' : request}
    return render(request, 'edit_projects_page.html', context)

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

def user_login(request):


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return redirect('/projects')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        context = {}
        return render(request, 'login.html', context)

@login_required
def user_logout(request):

    logout(request)

    return redirect('/projects')

def twitter_license(request):

    return render(request, "twitter_license.html")

def django_license(request):

    return render(request, "django_license.html")


