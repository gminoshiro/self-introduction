from django.contrib import admin
#↓Workだとすでに登録されてる？とエラーとなる為、Work1とした。
from .models import Experience, Profile, Work1, Experience, Education, Software, Technical

admin.site.register(Profile)
admin.site.register(Work1)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)