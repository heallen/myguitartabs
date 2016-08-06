from django import forms
from guitartabs.models import Song, Category

class SongForm(forms.ModelForm):
	name = forms.CharField(max_length=50, label="Song Name")
	url = forms.URLField(label="Tab URL")
	artist = forms.CharField(max_length=50, label="Artist")

	class Meta:
		model = Song
		fields = ('name', 'url', 'artist')

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=50, label="Category Name")
	songs = forms.ModelMultipleChoiceField(queryset=Song.objects.all())

	class Meta:
		model = Category
		fields = ('name',)