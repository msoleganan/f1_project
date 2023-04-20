
import requests
import fastf1 as ff1
from fastf1 import plotting
import pandas as pd
import requests
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz


def results(year,locations,session):
    """Session must be introduced as a string.
    Years needs to be introduced as a string.
    Location needs to be introduced as a list. This is to get results, weather and laptimes per race."""
    laptime_list=[]
    weather_list=[]
    results_list=[]
    locals()[str(year)+"_"+session+"laptime"]=pd.DataFrame()
    locals()[str(year)+"_"+session+"weather"]=pd.DataFrame()
    locals()[str(year)+"_"+session+"race_results"]=pd.DataFrame()
    
    
    for location in locations:
        race_year=ff1.get_session(year,location,session)
        race_year.load()
        locals()["laptime_"+str(session)+"_"+str(year)+"_"+str(location)]=pd.DataFrame(race_year.load_laps(with_telemetry=True))
        locals()["laptime_"+str(session)+"_"+str(year)+"_"+str(location)]['year']=year
        locals()["laptime_"+str(session)+"_"+str(year)+"_"+str(location)]['Location']=location
        locals()[str(year)+"_"+session+"laptime"]=pd.concat([locals()["laptime_"+str(session)+"_"+str(year)+"_"+str(location)],
                                                                                                    locals()[str(year)+"_"+session+"laptime"]])
        locals()["weather_"+str(session)+"_"+str(year)+"_"+str(location)]=pd.DataFrame(race_year.weather_data)
        locals()["weather_"+str(session)+"_"+str(year)+"_"+str(location)]['year']=year
        locals()["weather_"+str(session)+"_"+str(year)+"_"+str(location)]['Location']=location
        locals()[str(year)+"_"+session+"weather"]=pd.concat([locals()["weather_"+str(session)+"_"+str(year)+"_"+str(location)]
                                                                                                   ,locals()[str(year)+"_"+session+"weather"]])
        locals()["race_results_"+str(session)+"_"+str(year)+"_"+str(location)]=pd.DataFrame(race_year.results)
        locals()["race_results_"+str(session)+"_"+str(year)+"_"+str(location)]['year']=year
        locals()["race_results_"+str(session)+"_"+str(year)+"_"+str(location)]['Location']=location
        locals()[str(year)+"_"+session+"race_results"]=pd.concat([locals()["race_results_"+str(session)+"_"+str(year)+"_"+str(location)],locals()[str(year)+"_"+session+"race_results"]])

    return locals()[str(year)+"_"+session+"laptime"],locals()[str(year)+"_"+session+"weather"],locals()[str(year)+"_"+session+"race_results"]


def status_cleaning(data):

    '''This is to aggregate the different status that a driver could finish the race'''

    data.loc[data['status'].str.contains('Lap'),'clean_status']='Overlap'
    data.loc[data['status'].str.contains('Finished'),'clean_status']='Finished'
    data.loc[data['status'].str.contains('Accident|Collision damage|Damage|Spun off'),'clean_status']='Accident'
    data.loc[data['status'].str.contains('Disqualified|Excluded|Not classified'),'clean_status']='Disqualified/Not qualified'
    data.loc[data['status'].str.contains('Tyre|Puncture'),'clean_status']='Tyre Problem'
    data.loc[data['status'].str.contains('Injury|Illness|Exhaust'),'clean_status']='Driver issue'
    data.loc[data['status'].str.contains('Withdrew|Retired'),'clean_status']='Retired'
    data.clean_status.fillna('Car Problem',inplace=True)


def string_to_miliseconds(x):
    """Here we will transfrom a string into miliseconds"""
    x=str(x)
    if 'n' in x or 'N' in x or x==None:
        return None
    else:
        minutes=int(x[:x.find(':')])*60000
        seconds=int(x[x.find(':')+1:x.find('.')])*1000
        milesimas=int(x[x.find('.')+1:])
        
        return minutes+seconds+milesimas