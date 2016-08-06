from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# class Artist(models.Model):
# 	name = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.name

class Song(models.Model):
	name = models.CharField(max_length=50)
	url = models.URLField()
	artist = models.CharField(max_length=50)
	artist_slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.artist_slug = slugify(self.artist)
		super(Song, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	category_slug = models.SlugField()
	songs = models.ManyToManyField(Song)

	def save(self, *args, **kwargs):
		self.category_slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name