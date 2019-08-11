## CFO Forecast Code Challenge

#### Files Involved
- forecast_regression.py contains the solution to fill 'Values' column of test_blank.csv
- ** test_filled.csv ** contains test_blank.csv with values predicted and filled. It is the solution file.
- variable_prediction.py contains code to predicting the features that drives churn, gross adds etc

#### forecast_regression.py
to install necessary libraries for the script:
**pip install numpy, pandas, sklearn, tensorflow, keras**

with terminal on the directory with this file:
run **python forecast_regression.py**

- I've commented on the script so that it'll be easier to understand the code. It should be relatively easy to understand.

#### variable_prediction.py
- This script uses the same libraries as the script above.
- I've commented on the script so that it'll be easier to understand the code.
- It should be relatively easy to understand.
- Generic Group Variable is the label while the Product details and it's metrics from Hypothesis.xlsx are the keys

with terminal on the directory with this file:
run **python forecast_regression.py**

wait for the program to run and you'll come across an input:
"Enter data (array)" and then "Enter the top n variables that'll affect churn, gross adds, etc."
- the input here are the predictions after the model (as I didn't have enough time to write the script to process data from those seen in excel format)
- n would be the number of most important variables that the function will return

Entering an array such as:
[1.2019543e-22, 1.3352841e-27, 4.3504810e-13, 2.5440855e-26,
 9.0121055e-18, 1.0095733e-10, 1.8626299e-09, 7.9069368e-17,
 3.2711055e-21, 9.3631720e-11, 6.3767324e-18, 1.9687370e-09,
 3.5194460e-17, 1.2184037e-20, 2.6190970e-15, 1.5767819e-17,
 4.4996452e-21, 1.0000000e+00, 4.5711936e-17, 2.0055728e-09,
 6.2922510e-12, 2.5289669e-22, 9.2655917e-21, 1.2514402e-18,
 1.1675671e-23, 1.4137839e-11, 1.7673137e-17, 1.0174996e-17,
 1.1968977e-23, 3.1412777e-24, 1.3253070e-09, 5.0124684e-27,
 2.3763481e-25, 3.1780266e-17, 3.4947759e-17, 6.2465733e-19,
 1.2959971e-24, 1.1390129e-36, 1.0146667e-31, 2.3080074e-21,
 2.7034470e-19, 1.3017519e-28, 7.2511306e-26, 1.3622046e-16,
 1.5409131e-11, 2.1447596e-22, 1.4987528e-21, 8.9795302e-20,
 4.0344592e-27, 1.4509143e-12, 2.8691121e-19, 1.7765047e-19,
 7.5716092e-24, 3.3958446e-24, 4.7033888e-10, 2.1832254e-23,
 7.5464935e-24, 1.5002807e-09, 9.8280586e-20, 8.2083139e-24,
 3.9283092e-24, 3.5246195e-24, 1.2541986e-09, 6.3535146e-27,
 1.9327128e-29, 1.4118648e-19, 3.8193373e-29, 2.0977046e-17,
 2.0341470e-20, 9.5914694e-18, 1.1199585e-17, 2.4566499e-25,
 1.9823416e-18, 1.9395288e-30]

 and n as:
 2

 will result in
 ['Acquisition Price - Tortoise (Up to Speed 2) Delta (Sandesh Brand 1 VS Non Sandesh Brand 4)', 'Acquisition Price - Tortoise (Up to Speed 2)']

 Using the same array and entering n as 3 will result in:
 ['Acquisition Price - Low Rabbit (Speed 3 to Speed 4)',
 'Acquisition Price - Tortoise (Up to Speed 2) Delta (Sandesh Brand 1 VS Non Sandesh Brand 4)',
 'Acquisition Price - Tortoise (Up to Speed 2)']

'Acquisition Price - Low Rabbit (Speed 3 to Speed 4)]' would be the third most Important factor.
