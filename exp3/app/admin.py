from django.contrib import admin
from app.models import Cat,Owner,AccessRecord
# Register your models here.
admin.site.register(Cat)
admin.site.register(Owner)
admin.site.register(AccessRecord)