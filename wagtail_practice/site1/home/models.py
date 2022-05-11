from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    
    banner_title    = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'])
    banner_image    = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta      = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    ) 
    
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta')
    ]
    
    # max_count limit home to be only one unless a multisite.
    # It will disable home page to be child of its own page
    # max_count = 1
    
    template = "home_page.html"
    
    class Meta:
        
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
