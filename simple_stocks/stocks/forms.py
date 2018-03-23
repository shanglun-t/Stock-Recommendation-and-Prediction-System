from django import forms


class brief_form(forms.Form):
    T_CHOICES=[['T1','Less than 1 year'],['T2','1-2 years'],['T3','3-5 years'],
               ['T4','6-10 years'],['T5','More than 10 year']]
    
    R_CHOICES=[['R1','Strongly agree'],['R2','Agree'], ['R3','Disagree'],['R4','Strongly disagree']
               ,]

    B1 = forms.CharField(label='How long you plan to keep your fund invested?',
                                    widget=forms.RadioSelect(choices=T_CHOICES))
    B2 = forms.CharField(label='I would accept higher risk as a trade-off reaching my financial goal earlier than expected.',
                         widget=forms.RadioSelect(choices=R_CHOICES))

    
    def clean(self):
        self.cleaned_data = super(brief_form, self).clean()
        self.B1 = self.cleaned_data.get('B1')
        self.B2 = self.cleaned_data.get('B2')
        if not self.B1 and not self.B2:
            raise forms.ValidationError('No answer submitted!')
        return self.cleaned_data
    
    #def save_B(self, commit=True):
    #    form_data = self.cleaned_data
    #    self.instance.B1 = form_data['B1']
    #    self.instance.B2 = form_data['B2']
    #    self.instance.result_brief = self.calc_brief(form_data['B1'], form_data['B2']) 
    #    return super(brief_form, self).save(commit)
    

       
class full_form(forms.Form):
    T_CHOICES=[('T1','less than 1 year'),('T2','1-2 years'),('T3','3-5 years'),
               ('T4','6-10 years'),('T5','more than 10 year')]
    
    R_CHOICES=[('R1','strongly disagree'),('R2','disagree'),
               ('R3','agree'),('R4','strongly agree')]
    
    I_CHOICES=[('Energy','Energy'), ('Materials','Materials'),
               ('Capital Goods','Capital Goods'),('Commercial & Professional Services','Commercial & Professional Services'),
               ('Transportation','Transportation'),('Automobiles & Components','Automobiles & Components'),
               ('Consumer Durables & Apparel','Consumer Durables & Apparel'),('Consumer Services','Consumer Services'),
               ('Media','Media'),('Retailing','Retailing'),
               ('Food & Staples Retailing','Food & Staples Retailing'),('Food Beverage & Tobacco','Food Beverage & Tobacco'),
               ('Household & Personal Products','Household & Personal Products'), ('Health Care Equipment & Services','Health Care Equipment & Services'),
               ('Pharmaceuticals Biotechnology & Life Sciences','Pharmaceuticals Biotechnology & Life Sciences'), ('Banks','Banks'),
               ('Diversified Financials','Diversified Financials'),('Insurance','Insurance'),
               ('Software & Services','Software & Services'), ('Technology Hardware & Equipment','Technology Hardware & Equipment'),
               ('Semiconductors & Semiconductor Equipment','Semiconductors & Semiconductor Equipment'),
               ('Telecommunication Services','Telecommunication Services'),('Utilities','Utilities'),
               ('Real Estate','Real Estate')]
    
    #F0 = forms.TextInput(attrs={'size': 4, 'title': 'Your entry', 'required': True})
    F1 = forms.ChoiceField(label='How long you plan to keep your fund invested?', choices=T_CHOICES, widget=forms.RadioSelect())
    F2 = forms.ChoiceField(label='I would accept higher risk as a trade-off reaching my financial goal earlier than expected.',choices=R_CHOICES, widget=forms.RadioSelect())
    F3 = forms.MultipleChoiceField(
         choices = I_CHOICES, 
         widget  = forms.CheckboxSelectMultiple,
         )
    
    def clean(self):
        cleaned_data = super(full_form, self).clean()
        F1 = cleaned_data.get('F1')
        F2 = cleaned_data.get('F2')
        F3 = cleaned_data.get('F3')
        if not F1 and not F2 and not F3:
            raise forms.ValidationError('No answer submitted!')
        
    #def save_F(self, commit=True):
    #    form_data = self.cleaned_data
    #    self.instance.B1 = form_data['F1']
    #    self.instance.B2 = form_data['F2']
    #    self.instance.B2 = form_data['F3']
    #    self.instance.result_full = self.calc_full(form_data['F1'], form_data['F2'], form_data['F3']) 
    #    return super(full_form, self).save(commit)
       
'''
 Cable & Satellite
 Casinos & Gaming
 Computer & Electronics Retail
 Consumer Electronics
 Department Stores
 Distributors
 General Merchandise Stores
 Home Furnishings
 Home Improvement Retail
 Homebuilding
 Hotels; Resorts & Cruise Lines
 Household Appliances
 Housewares & Specialties
 Internet & Direct Marketing Retail
 Leisure Products
 Motorcycle Manufacturers
 Publishing
 Restaurants
 Specialty Stores
 Tires & Rubber
 Agricultural Products
 Brewers
 Distillers & Vintners
 Drug Retail
 Food Distributors
 Food Retail
 Household Products
 Hypermarkets & Super Centers
 Packaged Foods & Meats
 Personal Products
 Soft Drinks
 Tobacco
 Integrated Oil & Gas
 Oil & Gas Drilling
 Oil & Gas Equipment & Services
 Oil & Gas Exploration & Production
 Oil & Gas Refining & Marketing
 Oil & Gas Storage & Transportation
 Asset Management & Custody Banks
 Consumer Finance
 Diversified Banks
 Financial Exchanges & Data
 Insurance Brokers
 Investment Banking & Brokerage
 Life & Health Insurance
 Multi-line Insurance
 Multi-Sector Holdings
 Property & Casualty Insurance
 Regional Banks
 Reinsurance
 Thrifts & Mortgage Finance
 Biotechnology
 Health Care Distributors
 Health Care Equipment
 Health Care Facilities
 Health Care Services
 Health Care Supplies
 Health Care Technology
 Life Sciences Tools & Service
 Life Sciences Tools & Services
 Managed Health Care
 Pharmaceuticals
 Aerospace & Defense
 Agricultural & Farm Machinery
 Air Freight & Logistics
 Airlines
 Building Products
 Construction & Engineering
 Construction Machinery & Heavy Trucks
 Diversified Support Services
 Electrical Components & Equipment
 Environmental & Facilities Services
 Human Resource & Employment Services
 Industrial Conglomerates
 Industrial Machinery
 Railroads
 Research & Consulting Services
 Trading Companies & Distributors
 Trucking
 Application Software
 Communications Equipment
 Data Processing & Outsourced Services
 Electronic Components
 Electronic Equipment & Instruments
 Electronic Manufacturing Services
 Home Entertainment Software
 Internet Software & Services
 IT Consulting & Other Services
 Semiconductor Equipment
 Semiconductors
 Systems Software
 Technology Hardware; Storage & Peripherals
 Construction Materials
 Copper
 Diversified Chemicals
 Fertilizers & Agricultural Chemicals
 Gold
 Industrial Gases
 Metal & Glass Containers
 Paper Packaging
 Specialty Chemicals
 Steel
 Health Care REITs
 Hotel & Resort REITs
 Industrial REITs
 Office REITs
 Real Estate Services
 Residential REITs
 Retail REITs
 Specialized REITs
 Integrated Telecommunication Services
 Electric Utilities
 Independent Power Producers & Energy Traders
 Multi-Utilities
 Water Utilities
 '''

