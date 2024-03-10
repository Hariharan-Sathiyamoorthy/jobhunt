from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
    path('getWhishlist/', views.getIndexes,{'page':'whishlist'}, name='whsihlist'),
    path('getApplied/', views.getIndexes,{'page':'applied'} ,name='applied'),
    path('getInterview/', views.getIndexes,{'page':'interview'},name='interview'),
    path('getOffer/', views.getIndexes, {'page':'offer'},name='offer'),
    path('getRejected/', views.getIndexes,{'page':'rejected'} ,name='rejected'),
    path('createWhishlist/', views.createJobs,{'page':'whishlist'}, name='createWhishlist'),
    path('createApplied/', views.createJobs,{'page':'applied'}, name='createApplied'),
    path('createInterview/', views.createJobs,{'page':'interview'}, name='createInterview'),
    path('createOffer/', views.createJobs,{'page':'offer'}, name='createOffer'),
    path('createRejected/', views.createJobs,{'page':'rejected'}, name='createRejected'),
    path('updateWhishlist/<int:id>/', views.updateJobs,{'page':'whishlist'}, name='updateWhishlist'),
    path('updateApplied/<int:id>/', views.updateJobs,{'page':'applied'}, name='updateApplied'),
    path('updateInterview/<int:id>/', views.updateJobs,{'page':'interview'}, name='updateInterview'),
    path('updateOffer/<int:id>/', views.updateJobs,{'page':'offer'}, name='updateOffer'),
    path('updateRejected/<int:id>/', views.updateJobs,{'page':'rejected'}, name='updateRejected'),
    path('deleteWhishlist/<int:id>/', views.deleteJobs,{'page':'whishlist'}, name='deleteWhishlist'),
    path('deleteApplied/<int:id>/', views.deleteJobs,{'page':'applied'}, name='deleteApplied'),
    path('deleteInterview/<int:id>/', views.deleteJobs,{'page':'interview'}, name='deleteInterview'),
    path('deleteOffer/<int:id>/', views.deleteJobs,{'page':'offer'}, name='deleteOffer'),
    path('deleteRejected/<int:id>/', views.deleteJobs,{'page':'rejected'}, name='deleteRejected'),

]