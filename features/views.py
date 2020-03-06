from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Feature, FeatureComment
from django.contrib.auth.decorators import login_required
from .forms import FeatureForm, FeatureCommentForm


def features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {'features':features} )
    
@login_required()
def feature_description(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == "POST":
        
        form = FeatureCommentForm(request.POST)
        
        if form.is_valid():
            featureComment = form.save(commit=False)
            featureComment.feature = feature
            featureComment.author = request.user
            featureComment.save()
            return redirect(reverse('feature_description', kwargs={'pk': pk}))
            
    else:
        form = FeatureCommentForm()
        comments = FeatureComment.objects.filter(feature__pk=feature.pk)
        comments_total = len(comments)
        feature.views += 1
        feature.save()
        return render(request, 'featuredescription.html', {'feature':feature, 'comments':comments, 'comments_total':comments_total, 'form':form})
    
@login_required()
def add_or_edit_feature(request, id=None):

    feature =  get_object_or_404(Feature, pk=id) if id else None
    
    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)
        
        
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            return redirect('feature_description', feature.id)
            
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'create_feature.html', {'form':form})
    
@login_required() 
def delete_feature(request, id):
     feature =  get_object_or_404(Feature, pk=id) 
     feature.delete()
     return redirect('features')

