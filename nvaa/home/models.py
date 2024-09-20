from django.db import models
from django import forms 

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    hero = models.ForeignKey("wagtailimages.Image", null=True,
                              blank=True, related_name="+", on_delete=models.SET_NULL)

    value = models.TextField("value", null=True, blank=True,)
    phone = models.CharField("Telefon", max_length=50, null=True, blank=True,)
    mail = models.CharField("E-Mail", max_length=50, null=True, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel("hero", heading="Hero"),
        MultiFieldPanel(
            [
                FieldPanel("value", heading="Werteversprechen"),
            ],
            heading="Fakten",
        ),
        MultiFieldPanel(
            [
                FieldPanel("phone", heading="Telefon"),
                FieldPanel("mail", heading="E-Mail"),
            ], heading="Kontaktinformationen",),
    ]

    class Meta:
        verbose_name = "Startseite"
