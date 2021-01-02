# libraries to import
import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

# Input stock-list:
stocks_name = input("Enter the stock Names separated by a space > ").split()
Stocks = stocks_name
print(Stocks)


def func(stocks):           # Passing list as a argument
    f_data = []             # Creating a empty list to store the final data
    for stock in stocks:    # looping through the list argument

        # URL of Nse India
        nse = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock

        # defining Headers
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

        # getting the page using request library and assigning that data to page
        page = requests.get(nse, headers=headers)

        # Parse the HTML file(page) into the Beautiful Soup and one also needs to specify his/her parser. Here we are taking html parser.
        soup = BeautifulSoup(page.content, 'html.parser')

        # Finding the Element By ID
        data = soup.find(id='responseDiv').getText()

        # converting the data into json dictionary
        data = json.loads(data)

        # Accessing the data key from data dictionary
        data = data["data"]

        # using loop to get dictionaries
        # defaultdict used to make default empty list
        # for each key
        res = defaultdict(list)
        for sub in data:
            for key in sub:
                res[key].append(sub[key])

        # converting the data into a dictionary
        data = dict(res)

        # appending the required data to the f_data list
        f_data.append(f"""
        Stock : {stock}
            Open: {"".join(data["open"])}
            High: {"".join(data["dayHigh"])}
            Low: {"".join(data["dayLow"])}
            Close: {"".join(data["closePrice"])}
            Volume: {"".join(data["quantityTraded"])}
            Delivery percentage: {"".join(data["deliveryToTradedQuantity"])} % """)
    # returning the data as a List
    return f_data


# func = func(Stocks)
# for i in func:
#     print(i)
