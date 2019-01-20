from django.urls import path

from news import views, models

urlpatterns = [
    path('', models.NewsList.as_view()),
    path('<str:url>', views.get_news_by_id)
]
