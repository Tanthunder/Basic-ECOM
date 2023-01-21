from django.contrib import admin
from .models import Order , Products
# Register your models here.

admin.site.site_header= "E-Commerce site"
admin.site.site_title ="Shopping"
admin.site.index_title = "Manage Shopping"

#adding fields in admin panel
class ProductAdmin(admin.ModelAdmin):
    #creating custom action in admin panel
    def change_category_to_default(self,request,queryset):
        queryset.update(category = "default")
    
    #changing action name in admn action
    change_category_to_default.short_description = "Default Category"
    list_display = ('title','price','category','discount_price','description')
    search_fields = ('title','category')
    actions = (change_category_to_default,)
    fields = ('title','price') #only visible fields after selecting
    list_editable = ('price','category','discount_price','description') # making fields editable in admin page

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
