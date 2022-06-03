from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (FieldPanel, 
                                         StreamFieldPanel, 
                                         InlinePanel,
                                         MultiFieldPanel)
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from streams import blocks

class HomePageCarouselItems(Orderable):
    page = ParentalKey('home.HomePage', related_name='carousal_items')
    carousal_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )

class HomePage(RoutablePageMixin,Page):
    
    subtitle = models.CharField(max_length=100, default='some text')
    content  = StreamField(
        [
            ('cta', blocks.CTABlock())
        ],
        null = True,
        blank = True
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('subtitle'),
                StreamFieldPanel('content'),
            ],
            heading='Page Information'
        ),
        MultiFieldPanel(
            [
                InlinePanel('carousal_items', max_num=5, min_num=1, label='Carousal Image')
            ],
            heading='Carousal Pictures'
            ) 
    ]
    template = 'new_home.html'
    
    class Meta:
        verbose_name        = 'Home Page'
        verbose_name_plural = 'Home Pages'
        

    @route(r'^subscribe/$')
    def subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, args, kwargs)
        context['special_context'] = "Hello Explicit Context"
        
        return render(request, 'home/subscribe.html', context)
    