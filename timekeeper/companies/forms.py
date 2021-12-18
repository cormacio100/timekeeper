from django import forms

class AddCompanyForm(forms.Form):
    INDUSTRY_TYPE = (
        ('Hospitality','Hospitality'),
        ('Mining','Mining'),
        ('Healthcare','Healthcare'),
        ('Government','Government'),
        ('Waste','Waste'),
        ('IT','IT'),
        ('Music','Music'),
        ('Arts','Arts'),
        ('Culture','Culture'),
        ('Cinema','Cinema'),
        ('Entertainment','Entertainment'),
        ('Recreation','Recreation'),
        ('Utilities','Utilities'),
        ('Agriculture and Forestry','Agriculture and Forestry'),
        ('Construction','Construction'),
        ('Education','Education'),
        ('Transport','Transport'),
        ('Science','Science'),
        ('Pharma','Pharma'),
        ('Finance','Finance'),
        ('Retail','Retail'),
        ('Real Estate','Real Estate'),
        ('Sport','Sport'),
        ('Manufacturing','Manufacturing'),
        ('Engineering','Engineering'),
        ('Industrial','Industrial'),
        ('Landscaping','Landscaping'),
        ('Other','Other')
    )
    
    COUNTIES = (
        ('Antrim','Antrim'),
        ('Armagh','Armagh'),
        ('Cavan','Cavan'),
        ('Carlow','Carlow'),
        ('Clare','Clare'),
        ('Cork','Cork'),
        ('Derry','Derry'),
        ('Donegal','Donegal'),
        ('Down','Down'),
        ('Dublin','Dublin'),
        ('Fermanagh','Fermanagh'),
        ('Galway','Galway'),
        ('Kerry','Kerry'),
        ('Kildare','Kildare'),
        ('Kilkenny','Kilkenny'),
        ('Laois','Laois'),
        ('Leitrim','Leitrim'),
        ('Limerick','Limerick'),
        ('Longford','Longford'),
        ('Louth','Louth'),
        ('Mayo','Mayo'),
        ('Meath','Meath'),
        ('Monaghan','Monaghan'),
        ('Offaly','Offaly'),
        ('Roscommon','Roscommon'),
        ('Sligo','Sligo'),
        ('Tipperary','Tipperary'),
        ('Tyrone','Tyrone'),
        ('Waterford','Waterford'),
        ('Westmeath','Westmeath'),
        ('Wexford','Wexford'),
        ('Wicklow','Wicklow')
    )
    
    company_name = forms.CharField(label='Company Name ', max_length=100)
    industry  = forms.CharField(
        label = 'Industry Type ',
        widget = forms.Select(choices=INDUSTRY_TYPE)
    )
    county = forms.CharField(
        label = 'County ',
        widget = forms.Select(choices=COUNTIES)
    )
    
    eircode = forms.CharField(label='Eircode ', max_length=20)