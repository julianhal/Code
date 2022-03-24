investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    return bitcoin_amount*bitcoin_value_usd

# 2) use function to calculate if the investment is below $30,000
    if (bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)) < 30000:
        print('Value low!!!')


# 2) use function to calculate if its below $30,000