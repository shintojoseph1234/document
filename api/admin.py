"""
api model registration
"""
# django imports
from django.contrib import admin
# local imports
from api.models import Content, Tag

admin.site.register(Tag)
admin.site.register(Content)
