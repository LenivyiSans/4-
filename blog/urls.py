from django.urls import path
from . import views
from . import nowdate_view
from . import views3

urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', nowdate_view.nowdate_view),
    path('goodby/', views3.helloView),
]