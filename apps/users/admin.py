from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser ,profile

admin.site.register(profile)
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
   list_display = ('phone_number', 'user_name')
   ordering = ('phone_number',)

   
   def get_fieldsets(self, request, obj =None):
        if request.user.is_superuser   :
           return (

              ("اطلاعات شخصی", {"fields": ('phone_number' , 'user_name',)}),
              ("دسترسی ها", {"fields": ("is_active",'is_superuser','is_staff',)}),

           )   
        return (
            (None , {'fields':()}),
            ("اطلاعات شخصی", {"fields": ( 'user_name',)}),
    )
   
   def has_module_permission(self, request):
        return request.user.is_superuser
    

   

   def get_list_display(self, request):
      if request.user.is_superuser:
         return ('phone_number', 'user_name','is_active','is_superuser','is_staff')
      
      return ('user_name',)
   
   def get_ordering(self, request):
       if request.user.is_superuser:
          return('phone_number',)
       return('user_name',)


   def has_add_permission(self, request):
      if not request.user.is_superuser:
         return False
      return True
   
   def has_change_permission(self, request, obj = None):
      if not request.user.is_superuser:
         return False
      return True
   
   def has_delete_permission(self, request, obj = None):
       if not request.user.is_superuser:
         return False
       return True
    
   def has_view_permission(self, request, obj = None):
         if not request.user.is_superuser:
             return False
         return True
   
   def get_queryset(self, request):
      qs = super().get_queryset(request)
      if request.user.is_superuser:
         return qs 
      return qs.filter(is_superuser=False)
   
   def get_readonly_fields(self, request, obj = None):
      if not request.user.is_superuser:
         return ('is_staff', 'is_superuser')
      return ()
   
   def get_field_queryset(self, db, db_field, request):
      return super().get_field_queryset(db, db_field, request)
  
      