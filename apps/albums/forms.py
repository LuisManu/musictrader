# Author Luis Manuel Gutierrez http://luismanu.com
from django.forms import ModelForm, Textarea, TextInput, Select, ImageField
from django import forms
from django.utils.safestring import mark_safe

from apps.artists.models import Artist

from .models import Album

class AlbumForm(ModelForm):
	image = ImageField(widget=forms.FileInput)

	class Meta:
		model = Album
		fields = ['artist', 'name', 'market',
				'condition', 'image', 'description']
		labels ={
			'name': 'Album Name'
		}
		help_texts = {
			'artist': '<a href="/artists/add/">add artist</a>'
		}
		widgets = {
			'name': TextInput(attrs={'class': 'form-control'}),
			'artist': Select(attrs={'class': 'form-control'}),
			'description': Textarea(attrs={'class': 'form-control'}),
			'condition': Select(attrs={'class': 'form-control'}),
			'market': Select(attrs={'class': 'form-control'}),
		}