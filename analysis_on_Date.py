from tools import *

#Amount of Rating Per day of a year
df.groupby('date')['rating'].size()
# April 1, 2008        28
# April 1, 2009        21
# April 1, 2010        16
# April 1, 2011        12
# April 1, 2012        21
#                      ..
# September 9, 2013    44
# September 9, 2014    45
# September 9, 2015    90
# September 9, 2016    99
# September 9, 2017    55
plt.title("Amount of Rating Per day of a year")
df.groupby('date')['rating'].size().plot(figsize=(20,10))

#Distributtion of Review Per Year
plt.title("Amount of Review Per day of a year")
df.groupby('date')['review'].size().plot(figsize=(20,10))
#Amount of Reviews Per Year


#Using DatetimeIndex
grouped_date = df.groupby(df['date']).agg({'rating': np.mean, 'review': np.size, 'usefulCount': np.sum})
grouped_date['date'] = grouped_date.index
grouped_date['date'] = pd.DatetimeIndex(grouped_date['date'])
grouped_date = grouped_date.set_index('date')
#Result:
# date	          rating	review	usefulCount		
# 2008-04-01	8.285714	28	2303
# 2009-04-01	7.666667	21	3698
# 2010-04-01	7.812500	16	342
# 2011-04-01	8.583333	12	216
# 2012-04-01	9.238095	21	1178
# ...	...	...	...
# 2013-09-09	8.295455	44	1941
# 2014-09-09	8.800000	45	2935
# 2015-09-09	5.733333	90	1901
# 2016-09-09	6.777778	99	1728
# 2017-09-09	5.127273	55	298
#This counts average ratng per day of a year, numer of reviews per day of a year, and the sum of usefulCount per day of a year

#From grouped date we can extract different information based on date for example plot of means of ratings in 2010
plt.title("Avarege Rating in 2010")
grouped_date['2010']['rating'].plot(figsize=(15,10))

#We can also extract information about month 
#This are numer of reviews written in may of 2009
plt.title("Number of reviews in May 2009")
grouped_date['2009-05']['review'].plot(figsize=(15,10))
plt.show()
grouped_date.loc['2009-05']['review']
# 2009-05-01    27
# 2009-05-10    25
# 2009-05-11    34
# 2009-05-12    39
# 2009-05-13    32
# 2009-05-14    24
# 2009-05-15    26
# 2009-05-16    24
# 2009-05-17    31
# 2009-05-18    19
# 2009-05-19    21
# 2009-05-02    23
# 2009-05-20    38
# 2009-05-21    34
# 2009-05-22    25
# 2009-05-23    21
# 2009-05-24    31
# 2009-05-25    18
# 2009-05-26    25
# 2009-05-27    19
# 2009-05-28    36
# 2009-05-29    33
# 2009-05-03    37
# 2009-05-30    18
# ...
# 2009-05-06    26
# 2009-05-07    39
# 2009-05-08    31
# 2009-05-09    37