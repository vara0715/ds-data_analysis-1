import pandas as pd
data = pd.DataFrame.from_dict(
    {
        'Product': ['Table', 'Desktop', 'Bed', 'Dressing Table'],
        'Selling Price': [1500,3000,6000,3800],
        'Profit': [500, 1000, 1200, 800],
        'Shiping mode': ['First Class', 'Second class', 'Same day', 'Standard Class'],
        'Destination': ['Hyderabad', 'Chennai', 'Noida', 'Mumbai'],

    }
)
def surcharge(x):

        if x == "Same day":
            return 0.2
        
        elif x == "First Class":
            return 0.1

        elif x == "Standard Class":
            return 0.5
        else:
            return 0
data["Surcharge"] = data["Shiping mode"].apply(surcharge)
data['Total Cost'] = ((data['Selling Price']-data['Profit'])*(1+data['Surcharge'])).apply(int)
print(data)
