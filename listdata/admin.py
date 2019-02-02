from django.contrib import admin
from listdata.models import Variable, VarType, FileData
# Register your models here.
admin.site.register(Variable)
admin.site.register(VarType)
admin.site.register(FileData)
