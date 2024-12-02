from django import forms
from .models import Car, Video


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class SearchCarForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
