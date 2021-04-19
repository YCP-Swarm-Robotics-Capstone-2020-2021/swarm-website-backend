"""swarm_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers

# Import all the view sets
from core.views import userViewSet
from core.views import adminViewSet
from core.views import changeViewSet
from core.views import commentViewSet
from core.views import developerViewSet
from core.views import devPersonalPageViewSet
from core.views import entryViewSet
from core.views import headingViewSet
from core.views import personalPageViewSet
from core.views import photoGalleryViewSet
from core.views import sideBarViewSet
from core.views import sponsorPersonalPageViewSet
from core.views import sponsorViewSet
from core.views import wikiViewSet
from core.views import logViewSet
from core.views import runViewSet
from core.views_front import index
# from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash= False)

# Route view sets via the router
router.register('user', userViewSet.UserViewSet, basename='user')
router.register('admin2', adminViewSet.AdminViewSet, basename='admin2')
router.register('change', changeViewSet.ChangeViewSet, basename='change')
router.register('comment', commentViewSet.CommentViewSet, basename='comment')
router.register('developer', developerViewSet.DeveloperViewSet, basename= 'developer')
router.register('devpersonalpage', devPersonalPageViewSet.DevPersonalPageViewSet, basename='devpersonalpage')
router.register('entry', entryViewSet.EntryViewSet, basename='entry')
router.register('heading', headingViewSet.HeadingViewSet, basename='heading')
router.register('personalpage', personalPageViewSet.PersonalPageViewSet, basename='personalpage')
router.register('photogallery', photoGalleryViewSet.PhotoGalleryViewSet, basename='photogallery')
router.register('sidebar', sideBarViewSet.SideBarViewSet, basename='sidebar')
router.register('sponsorpersonalpage', sponsorPersonalPageViewSet.SponsorPersonalPageViewSet, basename='sponsorpersonalpage')
router.register('sponsor', sponsorViewSet.SponsorViewSet, basename='sponsor')
router.register('wiki', wikiViewSet.WikiViewSet, basename='wiki')
router.register('log', logViewSet.LogViewSet, basename='log')
router.register('run', runViewSet.RunViewSet, basename='run')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^.*$', index, name='index'),
]
