"""
URL configuration for codesphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="register"),
    path('login/',views.SignInView.as_view(),name="login"),
    path('index/',views.IndexView.as_view(),name='index'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('profile/change',views.ProfileEditView.as_view(),name='profile-edit'),
    path('project/add',views.ProjectView.as_view(),name='project-add'),
    path('mywork/all',views.MyprojectListView.as_view(),name="my-work"),
    path('project/<int:pk>/change',views.ProjectUpdateView.as_view(),name='project-change'),
    path('project/<int:pk>/detail',views.ProjectDetailView.as_view(),name='project-detail'),
    path('project/<int:pk>/add-wishlist',views.WIshlistView.as_view(),name='wishlist'),
    path('wishlist/all',views.WishlistItemView.as_view(),name='my-wishlist')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


