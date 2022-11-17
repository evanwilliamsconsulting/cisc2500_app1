from django.db import models

OVERALL_CHOICES= [
    ('horrible','Horrible'),
    ('average', 'Average'),
    ('good', 'Good'),
    ('great', 'Great'),
    ('fantastic', 'Fantastic'),
    ]    
PACE_CHOICES = [
    ('too_fast','Too Fast'),
    ('too_slow','Too Slow'),
    ('just_right','Just Right'),
    ]
LANGUAGE_CHOICES = [
    ('csharp','C#'),
    ('cplusplus','C++'),
    ('javascript','JavaScript'),
    ('php','PHP'),
    ('swift','Swift'),
    ('java','Java'),
    ('go','Go'),
    ('sql','SQL'),
    ('ruby','Ruby')
    ]

class Survey(models.Model):
    comment_text = models.CharField(max_length=500)
    overall = models.CharField(choices=OVERALL_CHOICES, max_length=120)
    pace = models.CharField(choices=PACE_CHOICES, max_length=120)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=120)
