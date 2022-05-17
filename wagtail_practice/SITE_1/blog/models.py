from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    MultiFieldPanel,
    FieldPanel,
    InlinePanel
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class BlogAuthorOderable(Orderable):
    
    page = ParentalKey('blog.BlogDetailPage', related_name='blog_authors')
    author = models.ForeignKey(
        'blog.BlogAuthor',
        on_delete=models.CASCADE,
    )
    
    panels = [
        SnippetChooserPanel('author')
    ]

class BlogAuthor(models.Model):
    name    = models.CharField(max_length=70)
    website = models.URLField(blank=True, null=True)
    image   = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )
    
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('website'),
                ImageChooserPanel('image')
            ]
        )
    ]
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Blog Author'
        verbose_name_plural = 'Blog Authors'


class BlogListingPage(RoutablePageMixin,Page):
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
    
    @route(r'^latest_posts/$', name='latest_posts')                 # name is used if we don't want to use method name 
    def latest_posts_func(self, request, *args, **kwargs):          # in the template.
        context = self.get_context(request, *args, **kwargs)
        context['latest_posts'] = BlogDetailPage.objects.live().public()[:1]
        # context['latest_posts'] = context['blog_posts'][:1]
        return render(request, 'blog/latest_posts.html', context)
    
    def get_sitemap_urls(self, request):
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url + self.reverse_subpage('latest_posts'),
                "lastmod" : (self.last_published_at or self.latest_revision_created_at),
            }
        )
        return sitemap


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
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [
            InlinePanel('blog_authors', label='Author', min_num=1, max_num=5)
            ],
            heading='Author(s)'
        )
    ]
    
    
register_snippet(BlogAuthor)
