from django.db import models
from django import forms 

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet

from sortedm2m.fields import SortedManyToManyField

class AthletesIndexPage(Page):
    template = "athletes_index_page.html"
    max_count = 1

    @property
    def athletes(self):
        # Get list of live blog pages that are descendants of this page
        athlete = AthletePage.objects.live().descendant_of(self)
        team = TeamPage.objects.live().descendant_of(self)
        # Combine both querysets into one list
        athletes = list(athlete) + list(team)
        return athletes

    def get_context(self, request):
        # Get persons
        athletes = self.athletes

        # Update template context
        context = super().get_context(request)
        context['athletes'] = athletes
        return context

class AthletePage(Page):
    template = "athlete_page.html"
    parent_page_types = ['AthletesIndexPage']
    subpage_types = []

    header = models.ForeignKey("wagtailimages.Image", null=True,
                              blank=True, related_name="+", on_delete=models.SET_NULL)
    image = models.ForeignKey("wagtailimages.Image", null=True,
                              blank=True, related_name="+", on_delete=models.SET_NULL)
    
    
    teaser = models.TextField("Teaser", max_length=256, null=True, blank=True,)
    sports = models.CharField("Sportart", max_length=50, null=True, blank=True,)
    birthdate = models.DateField("Geburtstag", null=True, blank=True,)
    nationality = models.CharField("Nationalität", max_length=50, null=True, blank=True,)
    career_start = models.CharField("Karrierestart", max_length=50, null=True, blank=True,)

    bio = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("header", heading="Hero"),
                FieldPanel("image", heading="Portrait"),
            ],
            heading="Bilder",
        ),
        FieldPanel("teaser", heading="Teaser"),
        MultiFieldPanel(
            [
                FieldPanel("birthdate", heading="Geburtstag"),
                FieldPanel("nationality", heading="Nationalität"),
                FieldPanel("career_start", heading="Karrierestart"),
                FieldPanel("sports", heading="Sport"),
            ],
            heading="Fakten",
        ),
        FieldPanel("bio", heading="Bio"),
    ]

    class Meta:
        verbose_name = "Athlet"
        verbose_name_plural = "Athletes"

class TeamPage(Page):
    template = "team_page.html"
    parent_page_types = ['AthletesIndexPage']
    subpage_types = []

    header = models.ForeignKey("wagtailimages.Image", null=True,
                              blank=True, related_name="+", on_delete=models.SET_NULL)
    image = models.ForeignKey("wagtailimages.Image", null=True,
                              blank=True, related_name="+", on_delete=models.SET_NULL)

    teaser = models.TextField("Teaser", max_length=256, null=True, blank=True,)
    sports = models.CharField("Sportarten", max_length=50, null=True, blank=True,)
    foundation_year = models.CharField("Gründungsjahr", max_length=4, null=True, blank=True,)

    bio = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("header", heading="Hero"),
                FieldPanel("image", heading="Portrait"),
            ],
            heading="Bilder",
        ),
        FieldPanel("teaser", heading="Teaser"),
        MultiFieldPanel(
            [
                FieldPanel("sports", heading="Sport"),
                FieldPanel("foundation_year", heading="Gründungsjahr"),
            ],
            heading="Fakten",
        ),
        FieldPanel("bio", heading="Bio"),
    ]

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"