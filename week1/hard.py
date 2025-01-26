capital = float(input("enter your capital: "))
i_rate = float(input("enter the yearly interest rate: "))
expiry = int(input("enter the expiry time: "))

revenue = (((i_rate/12)*expiry)/100)*capital

print(f"""
      Capital: {capital}
      Expiry: {expiry} month(s)
      Yearly Interest: {i_rate}%
      In {expiry} month(s), the net revenue from {capital}$ with {i_rate} interest is {round(revenue)}$
      """)