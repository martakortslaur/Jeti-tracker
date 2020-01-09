from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,  get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Feature
from .forms import AddFeatureForm

@login_required()
def get_features(request):
    features = Feature.objects.order_by('requested_by_id').all()
    paginator = Paginator(features, 8)
    page = request.GET.get('page', 1)
    features = paginator.page(page)
    return render(request, 'features.html', {'features': features})

@login_required()
def create_feature(request):
    """
    A view that renders a form to allow
    a user to request a feature.
    """
    if request.method == "POST":
        form = AddFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.requested_by = request.user
            feature.save()
            return redirect('get_features')
    else:
        form = AddFeatureForm()
    return render(request, 'create_feature.html', {'form': form})



