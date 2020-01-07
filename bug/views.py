from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from .models import bug
from .forms import AddBugForm

@login_required()
def add_bug(request):
    """
    Creates a view that allows a user to submit
    bug report
    """
    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect('bug_description', pk=bug.pk)
    else:
        form = AddBugForm()
    return render(request, "bug/addbug.html", {"form": form})

@login_required()
def show_bug(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template. Pagination is used to
    display eight bugs per page.
    """
    bugs = Bug.objects.order_by('-posted_on').all()
    paginator = Paginator(bugs, 8)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)
    return render(request, 'bug/allbug.html', {'bug': bugs})


@login_required()
def bug_description(request, pk):
    """
    This view allows a user to click on a particular
    bug to find out more details about it and add a
    comment
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    comments = Comment.objects.filter(bug=bug)
    return render(request, "bug/bugdescription.html",
                  {
                     'bug': bug, 'comments': comments
                   })