from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from boutique.models import *


class HomePage(Page):
    alaune = RichTextField(blank=True)
    actu = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        articles_vendus_page = ArticlesVendusPage.objects.live().first()
        context["articles_vendus_page"] = articles_vendus_page
        return(context)

    content_panels = Page.content_panels + [InlinePanel("image_gallery", label="gallery images"),
                                            FieldPanel('alaune'),
                                            FieldPanel('actu'),
                                            ]


class HomeImageGallery(Orderable):
    page = ParentalKey(HomePage, related_name="image_gallery", on_delete=models.CASCADE)
    image = models.ForeignKey("wagtailimages.Image", related_name="+", on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption")]
