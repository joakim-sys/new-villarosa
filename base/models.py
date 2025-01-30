from django.db import models
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel, FieldRowPanel, PublishingPanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Collection
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet


class StandardPage(Page):
    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", related_name="form_fields", on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]


class GalleryPage(Page):
    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    body = RichTextField(blank=True)
    collection = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=["Root"]),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Select the image collection for this gallery.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("collection"),
    ]
    subpage_types = []


@register_setting
class GenericSettings(ClusterableModel, BaseGenericSetting):
    x_url = models.URLField(verbose_name="X URL", blank=True)
    facebook_url = models.URLField(verbose_name="facebook URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    # linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    # skype_url = models.URLField(verbose_name="Skype URL", blank=True)

    phone_number = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("phone_number"),
        FieldPanel("email"),
        FieldPanel("address"),
        MultiFieldPanel(
            [
                FieldPanel("x_url"),
                FieldPanel("facebook_url"),
                FieldPanel("instagram_url"),
                # FieldPanel("linkedin_url"),
                # FieldPanel("skype_url"),
            ],
            "Social Settings",
        ),

    ]


@register_setting
class SiteSettings(BaseSiteSetting):
    title_suffix = models.CharField(
        verbose_name="Title suffix",
        max_length=255,
        help_text="The suffix for the title meta tag e.g. ' | Villarosa'",
        default="Villarosa",
    )

    panels = [
        FieldPanel("title_suffix"),
    ]


@register_snippet
class FooterText(models.Model):
    body = RichTextField()

    panels = [
        FieldPanel("body"),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = "Footer Text"
