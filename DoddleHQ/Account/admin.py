from django.contrib import admin
from Account.models import User,Project,Project_list,Card,Checklist,List_Table

# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Project_list)
admin.site.register(Card)
admin.site.register(Checklist)
admin.site.register(List_Table)