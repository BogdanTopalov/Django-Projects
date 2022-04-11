from django.urls import path

from ProjectSoftUni.accounts_app.views import ShowProfileView, RegisterProfileView, DeleteProfileView,\
    LoginProfileView, LogoutProfileView, UpdateProfileView, ProfileRecipesView

urlpatterns = [
    path('<int:pk>/', ShowProfileView.as_view(), name='show profile page'),
    path('register/', RegisterProfileView.as_view(), name='register profile page'),
    path('login/', LoginProfileView.as_view(), name='login profile page'),
    path('logout/', LogoutProfileView.as_view(), name='logout profile'),
    path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete profile page'),
    path('<int:pk>/edit/', UpdateProfileView.as_view(), name='edit profile page'),
    path('<int:pk>/recipes/', ProfileRecipesView.as_view(), name='profile recipes page'),

]

import ProjectSoftUni.accounts_app.signals
