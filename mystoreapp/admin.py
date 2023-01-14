from django.contrib import admin
from . models import products,user,orders,categories
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(products)
admin.site.register(user)
admin.site.register(orders)
admin.site.register(categories)

class StudentResource(resources.ModelResource):
   class Meta:
      model = products
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource