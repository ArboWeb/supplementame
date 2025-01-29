from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from boutique.models import *


class HomePage(Page):
    entete = RichTextField(blank=True)
    alaune = RichTextField(blank=True)
    actu = RichTextField(blank=True)

    # def get_context(self, request):
    #     context = super.get_context(request)
    #     articles = Article.objects.live().order_by("-first_published_at")
    #     context["articles"] = articles

    #     return context

    content_panels = Page.content_panels + [FieldPanel('entete'),
                                            FieldPanel('alaune'),
                                            FieldPanel('actu'),
                                            ]