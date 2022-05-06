
from statsmodels.tsa.arima_model  import ARIMA
from random import random
# contrived dataset
data = [1,
5,
14,
16,
28,
45,
51,
62,
76,
64,
78,
64,
128,
130,
197,
150,
203,
366,
492,
734,
865,
977,
979,
1580,
2231,
2631,
3450,
4381,
5656,
5298,
4144,
6051,
7788,
8581,
13086,
16766,
19660,
20398,
22609,
23937,
25173,
22348,
25141,
25146,
19872,
19923,
21582,
19831,
17332,
16407,
15861,
15698,
20634,
19657,
18373,
17521,
16200,
15040,
14833,
13646
]
print(data)
predictions=[]
# fit model
model = ARIMA(data, order=(2, 0, 1))
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(20)


yhat2 = yhat[0]
predictions.append(yhat2)

print(predictions)


