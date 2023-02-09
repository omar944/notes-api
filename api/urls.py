from api.views import NotesViewSet
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('notes/', NotesViewSet.as_view())
    path('account/registration/', RegisterView.as_view(), name='rest_register'),
    path('account/login/', LoginView.as_view(), name='rest_login'),
]
router = DefaultRouter()
router.register(r'notes', NotesViewSet, basename='airport')
urlpatterns += router.urls
