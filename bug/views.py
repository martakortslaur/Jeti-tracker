from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bug, Comment
from .forms import AddBugForm, AddBugCommentForm

@login_required()
def add_bug(request):

    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
        
            return redirect('bug_description', pk=bug.pk)
            # return  redirect(reverse('bug_description', kwargs={'pk': bug.pk}))
        
    else:
        form = AddBugForm()
    return render(request, "bug/addbug.html", {"form": form})

@login_required()
def show_bug(request):

    bug = Bug.objects.order_by('author').all()
    paginator = Paginator(bug, 100)
    page = request.GET.get('page', 1)
    bug = paginator.page(page)
    return render(request, 'bug/show_bug.html', {'bug': bug})


@login_required()
def bug_description(request, pk):

    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    comments = Comment.objects.filter(bug=bug)
    return render(request, "bug/bugdescription.html",
                  {
                     'bug': bug, 'comments': comments
                   })