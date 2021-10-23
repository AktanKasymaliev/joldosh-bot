from django.urls import path

from map.views import HomePage
from map.api.views import PointsView, SavePointView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomePage.as_view()),

    path("api/v1/add-point/", SavePointView.as_view()),
    path("api/v1/points-list/", PointsView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)