from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
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
    WARCASTER = 'WC'
    WARLOCK = 'WL'
    WARJACK = 'WJ'
    WARBEAST = 'WB'
    UNIT = 'UN'
    ATTACHMENT = 'UA'
    SOLO = 'SL'
    BATTLE_ENGINE = 'BE'
    COLOSSAL = 'CO'
    GARGANTUAN = 'GA'
    TYPE_CHOICES = (
            (WARCASTER, 'Warcaster'),
            (WARLOCK, 'Warlock'),
            (WARJACK, 'Warjack'),
            (WARBEAST, 'Warbeast'),
            (UNIT, 'Unit'),
            (ATTACHMENT, 'Unit Attachment'),
            (SOLO, 'Solo'),
            (BATTLE_ENGINE, 'Battle Engine'),
            (COLOSSAL, 'Colossal'),
            (GARGANTUAN, 'Gargantuan'),
    )

    name = models.CharField(max_length=254)
    utype = models.CharField(max_length=2,
            choices=TYPE_CHOICES)
    faction = models.CharField(max_length=2,
            choices=FACTION_CHOICES)
    points = models.IntegerField()
    allowance = models.IntegerField(null=True, blank=True)

    attachments = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)

    def __str__(self):
        return self.name

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
    created = models.DateField(editable=False)
    
    units = models.ManyToManyField(Unit, through='ListEntry')
    
    rating = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    owner = models.ForeignKey(User, related_name='armylists', null=True, blank=True)
    
    def __str__(self):
        return self.name

class ListEntry(models.Model):
    unit = models.ForeignKey(Unit)
    armylist = models.ForeignKey(ArmyList)
    attached = models.ForeignKey('self', null=True, blank=True, related_name='attachments')

    def __str__(self):
        return self.unit.name
