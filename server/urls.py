from django.contrib import admin
from django.urls import path
from core.views import PersonController, IdealWeightController

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/persons/', PersonController.as_view()),
    path('api/persons/<int:pk>/', PersonController.as_view()),
    path('api/persons/<int:pk>/ideal_weight/', IdealWeightController.as_view()),
]
