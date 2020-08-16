from django.contrib import admin
from .models import posts,tags
from django_summernote.admin import SummernoteModelAdmin



class postsAdmin(SummernoteModelAdmin):
      summernote_fields = ('content',)
      list_display=('title','created_on','author')

admin.site.register(posts,postsAdmin)
# Register your models here.
admin.site.register(tags)
