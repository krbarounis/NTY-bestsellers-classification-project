# NYT-bestsellers-classification-project

## Intro

This classification project aims to predict if a book will appear on any of the New York Times bestseller lists.

## Tech Stack

- Python
    - Requests
    - Selenium
    - Beautiful Soup
    - Pandas
    - Matplotlib
    - Seaborn
    - Scikit-learn
    
## Process

I gathered data through the New York Times' Book API as well as by scraping GoodReads.com. Bestsellers from 2017 to the present were sourced from the NYT API, while non-bestsellers from 2017-2018 were sourced from GoodReads. Ultimately, features for each book (both bestsellers and non-bestsellers) were also scapred from GoodReads.


## The Data & EDA

In order to both prepare and understand the data prior to running models, I completed a number of preprocessing/cleaning steps as well as exploritory data analysis. 

### Observations:

- 1646 total observations
    - 551 bestsellers
    - 1095 non-bestsellers
    
### Features

- Part of a series (Y/N)
- Goodreads rating (based on user input)
- Goodreads genre (based on most user tags)
- Top author (Y/N) (list of Forbes' top earning authors 2017 & 2018)
- Publishing company
- Month of publishing

### Visuals

As part of the EDA process, I created a number of visuals using Python's Matplotlib and Seaborn libraries. 

![](/Plots/Top_authors.png)

![](/Plots/Publish_month_and_rating.png)

![](/Plots/Ratings.png)

![](/Plots/Top_5_publishing_companies.png)


## Modeling

I ran a variety of classification models. Here I have only highlighted the baseline model and the final model. For a look at the full set of models, refer to the "Modeling" notebook in this repo. In selecting a "final model," I chose to focus on accuracy score as the best measure of evaluating models. This is due to the fact that I view a false positive and a false negative as having equal importance. In the first case (false positive), the model would predict a book to be a bestseller when in fact it is not. In the latter case (false negative), the model would predict that a book would not be a bestseller, when in fact it was. From the perspective of a publishing company, the first case is a bad investment (the company would make less than expected on a particular book given the incorrect prediction that it would be a bestseller) and the second case is a missed opportunity (the company would miss out on the chance to make money on a bestselling book given the model's incorrect prediction).

### Baseline: Dummy Classifier

I used Sklearn's Dummy Classifier (parameter for strategy was "most frequent") to create a baseline model. This model looks at the distibution of the data across classes and predicts each observation as the most frequent class. In this case, a larger proportion of the observations were non-bestsellers, so the model always predicted that a book was not a bestseller. As a result, the model had an accuracy score (67-68%) roughly equal to the distribution of the data by class (66% non-bestsellers) with the difference attributed to the fact that the data was split into training and testing sets, so the exact distribution varied.

![](/Plots/Confusion_Matrix_baseline.png)

The confusion matrix shows that no observations were classified as positives (bestsellers) since those made up the less frequent class. The model correctly classified 220 negatives (true negatives) and incorrectly classified 108 negatives (false positives). The latter are the observations in the test set that were in fact bestsellers.

### Final Model: Logistic Regression

The model which performed the best in terms of accuracy was Logistic Regression with Sklearn's default parameters (i.e. C of 1 and penalty parameter of L1). 

![](/Plots/Confusion_Matrix_Log.png)

The confusion matrix shows that the model correctly predicted 41 positives and 202 negatives, while incorrectly classifying 20 negatives and 67 positives for a final accuracy score of ~74%. Given the class imbalance of the data set, the model performed better when classifying the more frequent class (negatives).

#### Parameters

- Penalty: L1 or L2
EXPLAIN

- C: C=1/lamdba
EXPLAIN



## Future Improvements:

- More bestsellers: The NYT API returned multiple duplciate values and due to time constraints, I was not able to gather additional bestsellers in time for modeling. As a result, there was class imbalance present in my data set (2/3 of the data were not bestsellers) so the model performed better when classifying negative cases.

- Additional features: I would like to use NLP to 







