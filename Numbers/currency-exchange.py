# Exercise Instructions

# Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him. Here are his specifications for the app:

# Task 1 - Create the exchange_money() function, taking 2 parameters:

    # budget : The amount of money you are planning to exchange.
    # exchange_rate : The amount of domestic currency equal to one unit of foreign currency.

# This function should return the value of the exchanged currency.

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

# Task 2 - Create the get_change() function, taking 2 parameters:

    # budget : Amount of money before exchange.
    # exchanging_value : Amount of money that is taken from the budget to be exchanged.

# This function should return the amount of money that is left from the budget.

def get_change(budget, exchanging_value):
    return budget - exchanging_value

# Task 3 - Create the get_value_of_bills() function, taking 2 parameters:

    # denomination : The value of a single bill.
    # number_of_bills : The total number of bills.

# This exchanging booth only deals in cash of certain increments. The total you receive must be divisible by the value of one "bill" or unit, which can leave behind a fraction or remainder. Your function should return only the total value of the bills (excluding fractional amounts) the booth would give back. Unfortunately, the booth gets to keep the remainder/change as an added bonus.

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

# Task 4 - Create the get_number_of_bills() function, taking amount and denomination.

# This function should return the number of currency bills that you can receive within the given amount. In other words: How many whole bills of currency fit into the starting amount? Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly. Effectively, you are rounding down to the nearest whole bill/denomination.

def get_number_of_bills(amount, denomination):
    return amount//denomination

# Task 5 - Create the get_leftover_of_bills() function, taking amount and denomination.

# This function should return the leftover amount that cannot be returned from your starting amount given the denomination of bills. It is very important to know exactly how much the booth gets to keep.

def get_leftover_of_bills(amount, denomination):
    return amount - (denomination * (amount//denomination))

# Task 6 - Create the exchangeable_value() function, taking budget, exchange_rate, spread, and denomination.

# Parameter spread is the percentage taken as an exchange fee, written as an integer. It needs to be converted to decimal by dividing it by 100. If 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be: 1.00 EUR == 1.32 USD because 10% of 1.20 is 0.12, and this additional fee is added to the exchange.

# This function should return the maximum value of the new currency after calculating the exchange rate plus the spread. Remember that the currency denomination is a whole number, and cannot be sub-divided.

# Note: Returned value should be int type.

def exchangeable_value(budget, exchange_rate, spread, denomination):
    return (int((budget / (exchange_rate * (1 + (spread/100)))) // denomination)) * denomination