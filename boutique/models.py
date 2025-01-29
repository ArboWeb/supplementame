from django.db import models
from django import forms
from datetime import date

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField, RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.models import ParentalKey, ParentalManyToManyField

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField



class IndexBoutique(Page):
    description = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        articles = Article.objects.live().order_by("-first_published_at")
        context["articles"] = articles

        return context

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ]
    

@register_snippet
class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    # panels = [FieldPanel("nom")]

    class Meta:
        verbose_name_plural = 'categories article'

    def __str__(self):
        return self.nom

class ArticleCategorie(Orderable):
    page = ParentalKey('boutique.Article', related_name='categories')
    categorie = models.ForeignKey(
        'boutique.Categorie',
        on_delete=models.CASCADE,
        )

    panels = [
        FieldPanel('categorie')
        ]


class Article(Page):
    categorie = ParentalManyToManyField("boutique.Categorie", blank=True)
    description = RichTextField(blank=True)
    date = models.DateField("Date d'ajout", default=date.today)

    def main_image(self):
        thumbnail_image = self.image_gallery.first()
        if thumbnail_image:
            return thumbnail_image.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel("categorie", widget=forms.CheckboxSelectMultiple),
        FieldPanel("description"),
        InlinePanel("image_gallery", label="gallery images")
    ]


class ArticleImageGallery(Orderable):
    page = ParentalKey(Article, related_name="image_gallery", on_delete=models.CASCADE)
    image = models.ForeignKey("wagtailimages.Image", related_name="+", on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption")]