import numpy as np

## Task 1: extract columns
stock_data = np.genfromtxt('stock_prices_intro.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

dates = stock_data['Date']
#print(dates)

openp = stock_data['Open']
#print(openp)

closep = stock_data['Close']
#print(closep)

vol = stock_data['Volume']
#print(vol)

## Task 2: calculate daily returns
rate = (closep - openp) / openp * 100
print(f'Date: {dates[0]}, Return rate: {rate[0]}\n'
      f'Date: {dates[1]}, Return rate: {rate[1]}\n'
      f'Date: {dates[2]}, Return rate: {rate[2]}\n'
      f'Date: {dates[3]}, Return rate: {rate[3]}\n'
      f'Date: {dates[4]}, Return rate: {rate[4]}')

## Task 3: Calculate statistics
rate_mean = np.mean(rate)
rate_median = np.median(rate)
rate_std_dev = np.std(rate)

print(f'\nMean Daily Return: {rate_mean.round(2)}\n' 
      f'Median Daily Return: {rate_median.round(2)}\n' 
      f'Daily Return Standard Deviation: {rate_std_dev.round(2)}')

## Task 4: Identify best and worst trading days
best_day = np.argmax(rate)

print(f'\nBest Trading Day: {dates[best_day]}\n'
    f'Best Trading Day Open: {openp[best_day]}\n'
    f'Best Trading Day Close: {closep[best_day]}\n'
    f'Best Trading Day Rate: {rate[best_day].round(2)}'
        )

worst_day = np.argmin(rate)
print(f'\nWorst Trading Day: {dates[worst_day]}\n'
    f'Worst Trading Day Open: {openp[worst_day]}\n'
    f'Worst Trading Day Close: {closep[worst_day]}\n'
    f'Worst Trading Day Rate: {rate[worst_day].round(2)}\n'
        )

## Task 5: Analyze up and down trading days
positive_days = rate[rate > 0]

negative_days = rate[rate < 0]

num_positive_days = np.size(positive_days)
posi_days_total = np.sum(positive_days)

num_negative_days = np.size(negative_days)
neg_days_total = np.sum(negative_days)

net_return = posi_days_total + neg_days_total

print(f'Number of positive trading days: {num_positive_days}, Total positive return: {posi_days_total.round(2)}\n'
      f'Number of negative trading days: {num_negative_days}, Total negative return: {neg_days_total.round(2)}\n'
      f'Net return: {net_return.round(2)}')

## Task 6: 
