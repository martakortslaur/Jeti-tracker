from django.shortcuts import render
from .models import Bug

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