from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock


class HeroImageBlock(StructBlock):
    image = ImageChooserBlock()