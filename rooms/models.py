from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractFormField
from wagtail.fields import RichTextField
from wagtail.models import Page



class RoomListingPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super(RoomListingPage, self).get_context(request)
        context['rooms'] = RoomDetailPage.objects.descendant_of(self).live()
        return context

    subpage_types = ['RoomDetailPage']


class RoomDetailPage(Page):
    price = models.PositiveIntegerField(null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    description = RichTextField(blank=True, null=True)


    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('price'),
        FieldPanel('size'),
        FieldPanel('capacity'),
    ]

    parent_page_types = [RoomListingPage]


class FormField(AbstractFormField):
    page = ParentalKey('BookingPage', related_name='form_fields', on_delete=models.CASCADE)


class BookingPage(Page):
    content_panels = Page.content_panels + [

        InlinePanel("form_fields", heading="Form fields", label="Field"),

    ]