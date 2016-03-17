# Author Luis Manuel Gutierrez http://luismanu.com
# from django.forms import ModelForm
from django.forms import ModelForm, Textarea, TextInput, Select, ImageField, FileInput
from .models import Artist, Genre




class ArtistForm(ModelForm):
	image = ImageField(widget=FileInput)

	class Meta:
		model = Artist
		fields = ['name', 'genre', 'description', 'image']
		help_texts = {
			'genre': '<a href="/artists/genre/add/">add genre</a>'
		}
		widgets = {
			'name': TextInput(attrs={'class': 'form-control'}),
			'genre': Select(attrs={'class': 'form-control'}),
			'description': Textarea(attrs={'class': 'form-control'})
		}


class GenreForm(ModelForm):
	class Meta:
		model = Genre
		fields = ['name', 'description']
		widgets = {
			'name': TextInput(attrs={'class': 'form-control'}),
			'description': Textarea(attrs={'class': 'form-control'})
		}