from django.db import models

class b_answers(models.Model):
    T_CHOICES=[('T1','less than 1 year'),('T2','1-2 years'),('T3','3-5 years'),
               ('T4','6-10 years'),('T5','less than 1 year')]
    
    R_CHOICES=[('R1','strongly disagree'),('R2','disagree'),
               ('R3','agree'),('R4','strongly agree')]
    
    #B0 = models.CharField(max_length=4)
    B1 = models.CharField(max_length=2, choices=T_CHOICES)
    B2 = models.CharField(max_length=2, choices=R_CHOICES)
    
    
class f_answers(models.Model):
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
    
    #F0 = models.CharField(max_length=4)
    F1 = models.CharField(max_length=1, choices=T_CHOICES)
    F2 = models.CharField(max_length=1, choices=R_CHOICES)
    F3 = models.CharField(max_length=1, choices=I_CHOICES)
    
    
    
class b_result(models.Model):
    clean_B1 = models.CharField(max_length=1)
    clean_B2 = models.CharField(max_length=1)
    B_result = models.CharField(max_length=200)   
    
    
class f_result(models.Model):
    clean_F1 = models.CharField(max_length=1)
    clean_F2 = models.CharField(max_length=1)
    clean_F3 = models.CharField(max_length=1)
    F_result = models.CharField(max_length=200)
    
<<<<<<< HEAD
=======

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
