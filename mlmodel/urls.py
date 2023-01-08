from django.urls import path



from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('previous',views.prediction_history,name='previous'),
]