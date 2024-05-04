import os
from iracing_connect import iRacingConnect
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    iRacing = iRacingConnect(username, password)

    subsession_id = 64059658
    customer_id = 937417
    car_id = 142
    x_int = 9999999
    x_string = "random"

    # get_result = iRacing.results.summary(subsession_id, 0)
    # get_result = iRacing.results.lap_data(subsession_id, 0)
    # get_result = iRacing.results.event_log(subsession_id, 0)
    # get_result = iRacing.results.lap_chart_data(subsession_id, 0)
    # get_result = iRacing.stats.member_bests(customer_id=customer_id, car_id=car_id)
    # get_result = iRacing.stats.member_yearly(customer_id=customer_id)
    # get_result = iRacing.stats.member_career(customer_id=customer_id)
    # get_result = iRacing.stats.member_recent_races(customer_id=customer_id)
    # get_result = iRacing.stats.member_summary(customer_id=customer_id)

    # get_result = iRacing.stats.membership(customer_id=customer_id)

    ## league
    # get_result = iRacing.league.cust_league_sessions(mine=True, package_id=x_int)
    # get_result = iRacing.league.directory(search=x_string, tag="test")
    # get_result = iRacing.league.get(league_id=x_int, include_licenses=True)
    # get_result = iRacing.league.get_points_systems(league_id=x_int, season_id=x_int)
    # get_result = iRacing.league.membership(
    #     customer_id=customer_id, include_league=False
    # )
    # get_result = iRacing.league.roster(league_id=x_int, include_licenses=True)
    # get_result = iRacing.league.seasons(league_id=x_int, retired=True)
    # get_result = iRacing.league.season_standings(league_id=x_int, season_id=x_int)
    get_result = iRacing.league.season_sessions(
        league_id=x_int, season_id=x_int, results_only=True
    )

    # track
    # get_result = iRacing.track.get()
    # get_result = iRacing.track.assets()

    print(get_result)
