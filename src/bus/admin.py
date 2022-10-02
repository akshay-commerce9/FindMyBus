from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(User_reg),
admin.site.register(Owner_reg),
admin.site.register(Complaint),
admin.site.register(Bus),
admin.site.register(Route),
admin.site.register(Places),