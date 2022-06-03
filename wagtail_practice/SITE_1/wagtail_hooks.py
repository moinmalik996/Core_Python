from wagtail import hooks
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)




@hooks.register('register_rich_text_features')
def register_code_styling(features):
    
    # step 1
    feature_name = 'code'
    type_        = 'CODE'
    tag          = 'code'
    
    # step 2
    control = {
        "type"        : type_,
        "label"       : '</>',
        "description" : 'Code'
    }
    
    # step 3
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )
    
    # step 4
    db_conversion = {
        "from_database_format" : {tag : InlineStyleElementHandler(type_)},
        "to_database_format"   : {"style_map" : {type_: {"element" : tag}}}
    }
    
    # step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)
    
    #step 6
    features.default_features.append(feature_name)