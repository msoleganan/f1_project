READ ME: 

TITLE: PREDICTING THE PROBABILITIES OF FERNANDO ALONSO WINNING THE RACE ON THE SPANISH GRAND PRIX IN 2023.

GOAL

Imagine you are a restaurant and you want to grow with a trend. Then you hear that everybody in SPain is mentioning the 33 in Twitter, but you do not know exactly what is happening. You realized that they want to see the 33rd victory of Fernando Alonso's in his career. 
Then you come up with an idea to gain attention, which is offerring 33% of discount on the meals if Fernado wins the 33 in Spain. However, you want to know what are the probabilities of this happening. 
The idea of this project is to analyze past data to predict the probability of Fernando winning the race and the predicted. The probability of Fernando winning the race is important to understand the the impact on economical terms and too see if it's vaible or not.
In order to do the prediction, we will use two regression models, one for the qualifying and one for the race. In the qualifying we will predict the best laptime and in race we will predict the final position.

DATA USED:

There are multiple sources that we will use to do this project. First we will use different datasets uploaded in Kaggle, that has data from 1950 to 2022. There we can find: lap times, race results, qualifying, information from the circuits and much more.
Also, in order to test our model and do the prediction, we will use data provided by the Fast F1 library, which has data from 2018 to 2023. It gives information about the weather, lap times, results...
Finally, another data source that we have used is the Visual Crossing API. This will be able to tell us on the day of the qualifying at specific place, if it rained or what was the wind speed.  To evaluate the lap times, we have decided to use milliseconds.

REGRESSION MODELS USED:

For this project, we have supervised supervised learning models. We have used different models: decison tree regressor, linear regression, random forest regressor and xgbooster regressor. To value the model, we have used the R2 Score and the Mean Squared Error. We have used grid search (function of hyperparaeter tunning to find the best model possible.)


LIBRARIES USED:

-sklearn
-pickle
-seaborn
-scipy.stats
-xgboost
-pandas
-numpy
-fastf1
-warnings
-imblearn.pipeline
-datetime
-itertools

SOURCES USED:

Formula 1 World Championship - https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

Fast F1- https://theoehrly.github.io/Fast-F1/

Visual Crossing - https://www.visualcrossing.com/
