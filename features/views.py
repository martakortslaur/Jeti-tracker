from django.shortcuts import render
from .models import Feature

# Create your views here.
def features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})