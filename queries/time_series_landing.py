from secret.private import VIEW_ID
from settings import config

print(config)

request_body = {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': config['date_start'], 'endDate': config['date_end']}],
          'metrics': [{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:date'},{'name':'ga:browser'},{'name':'ga:pagePath'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": []
              }
            ],
          "pageSize":"10000"
        }]
      }