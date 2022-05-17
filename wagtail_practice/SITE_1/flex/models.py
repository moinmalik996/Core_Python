""" DJANGO """
from django.db import models

""" WAGTAIL """
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
""" Stream Blocks """
from streams import blocks


class FlexPage(Page):
    
    # @todo and streamfields
    # content = StreamField()
    
    subtitle = models.CharField(max_length=100, default='Some Text')
    content  = StreamField(
        [
            ('Title_And_Text',    blocks.TitleAndText()),
            ('Rich_Text',         blocks.RichBlock()),
            ('LImited_Rich_Text', blocks.LimitedRichBlock()),
            ('cards',             blocks.CardBlock()),
            ('cta',               blocks.CTABlock()),
            ('button',        blocks.ButtonBlock())
        ],
        null=True,
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content')
    ]
    
    template = 'flex/flex_page.html'
    
    class Meta:
        
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'