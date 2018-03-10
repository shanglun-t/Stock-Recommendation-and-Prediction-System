from django import forms
#from sector import StockSelection

class brief_form(forms.Form):
    T_CHOICES=[('T1','less than 1 year'),('T2','1-2 years'),('T3','3-5 years'),
               ('T4','6-10 years'),('T5','less than 1 year')]
    
    R_CHOICES=[('R1','strongly disagree'),('R2','disagree'),
               ('R3','agree'),('R4','strongly agree')]  
    
    #B0 = forms.TextInput(attrs={'size': 4, 'title': 'Your entry', 'required': True})
    B1 = forms.ChoiceField(choices=T_CHOICES, widget=forms.RadioSelect())
    B2 = forms.ChoiceField(choices=R_CHOICES, widget=forms.RadioSelect())
    
    def clean(self):
        cleaned_data = super(brief_form, self).clean()
        B1 = cleaned_data.get('B1')
        B2 = cleaned_data.get('B2')
        if not B1 and not B2:
            raise forms.ValidationError('No answer submitted!')
    
    #def save_B(self, commit=True):
    #    form_data = self.cleaned_data
    #    self.instance.B1 = form_data['B1']
    #    self.instance.B2 = form_data['B2']
    #    self.instance.result_brief = self.calc_brief(form_data['B1'], form_data['B2']) 
    #    return super(brief_form, self).save(commit)
    

       
class full_form(forms.Form):
    T_CHOICES=[('T1','less than 1 year'),('T2','1-2 years'),('T3','3-5 years'),
               ('T4','6-10 years'),('T5','less than 1 year')]
    
    R_CHOICES=[('R1','strongly disagree'),('R2','disagree'),
               ('R3','agree'),('R4','strongly agree')]
    
    I_CHOICES=[('1010','Energy'),
               ('1510','Materials'),
               ('2010','Capital Goods'),('2020','Commercial & Professional Services'),('2030','Transportation'),
               ('2510','Automobiles & Components'),('2520','Consumer Durables & Apparel'),('2530','Consumer Services'),('2540','Media'),('2550','Retailing'),
               ('3010','Food & Staples Retailing'),('3020','Food, Beverage & Tobacco'),('3030','Household & Personal Products'),
               ('3510','Health Care Equipment & Services'),('3520','Pharmaceuticals, Biotechnology & Life Sciences'),
               ('4010','Banks'),('4020','Diversified Financials'),('4030','Insurance'),
               ('4510','Software & Services'),('4520','Technology Hardware & Equipment'),('4530','Semiconductors & Semiconductor Equipment'),
               ('5010','Telecommunication Services'),
               ('5510','Utilities'),
               ('6010','Real Estate')]
    
    #F0 = forms.TextInput(attrs={'size': 4, 'title': 'Your entry', 'required': True})
    F1 = forms.ChoiceField(choices=T_CHOICES, widget=forms.RadioSelect())
    F2 = forms.ChoiceField(choices=R_CHOICES, widget=forms.RadioSelect())
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
       
    
class brief_result_form(forms.Form):   
    B_result = forms.CharField(widget=forms.Textarea)
    
class full_result_form(forms.Form):   
    F_result = forms.CharField(widget=forms.Textarea) 
