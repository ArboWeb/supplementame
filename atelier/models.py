from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from boutique.models import *


class AtelierPage(Page):
    template = "atelier/atelier_page.html"
    presentation = RichTextField(blank=True)

    content_panels = Page.content_panels + [InlinePanel("image_gallery", label="gallery images"),
                                            FieldPanel('presentation'),
                                            ]


class AtelierImageGallery(Orderable):
    page = ParentalKey(AtelierPage, related_name="image_gallery", on_delete=models.CASCADE)
    image = models.ForeignKey("wagtailimages.Image", related_name="+", on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption")]

