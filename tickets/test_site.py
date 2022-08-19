from django.test import TestCase
from .models import LogIdeas
import datetime

class LogIdeaTest(TestCase):

    def test_was_published_recently_with_future_question(self):

        name = 'TestIdeaName'
        description = 'This is a test Description'
        log_date = datetime.timedelta(days=30)


