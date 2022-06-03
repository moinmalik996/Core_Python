from django.db import models
from django.shortcuts import render
from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from modelcluster.fields import ParentalKey, ParentalManyToManyField

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
        

class BlogCategory(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name='slug',
        max_length=255,
        allow_unicode=True,
        help_text='A slug to identify posts by this category'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]
    
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'
        ordering = ['name']
        
    def __str__(self):
        return self.name

    

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
        
        all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        paginator = Paginator(all_posts, 2)  # Change to 5 Per Page
        context['categories'] = BlogCategory.objects.all()
        qs = BlogDetailPage.objects.all()
        
        if request.GET.get('category'):
            category = request.GET.get('category')
            qs=qs.filter(categories__slug__exact=category)
            
            context['blog_posts'] = qs
            return context
        
        request.GET.get('page')
        page = request.GET.get('page')
        try:
            all_posts = paginator.page(page)
        except PageNotAnInteger:
            all_posts = paginator.page(1)
        except EmptyPage:
            all_posts = paginator.page(paginator.num_pages)

        context['blog_posts'] = all_posts
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
    """Parental Blog Detail Page"""
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='This title overrides the default Title'
    )
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
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
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [
            InlinePanel('blog_authors', label='Author', min_num=1, max_num=5)
            ],
            heading='Author(s)'
        ),
        MultiFieldPanel(
            [
                FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
            ],
            heading='Categories'
        )
    ]
    
    def save(self,  *args, **kwargs):
        
        key = make_template_fragment_key('post_preview', [self.id])
        cache.delete(key)
        print("I am saving changes to template fragment cache")
        print("I am saving changes to template fragment cache")
        print("I am saving changes to template fragment cache")
        return super().save(*args, **kwargs)
    

class ArticleBlogPage(BlogDetailPage):
    """
    A subclassed Article page for blog
    """
    
    template = "blog/article_blog_page.html"
    
    subtitle = models.CharField(max_length=100, 
                                blank=True, 
                                null=True)
    
    intro_image = models.ForeignKey('wagtailimages.Image',
                                    blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    help_text='This is the Intro Image')
    
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('subtitle'),
        ImageChooserPanel('banner_image'),
        ImageChooserPanel('intro_image'),
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [
            InlinePanel('blog_authors', label='Author', min_num=1, max_num=5)
            ],
            heading='Author(s)'
        ),
        MultiFieldPanel(
            [
                FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
            ],
            heading='Categories'
        )
    ]
    

class VideoArticlePage(BlogDetailPage):
    """
    A subclassed Article page for blog
    """
    template = "blog/video_article_page.html"
    
    youtube_video_id = models.CharField(max_length=100,
                                help_text='This is the video id of youtube video')
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('banner_image'),
        FieldPanel('youtube_video_id'),
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [
            InlinePanel('blog_authors', label='Author', min_num=1, max_num=5)
            ],
            heading='Author(s)'
        ),
        MultiFieldPanel(
            [
                FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
            ],
            heading='Categories'
        )
    ]
    
    
register_snippet(BlogAuthor)
register_snippet(BlogCategory)
