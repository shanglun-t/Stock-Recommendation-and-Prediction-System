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
               ('Telecommunication Services','Telecommunication Services'),('Utilities', 'Utilities'),
               ('Real Estate','Real Estate')]

    #F0 = forms.TextInput(attrs={'size': 4, 'title': 'Your entry', 'required': True})
    F1 = forms.ChoiceField(label='How long you plan to keep your fund invested?', choices=T_CHOICES, widget=forms.RadioSelect())
    F2 = forms.ChoiceField(label='I would accept higher risk as a trade-off reaching my financial goal earlier than expected.',choices=R_CHOICES, widget=forms.RadioSelect())
    F3 = forms.MultipleChoiceField(label='Select your choice of industry/industries from the list',
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



