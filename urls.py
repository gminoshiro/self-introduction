from django.urls import path
from mino import views
# ↓過去のもの(一応残してる)
#from .views import AboutView,BlogView,portfoliofunc,contactfunc

app_name = 'mino'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    #
    # ↓過去のもの(一応残してる)
    #path('About/', AboutView.as_view()),
    #path('Portfolio/', portfoliofunc),
    #path('Blog/', BlogView.as_view()),
    #path('Contact/', contactfunc),
]
