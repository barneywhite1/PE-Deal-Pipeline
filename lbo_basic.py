# ----- Assumptions (money in £m) -----
entry_ebitda = 2        # company's earnings when the PE firm buys it
entry_multiple = 6      # price paid = 6 x EBITDA
debt = 8                # how much is borrowed to buy it
exit_ebitda = 3         # earnings when the PE firm sells it
exit_multiple = 7
       # sale price = 6 x EBITDA
remaining_debt = 8      # loan still owed at the sale
years = 5               # how long the PE firm owns it

# Equations for buying the company
purchase_price = entry_ebitda * entry_multiple
equity = purchase_price - debt

# Equations for selling the company 
sale_price = exit_ebitda * exit_multiple
money_back = sale_price - remaining_debt

# These are the relevant equations used
moic = money_back / equity
total_return = moic - 1
irr = moic ** (1 / years) - 1

# This shows the results from the combination of above
print(f"Purchase price: £{purchase_price}m")
print(f"PE firm invests: £{equity}m")
print(f"Sale price: £{sale_price}m")
print(f"PE firm gets back: £{money_back}m")
print(f"MOIC: {moic:.2f}x")
print(f"Total return: {total_return:.0%}")
print(f"IRR: {irr:.1%}")