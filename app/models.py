from django.db import models
from django.contrib.auth.models import User

class ArmyList(models.Model):
    CYGNAR = 'CY'
    MENOTH = 'ME'
    KHADOR = 'KD'
    CRYX = 'CX'
    RETRIBUTION = 'RT'
    CONVERGENCE = 'CV'
    MERCENARIES = 'MC'
    TROLLBLOODS = 'TR'
    CIRCLE = 'CO'
    SKORNE = 'SK'
    LEGION = 'LG'
    MINIONS = 'MN'
    FACTION_CHOICES = (
            (CYGNAR, 'Cygnar'),
            (MENOTH, 'The Protectorate of Menoth'),
            (KHADOR, 'Khador'),
            (CRYX, 'Cryx'),
            (RETRIBUTION, 'Retribution of Scyrah'),
            (CONVERGENCE, 'Convergence of Cyriss'),
            (MERCENARIES, 'Mercenaries'),
            (TROLLBLOODS, 'Trollbloods'),
            (CIRCLE, 'Circle Orboros'),
            (SKORNE, 'Skorne'),
            (LEGION, 'Legion of Everblight'),
            (MINIONS, 'Minions'),
    )
    XSMALL = 15
    SMALL = 25
    MEDIUM = 35
    LARGE = 50
    POINTS_CHOICES = (
            (XSMALL, '15 pts'),
            (SMALL, '25 pts'),
            (MEDIUM, '35 pts'),
            (LARGE, '50 pts'),
    )
    name = models.CharField(max_length=254, unique=True)
    faction = models.CharField(max_length=2,
            choices=FACTION_CHOICES)
    points = models.IntegerField(choices=POINTS_CHOICES)
    created = models.DateTimeField(editable=False)

    owner = models.ForeignKey(User, related_name='armylists', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Unit(models.Model):
    CASTER = 'CS'
    WARJACK = 'WJ'
    UNIT = 'UN'
    SOLO = 'SO'
    COLOSSAL = 'CO'
    ENGINE = 'EN'
    TYPE_CHOICES = (
            (CASTER, 'Warcaster/Warlock'),
            (WARJACK, 'Warjack/Warbeast'),
            (UNIT, 'Unit'),
            (SOLO, 'Solo'),
            (COLOSSAL, 'Colossal/Gargantuan'),
            (ENGINE, 'Battle Engine'),
    )
    name = models.CharField(max_length=254)
    utype = models.CharField(max_length=2,
            choices=TYPE_CHOICES)

    armylist = models.ForeignKey(ArmyList, related_name='units', null=True, blank=True)

    def __str__(self):
        return self.name
