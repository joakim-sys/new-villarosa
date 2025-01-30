from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractFormField
from wagtail.contrib.settings.models import BaseGenericSetting
from wagtail.contrib.settings.registry import register_setting

from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page, Orderable

from rooms.models import RoomDetailPage


class HomePage(Page):
    hero_heading = models.CharField(max_length=255, null=True, blank=True)
    hero_text = models.TextField(null=True, blank=True)
    hero_cta = models.CharField(max_length=255, null=True, blank=True)
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to",
    )

    hero_form_heading = models.CharField(max_length=255, null=True, blank=True)
    hero_form_button_text = models.CharField(max_length=255, null=True, blank=True)

    hero_images = StreamField([
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    about_section_title = models.CharField(max_length=255, null=True, blank=True)
    about_section_heading = models.CharField(max_length=255, null=True, blank=True)
    about_section_body = RichTextField(null=True, blank=True)
    about_section_cta = models.CharField(max_length=255, null=True, blank=True)
    about_section_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="About CTA link",
        help_text="Choose a page to link to",
    )

    about_section_images = StreamField([
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    service_section_title = models.CharField(max_length=255, null=True, blank=True)
    service_section_heading = models.CharField(max_length=255, null=True, blank=True)

    testimonial_section_title = models.CharField(max_length=255, null=True, blank=True)
    testimonial_section_heading = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_heading'),
            FieldPanel('hero_text'),
            FieldPanel('hero_cta'),
            FieldPanel('hero_cta_link'),
            FieldPanel('hero_images'),
        ], heading='Hero Section'),

        MultiFieldPanel([
            FieldPanel('about_section_title'),
            FieldPanel('about_section_heading'),
            FieldPanel('about_section_body'),
            FieldPanel('about_section_cta'),
            FieldPanel('about_section_cta_link'),
            FieldPanel('about_section_images'),

        ], heading='About Section'),

        MultiFieldPanel([
            FieldPanel('service_section_title'),
            FieldPanel('service_section_heading'),
            InlinePanel('services'),
        ], heading='Service Section'),

        MultiFieldPanel([
            FieldPanel('testimonial_section_title'),
            FieldPanel('testimonial_section_heading'),
        ], heading='Testimonial Section'),

    ]

    def get_services(self):
        return [n.service for n in self.services.select_related("service")]

    def get_rooms(self):
        return RoomDetailPage.objects.live()

    def get_reviews(self):
        return Testimonial.objects.all()


class Service(ClusterableModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceOrderable(Orderable):
    page = ParentalKey("HomePage", related_name="services")
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

    panels = [
        FieldPanel('service')
    ]


class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.client_name} - Rating: {self.rating}'
