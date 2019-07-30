import pandas as pd
import datetime

from secret.private import client_id, client_secret, redirect_uri, access_code, access_token, refresh_token
from config.initialize_analytics import initialize_analyticsreporting
from components.to_df import response_to_df

from queries.time_series_landing import request_body
from query import request
#from components.analyse.correlation.cross_correlation import analyse as analysis

# INPUT
## Query report from Analytics
def get_report(analytics,start,end):
  ## Use the Analytics Service Object to query the Analytics Reporting API V4.
  return analytics.reports().batchGet(
      body=request(start,end)
  ).execute()

def main():
  ## Initialize
  config = initialize_analyticsreporting()
  def generateDateRange(year,month,day,numdays):
    base = datetime.datetime(year,month,day)
    date_list = [(base - datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(numdays)]
    return date_list

  ## Get response
  dates = generateDateRange(2019,6,1,60)
  
  ## Concatena dataframe iterando rango de fechas
  df_full = pd.DataFrame()
  for d in dates:
    print('procesando día ' + d)
    response = get_report(config,d,d)
    ## Convert response to dataframe
    df = response_to_df(response)
    df_full = pd.concat([df_full,df])
  ## OUTPUTVisualise Dataframe 
  return df_full
def dailyBatch():
  a = main()
  a.to_csv('out.csv')
dailyBatch()
