from django.contrib import admin

from .models import Course,Department,Group,User,Article, Specialization

# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Specialization)
