"""darts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pdfreports import views


urlpatterns = [
    path('', include('pages.urls')),
    path('weeks', include('weeks.urls')),
    path('schedules', include('schedules.urls')),
    path('standings/', include('standings.urls')),
    path('teams', include('teams.urls')),
    path('players/', include('players.urls')),
    path('playerstat/', include('playerstat.urls')),
    path('playerplus/', include('playerplus.urls')),

    path('upload/', views.upload, name='upload'),
    path('pdfreports/', views.pdfreport_list, name='pdfreport_list'),
    path('pdfreports/upload/', views.upload_pdfreport, name='upload_pdfreport'),
    path('pdfreports/<int:pk>/', views.delete_pdfreport, name='delete_pdfreport'),

    path('class/pdfreports/', views.PdfreportListView.as_view(), name='class_pdfreport_list'),
    path('class/pdfreports/upload/', views.UploadPdfreportView.as_view(), name='class_upload_pdfreport'),

    path('admin/', admin.site.urls),
    path('explorer/', include('explorer.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

