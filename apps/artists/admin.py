# Author Luis Manuel Gutierrez http://luismanu.com
from django.contrib import admin

from .models import Artist, Genre




admin.site.register(Artist)
admin.site.register(Genre)