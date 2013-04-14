# vim:set fileencoding=utf-8:
from django.db import models
from ..tutor.models import Tutor
from datetime import date, time, datetime

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    rsvp = models.BooleanField(verbose_name="Tilmelding mulig")

    def category(self):
        if u'stormøde' in self.title:
            return 'stormoede'
        if u'RKFL' in self.title:
            return 'rkfl'
        if u'RKFW' in self.title:
            return 'rkfw'
        if u'fest' in self.title:
            return 'fest'

    def __unicode__(self):
        return '[Event '+self.title+' on '+str(self.start_date)+']'

    class Meta:
        ordering = ['start_date', 'start_time']
        verbose_name = 'begivenhed'
        verbose_name_plural = verbose_name + 'er'

    def json_of(self):
        return {
            'title': self.title,
            'description': self.description,
            'start_date': date.strftime(self.start_date, '%Y-%m-%d') if self.start_date else None,
            'start_time': time.strftime(self.start_time, '%H:%M:%S') if self.start_time else None,
            'end_date': date.strftime(self.end_date, '%Y-%m-%d') if self.end_date else None,
            'end_time': time.strftime(self.end_time, '%H:%M:%S') if self.end_time else None,
            'rsvp': self.rsvp,
        }

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, related_name="participants")
    tutor = models.ForeignKey(Tutor, related_name="events")
    status = models.CharField(verbose_name='Tilbagemelding', max_length=10, choices=(
        ('yes', 'Kommer',),
        ('no', 'Kommer ikke',),
        ('maybe', 'Har ikke taget stilling',),
        ))
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return '[RSVP '+str(self.event_id)+' '+str(self.tutor_id)+' '+self.status+']'

    class Meta:
        unique_together = (('event', 'tutor',),)
        verbose_name = 'tilbagemelding'
        verbose_name_plural = verbose_name + 'er'
        ordering = ['event', 'status']

    def json_of(self):
        return {
            'event': self.event.title,
            'tutor': self.tutor.studentnumber,
            'year': self.tutor.studentnumber,
            'status': self.status,
        }
