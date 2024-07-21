from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from articles.models import Episode

class Command(BaseCommand):
    def handle(self, *args, **options):
        # feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        # feed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
        feed = feedparser.parse("https://bengali.abplive.com/home/feed")
        podcast_title = feed.channel.link
        # podcast_image = feed.channel.image["href"]

        for item in feed.entries:
            if not Episode.objects.filter(guid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    podcast_name=podcast_title,
                    guid=item.guid,
                )
                episode.save()
        print("https://github.com/realpython/materials/tree/master/build-a-django-content-aggregator/source_code_final")
