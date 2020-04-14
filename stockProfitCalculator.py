class StockProfitCalculator:

    def __init__(self):
        self.result = {
            "symbol": "",
            "proceeds": 0.0,
            "cost": 0,
            "totalPurchasePrice": 0,
            "buyCommission": 0,
            "sellCommission": 0,
            "capitalTaxGain": 0,
            "netProfit": 0,
            "roi": 0,
            "breakEven": 0
        }

    def calculateProfit(self, data):

        #getting data from the request form
        symbol = data.get('symbol')
        allotment = float(data.get('allotment'))
        finalSharePrice = float(data.get('finalSharePrice'))
        sellCommission = float(data.get('sellCommission'))
        initialSharePrice = float(data.get('initialSharePrice'))
        buyCommission = float(data.get('buyCommission'))
        capitalGainRate = float(data.get('capitalGainRate'))

        #calculating proceeds
        proceeds = allotment * finalSharePrice

        #calculating total purchare price
        totalPurchasePrice = allotment * initialSharePrice
        commissions = sellCommission + buyCommission

        grossProfit = totalPurchasePrice + commissions
        capitalGainTax = (capitalGainRate / 100) * (proceeds - grossProfit)

        #calculating net profit
        netProfit = (proceeds - grossProfit) - capitalGainTax

        #calculating cost
        cost = proceeds - netProfit

        #calculating rate of interest
        roi = round((netProfit / cost) * 100, 2)

        #calculating break even
        breakEven = (totalPurchasePrice + commissions) / 100

        #assigning the values back to class variables
        self.result["symbol"] = symbol
        self.result["proceeds"] = proceeds
        self.result["totalPurchasePrice"] = totalPurchasePrice
        self.result["cost"] = cost
        self.result["sellCommission"] = sellCommission
        self.result["buyCommission"] = buyCommission
        self.result["capitalTaxGain"] = capitalGainTax
        self.result["netProfit"] = netProfit
        self.result["roi"] = roi
        self.result["breakEven"] = breakEven

        return self.result