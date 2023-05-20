# Supervised Learning Study Case

This project is a study case following the [Data Science Academy](https://www.datascienceacademy.com.br/course/machine-learning-em-python-e-c) as source.

---

## Text Classification

We use PRAW ([see documentation](https://praw.readthedocs.io/en/stable/)) to scrape posts from reddit. Then we use three different algorithms (KNeighborsClassifier, RandomForestClassifier and LogisticRegressionCVclassify) to determine the main subject that is being discussed in those posts.

We also use Matplotlib and Seaborn to visualize the results achieved by each model.