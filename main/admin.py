from django.contrib import admin
from main import models as m1
# Register your models here.

# Project Model Admin
#........................................
@admin.register(m1.ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ProName', 'Live_site_link', 'Github_link')
    search_fields = ('ProName',)

# Contact Model Admin
#........................................
@admin.register(m1.ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email')
    search_fields = ('name',)


# SiteDataModel Admin
#........................................
@admin.register(m1.SiteDataMOdel)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'pictures', 'text', 'email', 'contact_no')
    search_fields = ('name',)


# Education Model Admin
#........................................
@admin.register(m1.EducationModel)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'program')
    search_fields = ('degree_name',)


# UnderConstruction Model Admin
# ........................................
@admin.register(m1.underconstruction)
class UnderConstrutAdmin(admin.ModelAdmin):
    list_display = ('is_under_const','uc_duration')
    search_fields = ('is_under_const',)


@admin.register(m1.LanguagesModel)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('l_name', 'note')
    search_fields = ('l_name',)
