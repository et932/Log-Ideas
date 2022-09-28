from email import message
from multiprocessing import get_context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from tickets.forms import LogIdeaForm
from tickets.models import LogIdeas
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import authenticate,  get_user_model
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.contrib import messages
import time
from django.template import RequestContext


@permission_required('auth.view_user')

def users_list_view(request):
    pass


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogIdeas
 
    def get_context_data(self, **kwargs):
        #super(HomeListView, self).get_context_data(**kwargs)
        context = super(HomeListView, self).get_context_data(**kwargs)
        print (super(HomeListView, self).get_context_data(**kwargs))
        return context

    def get_data(request):
        query_results = LogIdeas.objects.objects.all()
        #print (query_results)
        return query_results



    

def about(request):
    return render(request, "tickets/about.html")

def contact(request):
    return render(request, "tickets/contact.html")

def log_message(request):
    form = LogIdeaForm(request.POST)
    #descritption = DescForm(request.POST or None)
    if request.method == "POST":
    
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            messages.success(request, 'Success - Idea has been added')
            #return HttpResponseRedirect('/thanks/')
            return redirect("home")
        else:
            messages.MessageFailure(request, 'Failure - Check fields are correct')        
            
    else:
        return render(request, "tickets/log_message.html", {"form": form})
        


def delete_item(request, pk):
 
    LogIdeas.objects.filter(id=pk).delete()

    user = get_user_model()
    print('HERE',user.objects.all())

    return redirect("home")



def edit_item(request, pk):
    form = LogIdeaForm(request.POST)

    if request.method == "POST":
        
        if form.is_valid():
            LogIdeas.objects.filter(id=pk).delete()
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            messages.success(request, 'Success - Idea has been added')
            #return HttpResponseRedirect('/thanks/')
            return redirect("home")
        else:
            messages.MessageFailure(request, 'Failure - Check fields are correct') 


    else:
        return render(request, "tickets/edit_log_message.html", {"form": form})
