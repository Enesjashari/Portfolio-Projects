from django.contrib import admin
from .models import *


# Import required resources for data import and export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Define a resource for importing and exporting StudentData model
class StudentResource(resources.ModelResource):
    class Meta:
        model = StudentData

# Create an admin class for StudentData with import and export capabilities
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

# Register the StudentData model with the custom admin class
admin.site.register(StudentData, StudentAdmin)

# Register other models directly
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Paper)
