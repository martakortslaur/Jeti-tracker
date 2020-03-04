from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,  get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Feature, UpvoteFeature
from django.utils import timezone
from .forms import AddFeatureForm

def get_features(request): 
    orders = Feature.objects.all().order_by('-created_date')
    feature = Feature.objects.order_by('username').all()
    paginator = Paginator(feature, 15)
    page = request.GET.get('page', 1)
    feature = paginator.page(page)
    return render(request, 'features.html', {'feature': feature, 'orders': orders})

def features(request):

    orders = Feature.objects.all().order_by('-created_date')
    return render(request, 'features.html', {'orders': orders})


@login_required()
def get_features(request):
    
    orders = Feature.objects.all().order_by('-created_date')
    feature = Feature.objects.order_by('username').all()
    paginator = Paginator(feature, 15)
    page = request.GET.get('page', 1)
    feature = paginator.page(page)
    return render(request, 'features.html', {'feature': feature, 'orders': orders})

@login_required()
def create_feature(request):

    if request.method == "POST":
        form = AddFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.username = request.user
            feature.save()
            return redirect('get_features')
    else:
        form = AddFeatureForm()
    return render(request, 'create_feature.html', {'form': form})

@login_required()
def delete_feature(request, pk):

    feature = get_object_or_404(Feature, pk=pk)
    if request.user == feature.username:
        feature.delete()
        messages.success(request, 'This feature has been deleted.')
    else:
        messages.info(request,
                      'You do not have permission to delete this feature.')
    return redirect('get_features')


