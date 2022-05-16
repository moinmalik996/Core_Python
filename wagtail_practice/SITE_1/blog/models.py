from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class BlogListingPage(Page):
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='This title overrides the default Title'
    )
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]
    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our context """
        context = super().get_context(request, *args, **kwargs)
        context['blog_posts'] = BlogDetailPage.objects.live().public()
        
        return context



class BlogDetailPage(Page):
    """Blog Detail Page"""
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='This title overrides the default Title'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content  = StreamField(
    [
        ('Title_And_Text',    blocks.TitleAndText()),
        ('Rich_Text',         blocks.RichBlock()),
        ('LImited_Rich_Text', blocks.LimitedRichBlock()),
        ('cards',             blocks.CardBlock()),
        ('cta',               blocks.CTABlock())
    ],
    null=True,
    blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('image'),
        StreamFieldPanel('content')
    ]
    
    
    
