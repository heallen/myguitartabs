from django.shortcuts import render
from guitartabs.models import Song, Category
from guitartabs.forms import SongForm, CategoryForm

def index(request):
	songlist = Song.objects.all().order_by('name')
	artistlist = list(set([(song.artist, song.artist_slug) for song in songlist]))
	artistlist.sort()
	categorylist = Category.objects.all().order_by('name')
	context_dict = {'songlist': songlist, 'artistlist': artistlist, 'categorylist': categorylist}
	return render(request, 'guitartabs/index.html', context_dict)

def show_artist(request, artist_slug):
	songlist = Song.objects.filter(artist_slug = artist_slug)
	artist = songlist[0].artist
	context_dict = {'songlist': songlist, 'artist': artist}
	return render(request, 'guitartabs/show_artist.html', context_dict)

def show_category(request, category_slug):
	category = Category.objects.filter(category_slug = category_slug)[0]
	songlist = category.songs.all()
	context_dict = {'songlist': songlist, 'category': category}
	return render(request, 'guitartabs/show_category.html', context_dict)

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

def add_category(request):
	form = CategoryForm()
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'guitartabs/add_category.html', {'form': form})