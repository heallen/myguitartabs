from django.shortcuts import render
from guitartabs.models import Song
from guitartabs.forms import SongForm

def index(request):
	songlist = Song.objects.all().order_by('name')
	artistlist = list(set([(song.artist, song.artist_slug) for song in songlist]))
	artistlist.sort()
	context_dict = {'songlist': songlist, 'artistlist': artistlist}
	return render(request, 'guitartabs/index.html', context_dict)

def show_artist(request, artist_slug):
	songlist = Song.objects.filter(artist_slug = artist_slug)
	artist = songlist[0].artist
	context_dict = {'songlist': songlist, 'artist': artist}
	return render(request, 'guitartabs/show_artist.html', context_dict)

def add_song(request):
	form = SongForm()
	if request.method == "POST":
		form = SongForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'guitartabs/add_song.html', {'form': form})