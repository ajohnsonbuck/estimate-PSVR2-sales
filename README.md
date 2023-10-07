# estimate-PSVR2-sales
Estimate hardware unit sales of Sony PS VR2 based on relevant subreddit statistics

# Extended Description

Subreddit subscribers historically exhibit a linear correlation with sales of hardware.
However, the ratio of hardware sales to subscribers is highly platform- and subreddit-dependent.

Using the historical correlation between r/PSVR subscribers and PS VR sales from 2016-2022, this method
predicted PS VR2 sales of 684,000 within the first month.
A consulting firm hired by Bloomberg, IDC, predicted about 270,000-300,000 sales in the same period.
Sales figures released by Sony indicated 580,000 units of PS VR2 sold in the first 6 weeks, so my estimate (27% error)
was considerably closer than that of IDC/Bloomberg (51% error), despite being based on the simple metric of 
subreddit statistics.

I further found very strong linear correlation (R^2 > 0.99) between the reported PS VR2 sales by Sony in the first 
6 weeks and the subscriber numbers of the r/PSVR and r/psvr2 subreddits.

I have used these more recent linear regression fits to create updated estimates of PS VR2 sales.
r/psvr2 and r/PSVR give two indepedent estimates, allowing a crude estimate of uncertainty (68% and 95% CIs).

This script extracts the subscriber numbers from r/PSVR and r/psvr2 and estimates units of PS VR2 sold up to the
present date, as well as 66 and 95% confidence intervals.

In May 2023, the two estimates from r/PSVR and r/psvr2 were quite close, but have since diverged considerably,
leading to large uncertainty in the estimate.  

However, as of October 7, 2023 the most likely range of unit sales is **727,000-959,000** (68% CI).

The validity of this method will be tested when the next batch of sales figures are released by Sony.
