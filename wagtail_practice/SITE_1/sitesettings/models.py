from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    
    facebook = models.URLField(null=True, blank=True, help_text='Add a Link')
    twitter  = models.URLField(null=True, blank=True, help_text='Add a Link')
    youtube  = models.URLField(null=True, blank=True, help_text='Add a Link')
    
    panels = [
        
        MultiFieldPanel(
            
            [
                FieldPanel('facebook'),
                FieldPanel('twitter'),
                FieldPanel('youtube')
            ],
            heading='Social Media Settings',
        )
    ]

    