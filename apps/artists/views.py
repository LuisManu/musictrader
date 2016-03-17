# Author Luis Manuel Gutierrez http://luismanu.com
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ArtistForm, GenreForm
from .models import Artist, Genre




class ArtistListView(ListView):
    model = Artist


class ArtistDetailView(DetailView):
    model = Artist

    def get_context_data(self, **kwargs):
    	context = super(ArtistDetailView, self).get_context_data(**kwargs)
    	context['albums'] = self.object.albums.all()
    	return context


class ArtistCreate(CreateView):
	model = Artist
	form_class = ArtistForm
	success_url = '/albums/add/'


class GenreCreate(CreateView):
	model = Genre
	form_class = GenreForm
	success_url = '/artists/add/'