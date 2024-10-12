from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField

# class Gender(models.TextChoices):
#     MALE = "first", _("The first choice, it is")
#     FEMALE = "second", _("The second choice, it is")

class Inscription(models.Model):
    username = models.CharField(max_length=100, default="")
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    password = models.CharField(max_length=32, default="")
    tel = models.CharField(max_length=10)
    adresse = models.TextField()
    date_naissance = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    civility = models.CharField(choices=[
        ('Homme', 'homme'),
        ('Femme', 'femme')
    ], max_length=20)
    comptes = models.CharField(choices=[
        ("1", 'Student'),
        ("2", 'Instructor'),
        ("3", 'Secretary'),
        ("4", 'Admin'),
    ], max_length=20, default='Student')
    # role=models.enums(["student", "instructor", "secretary", "admin"])    

# class Fiches(models.Model):
#     fk = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    
class Demande(models.Model):
    fk = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, null=True)
    forfait = models.IntegerField(null=True, blank=True) 
    confirmation = models.BooleanField(default=False)
    
#     @property
#     def username(self):
#          return self.fk.username
     
#     @property
#     def nom(self):
#          return self.fk.nom
     
#     @property
#     def prenom(self):
#          return self.fk.prenom
     
#     @property
#     def password(self):
#          return self.fk.password
     
#     @property
#     def tel(self):
#          return self.fk.tel
     
#     @property
#     def adresse(self):
#          return self.fk.adresse
     
#     @property
#     def date_naissance(self):
#          return self.fk.date_naissance
     
#     @property
#     def code_postal(self):
#          return self.fk.code_postal
     
#     @property
#     def email(self):
#          return self.fk.email
     
#     @property
#     def civility(self):
#          return self.fk.civility
     
     