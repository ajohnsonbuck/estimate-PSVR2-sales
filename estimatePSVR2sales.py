'''
Copyright Alex Johnson-Buck, 2023

Sony PSVR2 Hardware Sales Estimation:
    Subreddit subscribers historically exhibit a linear correlation with sales of hardware.
    However, the ratio of hardware sales to subscribers is highly platform- and subreddit-dependent.

    Using the historical correlation between r/PSVR subscribers and PS VR sales from 2016-2022, this method
    predicted PS VR2 sales of 684,000 within the first month.
    A consulting firm hired by Bloomberg, IDC, predicted about 270,000-300,000 sales through March 2023, about 6 weeks after launch.
    Sales figures released by Sony indicated 580,000 units of PS VR2 sold in the first 6 weeks, so my estimate (27% error)
    was considerably closer than that of IDC/Bloomberg (51% error), despite being based on the simple metric of 
    subreddit statistics.
    
    I further found very strong linear correlation (R^2 > 0.99) between the reported PS VR2 sales by Sony in the first 
    6 weeks and the subscriber numbers of the r/PSVR and r/psvr2 subreddits.
    
    I have used these more recent linear regression fits to create updated estimates of PS VR2 sales.
    r/psvr2 and r/PSVR give two indepedent estimates, allowing a crude estimate of uncertainty (68% and 95% CIs).
    
    This script extracts the subscriber numbers from r/PSVR and r/psvr2 and estimates units of PS VR2 sold up to the
    present date, as well as 66 and 95% confidence intervals.
    
    The validity of this method will be tested when the next batch of sales figures are released by Sony.
'''

import re
import requests
import numpy as np

# Send a GET request to subreddit stats pages, which will serve as sales indicators
url1 = 'https://subredditstats.com/r/PSVR'  # Sales indicator 1: r/PSVR
url2 = 'https://subredditstats.com/r/psvr2' # Sales indicator 2: r/psvr2
response1 = requests.get(url1)
response2 = requests.get(url2)

# Extract the subscriber count using regex
subscriber_count1 = re.search(r'"subscriberCount":\s*(\d+)', response1.text)
if subscriber_count1:
    subscriber_count1 = int(subscriber_count1.group(1))

subscriber_count2 = re.search(r'"subscriberCount":\s*(\d+)', response2.text)
if subscriber_count2:
    subscriber_count2 = int(subscriber_count2.group(1))

# Correction factors for June 12-14 Reddit blackout, determined as y-offset between pre- and post-blackout linear regression fits
corr1 = 395
corr2 = -297

# Estimate the number of units sold
if type(subscriber_count1) == int and type(subscriber_count2) == int:
    estimatedSales1 = int((subscriber_count1+corr1)*12.7254212 - 2093024.62) # extrapolated from linear regression fit of first 6 weeks of sales vs r/PSVR subscriber numbers
    estimatedSales2 = int((subscriber_count2+corr2)*138.7529435 + 161976.97) # extrapolated from linear regression fit of first 6 weeks of sales vs r/PSVR2 subscriber numbers
    
    estimatedSales = int(np.mean([estimatedSales1,estimatedSales2])) # average of estimates from both subreddits
    
    sd = np.std([estimatedSales1,estimatedSales2],ddof=1)
    CI95 = int(2*sd)
    CI68 = int(sd)
    print('Estimated sales:', estimatedSales,"+/-",CI95, " (95% CI)")
    print('                ', estimatedSales,"+/-",CI68, " (68% CI)")
else:
    print('Error: values not extracted correctly.')