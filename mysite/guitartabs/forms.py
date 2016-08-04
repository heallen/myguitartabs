from django import forms
from guitartabs.models import Song

class SongForm(forms.ModelForm):
	name = forms.CharField(max_length=50)
	url = forms.URLField()
	artist = forms.CharField(max_length=50)

	class Meta:
		model = Song
		fields = ('name', 'url', 'artist')