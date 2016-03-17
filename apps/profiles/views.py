# Author Luis Manuel Gutierrez http://luismanu.com
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from .forms import UserCreateForm, UserUpdateForm
from .models import Profile




class ProfileDetailView(DetailView):

    model = Profile

    def get_context_data(self, **kwargs):
    	context = super(ProfileDetailView, self).get_context_data(**kwargs)
    	context['albums'] = self.object.albums.all()
    	return context


def custom_registration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			new_user = authenticate(username=username, password=password)
			login(request, new_user)
			return HttpResponseRedirect('/accounts/dashboard/')
	else:
		form = UserCreateForm()
	return render(request, 'registration/registration_form.html', {'form': form})



@login_required
def dashboard(request):
	user = User.objects.get(id=request.user.id)
	profile = Profile.objects.get(user=user)
	return render(request, 'profiles/dashboard.html', {'profile': profile})



class UserUpdate(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = reverse_lazy('profiles:dashboard')
    template_name = 'profiles/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(
            self.request,
            u'Your contact information was updated successfully',
        )
        return super(UserUpdate, self).form_valid(form)