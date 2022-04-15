from django.urls import path

from ProjectSoftUni.accounts_app.views.user import RegisterUserView, LoginUserView, LogoutUserView

from ProjectSoftUni.accounts_app.views.profile import \
    ShowProfileView, DeleteProfileView, UpdateProfileView, ProfileRecipesView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user page'),
    path('login/', LoginUserView.as_view(), name='login user page'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),

    path('<int:pk>/', ShowProfileView.as_view(), name='show profile page'),
    path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete profile page'),
    path('<int:pk>/edit/', UpdateProfileView.as_view(), name='edit profile page'),
    path('<int:pk>/recipes/', ProfileRecipesView.as_view(), name='profile recipes page'),
]

import ProjectSoftUni.accounts_app.signals
