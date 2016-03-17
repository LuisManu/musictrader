# Author Luis Manuel Gutierrez http://luismanu.com
from django.db import models




class Genre(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'


class Artist(models.Model):
	name = models.CharField(max_length=40)
	genre = models.ForeignKey(Genre)
	description = models.TextField()
	image = models.ImageField(upload_to='artists', blank=True, null=True)

	def __unicode__(self):
		return self.name