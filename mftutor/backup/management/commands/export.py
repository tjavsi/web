from django.core.management.base import BaseCommand, CommandError
from mftutor.tutor.models import *
from mftutor.activation.models import *
from mftutor.aliases.models import *
from mftutor.events.models import *
from mftutor.news.models import *
from mftutor.shirt.models import *
import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "json_of") and callable(getattr(obj, "json_of")):
            return obj.json_of()
        try:
            return list(obj)
        except TypeError:
            return json.JSONEncoder.default(self, obj)

class Command(BaseCommand):
    args = '[FILE]'
    help = 'Exports the database in json format for later import'

    # TODO: Verify right number of arguments!
    def handle(self, *args, **options):
        result = {
            'version': 1,
            'profiles': TutorProfile.objects.all(),
            'tutor': Tutor.objects.all(),
            'groups': TutorGroup.objects.all(),
            'rus_classes': RusClass.objects.all(),
            'group_leaders': TutorGroupLeader.objects.all(),
            'board_members': BoardMember.objects.all(),
            'activations': ProfileActivation.objects.all(),
            'aliases': Alias.objects.all(),
            'events': Event.objects.all(),
            'event_participants': EventParticipant.objects.all(),
            'news_posts': NewsPost.objects.all(),
            'shirt_preferences': ShirtPreference.objects.all(),
            'shirt_options': ShirtOption.objects.all(),
        }
        out = json.dumps(result, indent=2, separators=(',', ': '), cls=Encoder)
        if 1 <= len(args):
            with open(args[0], 'w') as f:
                f.write(out + '\n')
        else:
            self.stdout.write(out + '\n')
