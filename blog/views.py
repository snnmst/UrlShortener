from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner
from django.contrib import messages
from django.db.models import F, Count
from django.contrib.auth.models import User



def Sample(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

@login_required
def home(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit = False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.author = User.objects.get(id = request.user.id)
           
            NewUrl.save()
            
        else:
            form = UrlForm()
            
    return render(request, 'blog/home.html', {'form': form, 'a': a})

@login_required
def data(request):
    context = {
        'datas': short_urls.objects.all()
    }
    return render(request, 'blog/data.html', context)


# Create your views here.
