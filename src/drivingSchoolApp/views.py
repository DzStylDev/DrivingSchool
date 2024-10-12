from django.shortcuts import render, redirect
from .models import Inscription , Demande
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sessions.models import Session

def index(request):
        
        # idSession = request.session.session_key
        
        try:
                        
                       
                        
                        
                        data = request.session.get('mes_donnees')
                             
                        if data is not None:
                                roleUser = data.get('currentRole')
                                currentUser = data.get('currentUser')
                                print("Le rôle de l'utilisateur dans la session est:", roleUser)                                                        
                                
                                # idSession = request.session.session_key
                                
                                # session = Session.objects.get(session_key=idSession)
                                # session_donnees = session.get_decoded()
                        
                                # user_id = session_donnees.get('_auth_user_id')
                                # currentUser = User.objects.get(id=user_id)
                                                                
                                
                        
                                if request.POST:
                                        userSecretaire = Inscription.objects.get(id=73, comptes=3)
                                        demande_instance = Demande(fk=userSecretaire)
                                
                                        demande_instance.nom = currentUser['username']    
                                        currentRole = roleUser
                                        userSecretaire = userSecretaire
                                        demande_instance.forfait = request.POST['forfait']
                                        confirmation = 'false'
                                        forfait = demande_instance.forfait
                                        demande_instance.save()
                                else:
                                        roleUser = data.get('currentRole')
                                        currentRole = roleUser
                                        userSecretaire = 'non'
                                        forfait = ''
                                        
                                        demande_user = Demande.objects.filter(fk=currentUser['id'])
                                        # confirmation = demande_user.confirmation
                                        confirmation = ""
                                        
                        else:
                                print("La clé 'mes_donnees' n'est pas présente dans la session.")
                                roleUser = None
                                currentRole = None
                                userSecretaire = 'non'
                                currentUser = None
                                confirmation = False
                                forfait = ''
                                
        except Session.DoesNotExist:
                messages.error(request, "La session n'existe pas")
                return redirect('/auto-ecole')
      
        return render(request, 'index.html',  {
                'currentRole' : currentRole,
                'currentSecretaire': userSecretaire,
                'currentUser': currentUser,
                'forfait': forfait,
                'confirmation': confirmation 
        })

def form_student(request):
        if request.method == "GET":        
                formInscription = InscriptionForm()
                return render(request, 'students/create_student.html', { 'form': formInscription})
        else:
                formInscription = InscriptionForm(request.POST)
                
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                
                if formInscription.is_valid():
                        formInscription.save()
                        
                        user=User.objects.create_user(
                                username, 
                                email,
                                password,
                        )
                        user.save()
                return redirect('eleves_list')
def modify_student(request, id):
        eleve = Inscription.objects.get(id=id)
        if request.method == "GET":
                form = InscriptionForm()
                return render(request, 'students/modify_student.html', { 
                        'form' : form, 
                        'eleve': eleve
                }) 
        else:
                userEleve = User.objects.get(username=eleve.username)
                
                if request.POST['username']:
                       eleve.username = request.POST['username']
                       userEleve.username = request.POST['username']
                if request.POST['nom']:
                        eleve.nom=request.POST['nom']
                if request.POST['prenom']:
                        eleve.prenom=request.POST['prenom']
                if request.POST['password']:
                        eleve.password=request.POST['password']
                        userEleve.password = request.POST['password']
                if request.POST['tel']:
                        eleve.tel=request.POST['tel'] 
                if request.POST['adresse']:
                        eleve.adresse=request.POST['adresse']
                if request.POST['date_naissance']:
                        eleve.date_naissance=request.POST['date_naissance']
                if request.POST['code_postal']:
                        eleve.code_postal=request.POST['code_postal']
                if request.POST['email']:
                        eleve.email=request.POST['email']
                if request.POST['civility']:
                        eleve.civility=request.POST['civility']

                eleve.save()
                userEleve.save()
                
        return redirect('/auto-ecole/eleves')
        
def delete_student(request, id):
          eleve = Inscription.objects.get(id=id)
          user = User.objects.get(username=eleve.username)
          user.delete()
          eleve.delete()
          return redirect('/auto-ecole/eleves')
        
def delete_instructor(request, id):
        instructeur = Inscription.objects.get(id=id)
        user = User.objects.get(username=instructeur.username)
        user.delete()
        instructeur.delete()
        return redirect('/auto-ecole/instructeurs')

def demandes_student(request, id_secretary):
        get_secretaire = Inscription.objects.get(id=id_secretary)
        receive_demandes = Demande.objects.filter(fk_id=id_secretary)
        
        return render(request, 'secretary/les_demandes.html', {
                'secretaire': get_secretaire, 
                'demandes' : receive_demandes
        })
