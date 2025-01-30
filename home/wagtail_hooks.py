from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from home.models import Service, Testimonial


class ServiceSnippetView(SnippetViewSet):
    model = Service
    menu_label = 'Icon Items'
    icon = 'icon'
    menu_order = 320



class TestimonialSnippetView(SnippetViewSet):
    model = Testimonial
    menu_label = 'Client Reviews'
    icon = 'reviews'
    menu_order = 330

class VillarosaViewSetGroup(SnippetViewSetGroup):
    menu_label = 'Villarosa Services'
    menu_icon = 'placeholder'
    menu_order = 300
    items = (ServiceSnippetView, TestimonialSnippetView)


register_snippet(VillarosaViewSetGroup)