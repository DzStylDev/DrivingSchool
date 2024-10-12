from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model=  Inscription
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = (
            'username',
            'nom',
            'prenom',
            'password',
            'tel',
            'adresse',
            'date_naissance',
            'code_postal',
            'email',
            'civility',
        )
        labels = {
            'username': 'Nom d\'utilisateur',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'password': 'Mot de passe',
            'tel': 'Numéro de téléphone',
            'adresse': 'Adresse',
            'date_naissance': 'Date de naissance',
            'code_postal': 'code_postal',
            'email': 'email',
            'civility': 'Genre',
        }
    def __init__(self, *args, **kwargs):
        super(InscriptionForm,self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['nom'].required = True
        self.fields['prenom'].required = True
        self.fields['password'].required = True
        self.fields['tel'].required = True
        self.fields['adresse'].required = True
        self.fields['date_naissance'].required = True
        self.fields['code_postal'].required = True
        self.fields['email'].required = True
        self.fields['civility'].empty_label = "Selectionner"
        
# class IndexForm(forms.ModelForm):
#     class Meta:
#         model = Secretary
#         fields = {
#             'name',
#             'hours_pay',
#             'hour_lessons'
#         }
#         labels = {
#             'hours_pay': "Nombre d'heure que tu vas payer",
#             'hour_lessons': "Nombre d'heure de leçon prise"
#         }