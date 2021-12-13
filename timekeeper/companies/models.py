from django.db import models

# Create your models here.

class Company(models.Model):
    
    def __unicode__(self):
        return self.name
    
 
    INDUSTRY_TYPE = {
        ('Government','Government'),
        ('Transport','Transport'),
        ('IT','IT'),
        ('Retail','Retail'),
        ('Sport','Sport'),
        ('Hospitality','Hospitality'),
        ('IT','IT'),
        ('Agriculture','Agriculture'),
        ('Telecoms','Telecoms'),
        ('Food','Food'),
        ('Construction','Construction'),
        ('Farming','Farming'),
        ('Education','Education'),
        ('Pharma','Pharma'),
        ('Healthcare','Healthcare'),
        ('Entertainment','Entertainment'),
        ('Media','Media'),
        ('Energy','Energy'),
        ('Manufacturing','Manufacturing'),
        ('Music','Music'),
        ('Mining','Mining'),
        ('Electronics','Electronics')
    }
    
    COUNTIES = (
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Derry', 'Derry'),
        ('Donegal', 'Donegal'),
        ('Down', 'Down'),
        ('Dublin', 'Dublin'),
        ('Fermanagh', 'Fermanagh'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Tyrone', 'Tyrone'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    )

    
    ############################################################################
    #   FIELDS
    ############################################################################
    name = models.CharField(
        max_length = 30
    )
    industry = models.CharField(
        max_length = 20,
        choices = INDUSTRY_TYPE,
        default = 'Government'
    )
    location = models.CharField(
        max_length = 15,
        choices = COUNTIES,
        default = 'Antrim'
    )
    