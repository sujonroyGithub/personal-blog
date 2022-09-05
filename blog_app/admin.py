from django.contrib import admin
from .models import Contact, Post
# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     list_display=[' fname' ,'lname', 'email','adress','state', 'post_code']
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id' ,'title', 'desc']
admin.site.register(Post, PostModelAdmin)

admin.site.register(Contact)
