from django.db import models

class Game(models.Model):
    sport = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    league = models.CharField(max_length=50)
    league_id = models.IntegerField()
    match_id = models.CharField(max_length=8)
    start_time = models.DateTimeField()
   
    match_status = models.CharField(max_length=3)
    team = models.CharField(max_length=30)
    opposition = models.CharField(max_length=30)
    ft1 = models.IntegerField(blank=True, null=True, default=None)
    ft2 = models.IntegerField(blank=True, null=True, default=None)
    home_odds = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    away_odds = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    draw_odds = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    ou = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_over = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_under = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    pin_over = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    pin_under = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    hdp = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    avg_home =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_away =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['start_time']


class Bets(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    match_id = models.CharField(max_length=8)
    side = models.CharField(max_length=12)
    line = models.DecimalField(max_digits=6, decimal_places=3)
    odd = models.DecimalField(max_digits=6, decimal_places=3)
    dollar = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        unique_together = ('match_id', 'line',)

class Ante(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    match_id = models.CharField(max_length=8, null=True, blank=True)

    description= models.CharField(max_length=100)
    bet_size = models.DecimalField(max_digits=16, decimal_places=2)
    returned = models.DecimalField(max_digits=16, decimal_places=2,blank=True, null=True)
    odds_struck = models.DecimalField(max_digits=6, decimal_places=3)
    pl = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True)
    

    def __str__(self):
        return self.description

class Preview(models.Model):
    sport = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    league = models.CharField(max_length=50)
    league_id = models.IntegerField()
    match_id = models.CharField(max_length=8)
    start_time = models.DateTimeField()
   
    match_status = models.CharField(max_length=3)
    team = models.CharField(max_length=30)
    opposition = models.CharField(max_length=30)
    ft1 = models.IntegerField(blank=True, null=True, default=None)
    ft2 = models.IntegerField(blank=True, null=True, default=None)
    home_odds = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    away_odds = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    draw_odds = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    ou = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_over = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_under = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    pin_over = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    pin_under = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    hdp = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True, default=None)
    avg_home =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    avg_away =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    winner = models.CharField(max_length=1)
    rf_pre_h = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_pre_a = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    diff = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    n_teams = models.IntegerField(blank=True, null=True)
    home_nth_game = models.IntegerField(blank=True, null=True)
    away_nth_game = models.IntegerField(blank=True, null=True)
    ex_ft1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_ft2 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_att_rank = models.IntegerField(blank=True, null=True)
    home_def_rank = models.IntegerField(blank=True, null=True)
    away_att_rank = models.IntegerField(blank=True, null=True)
    away_def_rank = models.IntegerField(blank=True, null=True)
    away_rank_rating = models.IntegerField(blank=True, null=True)
    home_rank_rating = models.IntegerField(blank=True, null=True)
    actual_cap = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ex_cap = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_last_opponent = models.CharField(max_length=50)    
    away_last_opponent = models.CharField(max_length=50)    
    home_last_venue = models.CharField(max_length=4)    
    away_last_venue = models.CharField(max_length=4)    
    home_last_result = models.CharField(max_length=4)    
    away_last_result = models.CharField(max_length=4)  
    home_last_days_delta = models.IntegerField(blank=True, null=True)  
    away_last_days_delta = models.IntegerField(blank=True, null=True)  
    
    home_second_last_opponent = models.CharField(max_length=50)    
    away_second_last_opponent = models.CharField(max_length=50)    
    home_second_last_venue = models.CharField(max_length=4)    
    away_second_last_venue = models.CharField(max_length=4)    
    home_second_last_result = models.CharField(max_length=4)    
    away_second_last_result = models.CharField(max_length=4)  
    home_second_last_days_delta = models.IntegerField(blank=True, null=True)  
    away_second_last_days_delta = models.IntegerField(blank=True, null=True)  

    
    home_third_last_opponent = models.CharField(max_length=50)    
    away_third_last_opponent = models.CharField(max_length=50)    
    home_third_last_venue = models.CharField(max_length=4)    
    away_third_last_venue = models.CharField(max_length=4)    
    home_third_last_result = models.CharField(max_length=4)    
    away_third_last_result = models.CharField(max_length=4)  
    home_third_last_days_delta = models.IntegerField(blank=True, null=True)  
    away_third_last_days_delta = models.IntegerField(blank=True, null=True)  
    
    home_fourth_last_opponent = models.CharField(max_length=50)    
    away_fourth_last_opponent = models.CharField(max_length=50)    
    home_fourth_last_venue = models.CharField(max_length=4)    
    away_fourth_last_venue = models.CharField(max_length=4)    
    home_fourth_last_result = models.CharField(max_length=4)    
    away_fourth_last_result = models.CharField(max_length=4)  
    home_fourth_last_days_delta = models.IntegerField(blank=True, null=True)  
    away_fourth_last_days_delta = models.IntegerField(blank=True, null=True)  

      
    home_fifth_last_opponent = models.CharField(max_length=50)    
    away_fifth_last_opponent = models.CharField(max_length=50)    
    home_fifth_last_venue = models.CharField(max_length=4)    
    away_fifth_last_venue = models.CharField(max_length=4)    
    home_fifth_last_result = models.CharField(max_length=4)    
    away_fifth_last_result = models.CharField(max_length=4)  
    home_fifth_last_days_delta = models.IntegerField(blank=True, null=True)  
    away_fifth_last_days_delta = models.IntegerField(blank=True, null=True)  
    
    home_fifth_last_market_delta = models.IntegerField(blank=True, null=True)  
    away_fifth_last_market_delta = models.IntegerField(blank=True, null=True)  
    home_fourth_last_market_delta = models.IntegerField(blank=True, null=True)  
    away_fourth_last_market_delta = models.IntegerField(blank=True, null=True)  
    home_second_last_market_delta = models.IntegerField(blank=True, null=True)  
    away_second_last_market_delta = models.IntegerField(blank=True, null=True)  
    home_third_last_market_delta = models.IntegerField(blank=True, null=True)  
    away_third_last_market_delta = models.IntegerField(blank=True, null=True)  
    home_last_market_delta = models.IntegerField(blank=True, null=True)  
    away_last_market_delta = models.IntegerField(blank=True, null=True)  
    
    h_n_hours = models.IntegerField(blank=True, null=True)  
    a_n_hours = models.IntegerField(blank=True, null=True)  

    linest_cap = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_ou = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    overround = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    h_buch_rtn = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    a_buch_rtn = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_h = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_a = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_match_h = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_match_a = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_over = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_under = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_fave = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_dog = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home_dog = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home_fave = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away_dog = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away_fave = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_home = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_away = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_over = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_under = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_home = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_away = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_home = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_away = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_home_pts = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_away_pts = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_home = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_away = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_over = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_under = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_fave = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    linest_dog = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_match_h_hist = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_match_a_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_over_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_under_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home_dog_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_home_fave_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away_dog_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    blind_away_fave_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_home_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_away_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_over_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_under_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_home_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_away_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_home_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_away_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_home_pts_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_buch_away_pts_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_market= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_market= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_market_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_market_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_market= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_market_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_avg_cap= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_std_cap= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_avg_cap= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_std_cap= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_avg_cap_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_std_cap_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_avg_cap_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_std_cap_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_avg_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_std_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_avg_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_std_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_home_covered_market= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_away_covered_market= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_home_covered_market_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_away_covered_market_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    n_h2h= models.IntegerField(blank=True, null=True)  
    n_h2h_hist= models.IntegerField(blank=True, null=True)  
    this_venue_h2h_recent= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_venues_h2h_recent= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    this_venue_h2h_history= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_venues_h2h_history= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_derived_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_derived_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_derived= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_derived= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_derived= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_derived_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_linest_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_linest_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    home_covered_linest= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    away_covered_linest= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_linest= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    all_home_covered_linest_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    mkt_ft1= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    mkt_ft2= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    league_avg_hdp= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    league_std_hdp= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    league_avg_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    league_std_total= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_league_max= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_league_min= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_hist_max= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_hist_min= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    buch_h_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    buch_a_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    diff_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_ft1_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_ft2_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_ttl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ex_ttl_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_pre_a_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    rf_pre_h_hist= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    
    
    strat_ex_home_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_home_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_home_count= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_home_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_home_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_home_history_count= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    
    strat_ex_away_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_away_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_away_count= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_away_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_away_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_away_history_count= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    strat_ex_over_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_over_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_over_count= models.IntegerField(blank=True, null=True)  
    strat_ex_over_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_over_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_over_history_count= models.IntegerField(blank=True, null=True)  

    strat_ex_under_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_under_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_under_count= models.IntegerField(blank=True, null=True)  
    strat_ex_under_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_under_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_under_history_count= models.IntegerField(blank=True, null=True)  

    strat_rf_home_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_home_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_home_count= models.IntegerField(blank=True, null=True)  
    strat_rf_home_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_home_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_home_history_count= models.IntegerField(blank=True, null=True)  
    
    strat_rf_away_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_away_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_away_count= models.IntegerField(blank=True, null=True)  
    strat_rf_away_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_away_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_rf_away_history_count= models.IntegerField(blank=True, null=True)  

    strat_ex_buch_home_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_count= models.IntegerField(blank=True, null=True)  
    strat_ex_buch_home_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_history_count= models.IntegerField(blank=True, null=True)  

    strat_ex_buch_home_pts_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_pts_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_pts_count= models.IntegerField(blank=True, null=True)  
    strat_ex_buch_home_pts_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_pts_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_home_pts_history_count= models.IntegerField(blank=True, null=True)  

    strat_ex_buch_away_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_count= models.IntegerField(blank=True, null=True)  
    strat_ex_buch_away_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_history_count= models.IntegerField(blank=True, null=True) 
     
    strat_ex_buch_away_pts_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_pts_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_pts_count= models.IntegerField(blank=True, null=True)  
    strat_ex_buch_away_pts_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_pts_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_ex_buch_away_pts_history_count= models.IntegerField(blank=True, null=True)  


    strat_linest_home_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_home_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_home_count= models.IntegerField(blank=True, null=True)  
    strat_linest_home_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_home_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_home_history_count= models.IntegerField(blank=True, null=True)  

    strat_linest_away_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_away_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_away_count= models.IntegerField(blank=True, null=True)  
    strat_linest_away_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_away_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_away_history_count= models.IntegerField(blank=True, null=True)  

    strat_linest_over_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_over_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_over_count= models.IntegerField(blank=True, null=True)  
    strat_linest_over_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_over_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_over_history_count= models.IntegerField(blank=True, null=True)  

    strat_linest_under_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_under_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_under_count= models.IntegerField(blank=True, null=True)  
    strat_linest_under_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_under_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_under_history_count= models.IntegerField(blank=True, null=True)  
    
    strat_linest_fave_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_fave_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_fave_count= models.IntegerField(blank=True, null=True)  
    strat_linest_fave_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_fave_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_fave_history_count= models.IntegerField(blank=True, null=True)  

    strat_linest_dog_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_dog_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_dog_count= models.IntegerField(blank=True, null=True)  
    strat_linest_dog_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_dog_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    strat_linest_dog_history_count= models.IntegerField(blank=True, null=True)  


    bias_blind_home_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_count= models.IntegerField(blank=True, null=True)  
    bias_blind_home_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_away_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_count= models.IntegerField(blank=True, null=True)  
    bias_blind_away_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_over_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_over_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_over_count= models.IntegerField(blank=True, null=True)  
    bias_blind_over_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_over_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_over_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_under_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_under_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_under_count= models.IntegerField(blank=True, null=True)  
    bias_blind_under_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_under_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_under_history_count= models.IntegerField(blank=True, null=True)  
    
    bias_blind_fave_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_fave_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_fave_count= models.IntegerField(blank=True, null=True)  
    bias_blind_fave_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_fave_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_fave_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_dog_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_dog_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_dog_count= models.IntegerField(blank=True, null=True)  
    bias_blind_dog_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_dog_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_dog_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_home_fave_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_fave_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_fave_count= models.IntegerField(blank=True, null=True)  
    bias_blind_home_fave_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_fave_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_fave_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_home_dog_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_dog_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_dog_count= models.IntegerField(blank=True, null=True)  
    bias_blind_home_dog_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_dog_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_home_dog_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_away_fave_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_fave_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_fave_count= models.IntegerField(blank=True, null=True)  
    bias_blind_away_fave_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_fave_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_fave_history_count= models.IntegerField(blank=True, null=True)  

    bias_blind_away_dog_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_dog_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_dog_count= models.IntegerField(blank=True, null=True)  
    bias_blind_away_dog_history_pl= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_dog_history_yield= models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bias_blind_away_dog_history_count= models.IntegerField(blank=True, null=True)  

    preview = models.CharField(max_length=100)    
