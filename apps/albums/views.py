# Author Luis Manuel Gutierrez http://luismanu.com
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from apps.profiles.models import Profile

from .forms import AlbumForm
from .models import Album

from braces.views import LoginRequiredMixin




class AlbumList(ListView):
    model = Album
    context_object_name = 'albums'


class AlbumDetail(DetailView):
    model = Album


class AlbumCreate(LoginRequiredMixin, CreateView):
	model = Album
	form_class = AlbumForm

	def form_valid(self, form):
		owner = Profile.objects.get(user=self.request.user)
		obj = form.save(commit=False)
		obj.owner = owner
		obj.save()

		return HttpResponseRedirect('/')


class AlbumUpdate(LoginRequiredMixin, UpdateView):
	model = Album
	form_class = AlbumForm
	template_name_suffix = '_update_form'
	success_url = '/'

	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object.owner.user == request.user
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			return redirect_to_login(request.get_full_path())
		return super(AlbumUpdate, self).dispatch(request, *args, **kwargs)


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('profiles:dashboard')
	success_message = "Album was deleted successfully."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(AlbumDelete, self).delete(request, *args, **kwargs)