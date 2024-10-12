from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),    
    
    # crud eleve (student)
    path('eleves', views.list_eleves, name="eleves_list"),    
    path('create-student', views.form_student, name="form_student"),    
    path('modifiy-student/<int:id>', views.modify_student, name="modify_student"),    
    path('delete-student/<int:id>', views.delete_student, name="delete_student"),    
    path('fiche-student/<int:id>', views.fiche_student, name="fiche_student"),    
    
    # crud instructeur (instructor)
    path('instructeurs', views.list_instructors, name="instructors_list"),    
    path('create-instructor', views.form_instructor, name="form_instructor"),    
    path('modifiy-instructor/<int:id>', views.modify_instructor, name="modify_instructor"),    
    path('delete-instructor/<int:id>', views.delete_instructor, name="delete_instructor"),    
    path('fiche-instructor/<int:id>', views.fiche_instructor, name="fiche_instructor"),   
    
    #Demande lier à la secretaire
    path('demande-students/<int:id_secretary>', views.demandes_student, name="demandes_students"),    
    #Demande accepter
    path('demande-accept/<int:id>', views.demande_accept, name="demande_accept"),
    
    path('form-connexion', views.form_connexion, name="form_connexion"),    
    path('form-deconnexion', views.form_deconnexion, name="form_deconnexion"),    
]  