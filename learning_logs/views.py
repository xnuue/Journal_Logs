from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logsApp/index.html')

@login_required
def topics(request):
    """This page returns all the topics entered by user. Importing the
    models module equips us with the Topic data to work with"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}      #here we store the resulting queryset from topics abob=ve in topics. Hence when context is called, topics ordered by date added will be returned.
    return render(request, 'learning_logsApp/topics.html', context)

@login_required #This tells django to run the login required function, and allow only logged in userss access to topic
def topic(request, topic_id):
    """This page returns the topic clicked and the entries under it"""
    topic = Topic.objects.get(id=topic_id)
    #make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logsApp/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        #Post data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #associates new topic with the current user or owner
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logsApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = EntryForm()
    else:
        #Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logsApp/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        #Post data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logsApp/edit_entry.html', context)
