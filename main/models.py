from django.db import models


# Логичнее чтобы сразу шёл герой и потом его разновидность, но в плане кода вариант сделать всё наоборот будет удобнее
class Specialization(models.Model):
    HEROES = (
        ('Warrior', 'Warrior'),
        ('DK', 'Death Knight'),
        ('DH', 'Demon Hunter'),
        ('Druid', 'Druid'),
        ('Hunter', 'Hunter'),
        ('Mage', 'Mage'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Priest', 'Priest'),
        ('Rogue', 'Rogue'),
        ('Shaman', 'Shaman'),
        ('Warlock', 'Warlock')
    )
    character = models.CharField(max_length=10, null=True, blank=True, choices=HEROES, default='')
    name = models.CharField(max_length=15, null=True, blank=True, default='')
    icon = models.ImageField(upload_to='specialization_photo/', null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    acronyms = models.TextField(max_length=150, null=True, blank=True, default='')
    stats_gems_enchants = models.TextField(max_length=150, null=True, blank=True, default='')
    talents = models.TextField(max_length=150, null=True, blank=True, default='')
    rotation_priority = models.TextField(max_length=150, null=True, blank=True, default='')
    legendaries = models.TextField(max_length=150, null=True, blank=True, default='')
    gear = models.TextField(max_length=150, null=True, blank=True, default='')
    trinkets = models.TextField(max_length=150, null=True, blank=True, default='')
    weak_auras = models.TextField(max_length=150, null=True, blank=True, default='')


class Character(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True, default='')
    icon = models.ImageField(upload_to='character_photo/', null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    specializations = models.ManyToManyField(Specialization, related_name='specializations', null=True, blank=True)