from django.urls import path
from .views import HomePageView,DetailPageView,UpdateViewPage,CreateViewPage,DeleteViewPage,MainHomePage

urlpatterns = [
    path('main/',MainHomePage.as_view(), name='home'),
    path('',HomePageView.as_view(), name='index'),
    path('<int:pk>/details/',DetailPageView.as_view(), name='detail'),
    path('<int:pk>/edit/',UpdateViewPage.as_view(), name='update'),
    path('create/',CreateViewPage.as_view(),name='create'),
    path('<int:pk>/delete/',DeleteViewPage.as_view(),name='delete')


]