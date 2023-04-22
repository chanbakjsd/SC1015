# SC1015 - Price the Game

Price the Game is a project for SC1015 (Introduction to Data Science and
Artificial Intelligence).

## Problem Statement

Can we price a game given its publicly available information such as ratings,
genres and number of players?

## Getting Started

This project is built on the [Steam Store Games][dataset] dataset provided by
nikdavis. The dataset must be extracted into the `data/` folder before
running.

The following libraries are used in the project and are therefore required:
- pandas
- seaborn
- matplotlib
- scikit-learn

There are 3 main parts for the project:

1. [Data Preparation/Cleaning][clean-file] -
   This file does the initial pre-processing and generates a `cleaned.csv` when
   it is complete. The `cleaned.csv` file is used by the other two notebooks.

2. [Data Visualization/Exploration][eda-file] -
   This file explores the data given in `cleaned.csv` to show how we might use
   the factors to predict the price.

3. [Machine Learning][ml-file] -
   This file attempts to use machine learning models including linear
   regression, decision tree, random forest, boosting regressors and
   perceptrons to predict the price.

## Conclusion

While the final result is not spectacular as there are other factors that
significantly affect the price of a game, we are able to predict the price of a
game to a certain extent.

## Contributors

- Chan Jie Ying, Jolene - Data Visualization, Data Analysis
- Chan Wen Xu - Data Cleaning, Machine Learning

## References

- A Gentle Introduction to Ensemble Learning Algorithms:
  https://machinelearningmastery.com/tour-of-ensemble-learning-algorithms/
- A New Algorithm for Data Compression:
  http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM ([Archived][new-algo-archive])
- Language Models are Unsupervised Multitask Learners:
  https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf
- Language Models are Few-Shot Learners: https://doi.org/10.48550/ARXIV.2005.14165
- LightGBM (Light Gradient Boosting Machine): https://github.com/Microsoft/LightGBM
- Scikit-Learn's API Reference: https://scikit-learn.org/stable/modules/classes.html
- Seaborn Documentation: https://seaborn.pydata.org/api.html
- XGBoost Documentation: https://xgboost.readthedocs.io/en/stable/index.html

[dataset]: https://www.kaggle.com/datasets/nikdavis/steam-store-games

[clean-file]: https://github.com/chanbakjsd/SC1015/blob/master/0%20Data%20Cleaning.ipynb
[eda-file]: https://github.com/chanbakjsd/SC1015/blob/master/1%20Exploratory%20Data%20Analysis.ipynb
[ml-file]: https://github.com/chanbakjsd/SC1015/blob/master/2%20Machine%20Learning.ipynb

[new-algo-archive]: https://web.archive.org/web/20220523110425/http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM
