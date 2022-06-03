from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndText(blocks.StructBlock):
    
    title    = blocks.CharBlock(max_length=100,
                                required=True,
                                help_text='Add Title')
    subtitle = blocks.TextBlock(max_length=100,
                                required=True,
                                help_text='Add Subtitle')
    class Meta:
        template = 'streams/title_and_text.html'
        icon     = 'edit'
        label    = 'Title & Text'
        

class RichBlock(blocks.RichTextBlock):
    """RichText with all the features"""
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        self.features = [
            'italic',
            'bold',
            'link'
        ]
        super().__init__(**kwargs)
    
    class Meta:
        template = 'streams/rich_block.html'
        icon     = 'edit'
        label    = 'Rich Text Block'
        
class LimitedRichBlock(blocks.RichTextBlock):
    """RichText with all the features"""
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'italic',
            'bold',
            'link'
        ]
        
    class Meta:
        template = 'streams/rich_block.html'
        icon     = 'edit'
        label    = 'Limited Rich Text Block'
        
class CardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required=True,
                             help_text='Add a Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock()),
                ('image_title', blocks.CharBlock(required=True,
                                                 help_text="Add Title To Your Image",
                                                 max_length=50)),
                ('text', blocks.TextBlock(required=False,
                                          help_text='Add Subtitle To Your Image',
                                          max_length=100)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False,
                                               help_text='If above page is selected, that will be used'))
            ]
        )
    )
    
    class Meta:
        template = 'streams/cards_block.html'
        icon     = 'edit'
        label    = 'Card Block'
        
        
class CTABlock(blocks.StructBlock):
    
    title       = blocks.CharBlock(required=True, max_length=50)      
    text        = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url  = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Learn More', max_length=70)
    
    class Meta:
        template = 'streams/cta_block.html'
        icon     = 'placeholder'
        label    = 'Call To Action'


class LinkStructValue(blocks.StructValue):
    
    def url(self):
        btn_page = self.get('button_page')
        btn_url  = self.get('button_url')
        
        if btn_page:
            return btn_page.url
        elif btn_url:
            return btn_url
        return None     
 
class ButtonBlock(blocks.StructBlock):
    
    button_page = blocks.PageChooserBlock(required=False, help_text='If selected this URL will be used first.')
    button_url  = blocks.URLBlock(required=False, help_text='If selected this URL will be used secondarily to the button page.')
    
    class Meta:
        template = 'streams/button_block.html'
        icon     = 'edit'
        label    = 'Button Block'
        value_class = LinkStructValue
        


        
        

        