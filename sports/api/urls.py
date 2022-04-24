from django.urls import path 
from . import views

urlpatterns = [
    path('', views.available_leagues, name='available_leagues'),
    path('game/<str:match_id>/', views.get_game, name='get_game'),
    path('game/<str:game_id>/preview', views.get_game_preview, name='get_game_preview'),
    path('game/<str:game_id>/totals', views.get_game_totals, name='get_game_totals'),
    path('game/<str:game_id>/placeholder', views.get_game_placeholder, name='get_game_placeholder'),
    path('league/<int:league_id>/', views.get_league, name='get_league'),
    path('league/<int:league_id>/strategies', views.get_league_strategies, name='get_league_strategies'),
    path('strategies/', views.get_strategies, name="get_strategies"),
    path('strategies/<int:strategy_id>', views.get_strategy, name="get_strategy"),
    path('bets/', views.get_bets, name="get_bets"),    
    path('bets/antes', views.get_bets_antes, name="get_bets_antes"),
    path('bets/statistics', views.get_bets_statistics, name="get_bets_statistics"),
    path('bets/upcoming', views.get_bets_upcoming, name="get_bets_upcoming"),
    path('preferences/', views.get_preferences, name="preferences")
]