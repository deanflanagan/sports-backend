from django.http import JsonResponse


# def home(request):
#     return JsonResponse({"home":"should return table with list of available games & leagues"})

def get_game(request, match_id):
    return JsonResponse({"match_id": match_id})

def get_game_preview(request, match_id):
    return JsonResponse({"match_id_preview": match_id})

def get_game_totals(request, match_id):
    return JsonResponse({"match_id_totals": match_id})

def get_game_placeholder(request, match_id):
    return JsonResponse({"match_id_placeholder": match_id})

def available_leagues(request):
    return JsonResponse({"leagues":[1,3,4]})

def get_league(request, league_id):
    return JsonResponse({"league_id": league_id})

def get_league_strategies(request, league_id):
    return JsonResponse({"league_id_and_strategies": league_id})

def get_strategies(request):
    return JsonResponse({"strategies":[1,3,4],
    "to_follow":[True, False, False]})

def get_strategy(request, strategy_id):
    return JsonResponse({"strategies":strategy_id})

def get_bets(request):
    return JsonResponse({"bets":[1,3,4],
    "to_follow":[True, False, False]})

def get_bets_antes(request):
    return JsonResponse({"bets_antes":[1,3,4],
    "to_follow":[True, False, False]})

def get_bets_statistics(request):
    return JsonResponse({"statistics":[1,3,4],
    "to_follow":[True, False, False]})

def get_bets_upcoming(request):
    return JsonResponse({"upcoming":[1,3,4],
    "to_follow":[True, False, False]})

def get_preferences(request):
    return JsonResponse({"preferences":"much config"})