def demande_accept(request, id):
        currentDemande = Demande.objects.get(id=id)
        inscription = Inscription.objects.get(id=currentDemande.fk_id)
        
        currentDemande.fk_id = inscription.id
        currentDemande.confirmation = True
        
        currentDemande.save()

        print(f"Tu a accepter la demande de {inscription.nom}")
        return redirect(f'/auto-ecole/demande-students/{inscription.id}')
        
def fiche_student(request, id):
        ficheEleve = Inscription.objects.get(id=id)
        return render(request, 'students/fiche_student.html', {
                'ficheEleve': ficheEleve
        })

def fiche_instructor(request, id):
        return render(request, 'instructors/fiche_instructor.html')

def modify_instructor(request, id):
        instructeur = Inscription.objects.get(id=id)
        userInstructeur = User.objects.get(username=instructeur.username)
        if request.method == "GET":
                form = InscriptionForm()
                return render(request, 'instructors/modify_instructor.html', { 
                        'form' : form, 
                        'instructeur': instructeur
                }) 
        else:
                if request.POST['username']:
                       instructeur.username = request.POST['username']
                       userInstructeur.username = request.POST['username']
                if request.POST['nom']:
                        instructeur.nom=request.POST['nom']
                if request.POST['prenom']:
                        instructeur.prenom=request.POST['prenom']
                if request.POST['password']:
                        instructeur.password=request.POST['password']
                        userInstructeur.password = request.POST['password']
                if request.POST['tel']:
                        instructeur.tel=request.POST['tel']
                if request.POST['adresse']:
                        instructeur.adresse=request.POST['adresse']
                if request.POST['date_naissance']:
                        instructeur.date_naissance=request.POST['date_naissance']
                if request.POST['code_postal']:
                        instructeur.code_postal=request.POST['code_postal']
                if request.POST['email']:
                        instructeur.email=request.POST['email']
                if request.POST['civility']:
                        instructeur.civility=request.POST['civility']
        
                instructeur.save()
                userInstructeur.save()
                return redirect('/auto-ecole/instructeurs')

        
def form_instructor(request):
        if request.method == "GET":        
                formInscription = InscriptionForm()
                return render(request, 'instructors/create_instructor.html', { 'form': formInscription})
        else:
                model = Inscription()
                
                model.username = request.POST['username']
                model.prenom = request.POST['prenom']
                model.nom = request.POST['nom']
                model.password = request.POST['password']
                model.tel = request.POST['tel']
                model.adresse = request.POST['adresse']
                model.date_naissance = request.POST['date_naissance']
                model.code_postal = request.POST['code_postal']
                model.email = request.POST['email']
                model.civility = request.POST['civility']
                
                model.comptes = 2
                model.save()
                
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                
                user=User.objects.create_user(
                        username, 
                        email,
                        password,
                )
                user.save()
                return redirect('instructors_list')
        
def list_eleves(request):
        eleves = Inscription.objects.filter(comptes=1).all()
        return render(request, 'students/list_eleves.html', { "eleves_list": eleves })        
       
def list_instructors(request):
       instructeurs = Inscription.objects.filter(comptes=2).all()
       return render(request, 'instructors/list_instructors.html', { "instructeurs_list": instructeurs })        
        
def get_role(currentRoleKey, comptes):
    return comptes.get(currentRoleKey, None)
 
def form_connexion(request):
        if request.method == "POST":     
                username = request.POST['username']
                password = request.POST['password']
                
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        try:
                                getUser = Inscription.objects.get(username=username)
                                login(request, user)
                                
                                userRole = getUser.comptes
                                request.session['mes_donnees'] = {
                                        'currentUser' : model_to_dict(getUser),
                                        'currentRole': userRole
                                }
                                messages.success(request, 'Authentification reussi')
                                
                        except Inscription.DoesNotExist: 
                                print("L'utilisateur avec le nom d'utilisateur spécifié n'existe pas.")
                                return redirect('/auto-ecole')
                        except Inscription.MultipleObjectsReturned:
                                print("Plusieurs utilisateurs correspondent au nom d'utilisateur spécifié.")
                                return redirect('/auto-ecole')
                        
                        return redirect('/auto-ecole')
                else:
                        messages.error(request, 'Mauvaise authentification')
                        return redirect('/auto-ecole')
        else:
                return render(request, 'connexion.html')
                        
def form_deconnexion(request):
        logout(request)
        messages.success(request, 'Vous avez bien était déconnecté')
        return redirect('/auto-ecole')

# def delete_eleve(request, id):
#         eleve=Student.objects.get(id=id)
#         eleve.delete()
#         return redirect('/')

# def form_inscription(request):
#         return render(request, 'form_inscription.html')   