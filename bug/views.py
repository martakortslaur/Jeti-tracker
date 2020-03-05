from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Bug, Comment
from .forms import AddBugForm, CommentForm


def allbugs(request):

    bug = Bug.objects.all().order_by('author')
    return render(request, 'show_bug.html', {'bugs': bug})


@login_required()
def show_bug(request, id):

    bug = get_object_or_404(Bug, pk=id)

    return redirect('bug_description', id=bug.pk)


@login_required()
def add_bug(request):

    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect('show_bug', id=bug.pk)
            
    else:
        form = AddBugForm()
    return render(request, "addbug.html", {"form": form})


@login_required
def add_comment_bug(request, id):
 
    bug = get_object_or_404(Bug, pk=id)
    comment = None

    # bug = Bug.objects.all()


    if request.method == "POST":
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bug = bug
            comment.save()
            
            return redirect('show_bug', id=bug.pk)
    else:
        form = CommentForm()

    return render(request, "bugcomment.html", {"form": form,
                                                "comments": comment,
                                                "bug": bug})


@login_required()
def bug_description(request, id):

    bug = get_object_or_404(Bug, pk=id)
    bug.views += 1
    bug.save()
    
    comment = Comment.objects.all()
    form = CommentForm(request.POST)

    print(comment)
    return render(request, "bugdescription.html",
                  {
                     'bug': bug, 'comments': comment, 'form': form
                   })

@login_required()
def toggle_status(request, id):
    bug = get_object_or_404(Bug, pk=id)
    if  bug.status == "done":
        bug.status = "doing"
    else:
        bug.status = "done"
    bug.save()
    return redirect('show_bug', id=bug.pk)


@login_required()
def delete_comment_bug(request, id):

    comment = get_object_or_404(Comment, pk=id)
    bug = comment.bug
    comment.delete()
    return redirect('bug_description', id=bug.pk)