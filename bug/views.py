from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bug, Comment
from .forms import AddBugForm, CommentForm


@login_required()
def show_bug(request):

    bug = Bug.objects.all().order_by('author')
    paginator = Paginator(bug, 100)
    page = request.GET.get('page', 1)
    bug = paginator.page(page)
    return render(request, 'bug/show_bug.html',  {'bug': bug})   


@login_required()
def add_bug(request):

    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()

            return redirect('bug_description', id=bug.pk)
            
    else:
        form = AddBugForm()
    return render(request, "bug/addbug.html", {"form": form})


@login_required
def add_comment_bug(request, id):
 
    bug = get_object_or_404(Bug, pk=id)

    # comment_form = CommentForm(request.POST, request.FILES)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bug = bug
            comment.save()
            
            return redirect('show_bug', pk=bug.pk)
    else:
        form = AddBugCommentForm()
    return render(request, "bug/bugcomment.html", {"form": form})


@login_required()
def bug_description(request, id):

    bug = get_object_or_404(Bug, pk=id)
    bug.views += 1
    bug.save()
    comment = Comment.objects.filter(bug=bug)
    form = CommentForm(request.POST)
    return render(request, "bug/bugdescription.html",
                  {
                     'bug': bug, 'comment': comment, 'form': form
                   })


@login_required()
def toggle_status(request, id):
    bug = get_object_or_404(Bug, pk=id)
    if  bug.status == "done":
        bug.status = "doing"
    else:
        bug.status = "done"

    bug.save()
    return redirect(show_bug)