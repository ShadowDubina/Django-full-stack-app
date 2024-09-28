from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, UserRegistrationForm, SearchForm, \
    UserEditForm, ProfileEditForm, AnnouncementForm
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Announcement, Profile
from django.core.paginator import Paginator
from taggit.models import Tag
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.views.decorators.http import require_POST

#inputh account
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

# check authentication


# create account
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
#Create search
def announcement_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            #search similar words
            search_vector = SearchVector('title', weight='A') +\
                            SearchVector('description', weight='B')
            search_query = SearchQuery(query)
            results = Announcement.objects.annotate(search=search_vector,
                                                    rank=SearchRank(search_vector, search_query)\
                                                    ).filter(search=search_query).order_by('-rank')

    return render(request,'account/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

# announcement list
def announcement_list(request, tag_slug=None):
    announcement_list = Announcement.objects.all()
    #system of tags
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        announcement_list = announcement_list.filter(tags__in=[tag])
    # limit announcements in page
    paginator = Paginator(announcement_list, 10)
    page_number = request.GET.get('page', 1)
    announcements = paginator.page(page_number)
    return render(request, 'account/list.html', {'announcements': announcements,
                                                 'tag': tag})

# solo announcement
def announcement_detail(request, year, month, day, announcement):
    # beauty url
    announcement = get_object_or_404(Announcement, slug=announcement,
                                     publish__year=year,
                                     publish__month=month,
                                     publish__day=day)
    #list similar announcements
    announcement_tags_ids = announcement.tags.values_list('id', flat=True)
    similar_announcements = Announcement.objects.filter(tags__in=announcement_tags_ids)\
        .exclude(id=announcement.id)
    similar_announcements = similar_announcements.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags', '-publish')[:4]

    return render(request, 'account/detail.html', {'announcement': announcement,
                                                   'similar_announcements': similar_announcements})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated'\
                                      ' succesfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

#create announcement
@login_required
def announcement_create(request):
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            forma = announcement_form.save(commit=False)
            #auto stand in field author his user name
            forma.author = request.user
            forma.slug = slugify(forma.title)
            forma.save()
            announcement_form.save_m2m()
            messages.success(request, 'announcement created'\
                                      'succesfully')
        else:
            announcement_form = AnnouncementForm(request.POST)
            messages.error(request, 'Error create announcement')
    else:
        announcement_form = AnnouncementForm()
    return render(request, 'announcement/announc_create.html',
                  {'announcement_form': announcement_form})

@login_required
def profile(request):
    announcement_my = Announcement.objects.filter(author=request.user)
    return render(request, 'account/profile.html',
                  {'announcement_my': announcement_my})
