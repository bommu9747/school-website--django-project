from django.contrib import admin

# Register your models here.
from .models import admins
from .models import teacher
from .models import students
from .models import leave
from .models import viewexamlist
from .models import mark

admin.site.register(admins)
admin.site.register(teacher)
admin.site.register(students)
admin.site.register(leave)
admin.site.register(viewexamlist)
admin.site.register(mark)