from django import forms
from .models import Feature, FeatureComment

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields=('name','description')
        
        
        
class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields=('description',)