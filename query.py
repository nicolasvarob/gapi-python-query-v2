from secret.private import VIEW_ID
from settings import config

def request(date_start,date_end):
    return {
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': date_start, 'endDate': date_end }],
          'metrics': [{'expression': 'ga:uniquePurchases'},{'expression':'ga:itemQuantity'},{'expression': 'ga:revenuePerItem'},{'expression':'ga:itemRevenue'},{'expression':'ga:itemsPerPurchase'}],
          'dimensions': [{'name': 'ga:transactionId'},{'name':'ga:productName'},{'name': 'ga:productCategoryHierarchy'},{'name':'ga:productCouponCode'}],
           "dimensionFilterClauses": [
              {
                "operator":"AND",
                "filters": [{
                    "dimensionName": "ga:landingPagePath",
                    "not":"true",
                    "expressions": ["/compra/confirmacion"]
                  }
                ]
              }
            ],
          "pageSize":"10000"
        }]
      }