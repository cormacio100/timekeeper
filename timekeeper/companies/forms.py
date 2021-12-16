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
    
    company_name = forms.CharField(label='Company Name', max_length=100)
    industry  = forms.CharField(
        label = 'Industry Type',
        widget = forms.Select(choices=INDUSTRY_TYPE)
    )
    eircode = forms.CharField(label='Eircode', max_length=20)