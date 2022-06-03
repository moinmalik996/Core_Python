from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from .models import Subscribers

class SubscribersAdmin(ModelAdmin):
    
    model = Subscribers
    menu_label = 'Subscribers'
    menu_icon = 'placeholder'
    menu_order = 290
    add_to_setting_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    
modeladmin_register(SubscribersAdmin)
    