from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from testapp1.models import Banking,District,Branch,ServiceAcctype,Services

# Register your models here.
admin.site.register(Banking)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(ServiceAcctype)
admin.site.register(Services)



# Register your models here.
