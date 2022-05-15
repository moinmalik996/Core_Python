"""Flexible Page"""
from django.db import models


#Wagtail Imports
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class FlexPage(Page):
    
    template = 'flex/flex_page.html'
    
    sub_title = models.CharField(max_length=100)
    
    content_panels = Page.content_panels + [
        FieldPanel('sub_title')
    ]
    
    class Meta:
        
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'