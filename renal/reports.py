"""
Provide data for opal reports.
"""
import collections
import datetime as dt

from django.contrib.auth.models import User

from opal.models import Episode, Patient

from elcid.models import Diagnosis

def usage():
    """
    Return data for a usage report.
    """
    episodes = collections.defaultdict(int)
    for episode in Episode.objects.all():
        start = episode.date_of_admission
        end = episode.discharge_date
        if not end:
            end = dt.date.today()

        while start <= end:
            episodes[start] +=1
            start += dt.timedelta(days=1)

    return dict(
        num_users=User.objects.count(),
        num_episodes=Episode.objects.count(),
        num_diagnoses=Diagnosis.objects.count(),
        num_patients=Patient.objects.count(),
        episodes=dict(**episodes)
        )
