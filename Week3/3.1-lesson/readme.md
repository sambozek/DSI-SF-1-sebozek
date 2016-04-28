---
title: Regression Metrics & Loss Functions
duration: "1:25"
creator:
    name: Marc Harper
    city: LA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lesson Title
Week # | Lesson #

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Explain and Use RMSA (Root Mean Squared Error)
- Explain and Use MAE (Mean Absolute Error)
- Compute these regression metrics with scikit-learn
- Fit a Least Absolute Deviations line to data with statsmodels


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Fit a linear regression with scikit-learn
- Compute the sum of squared errors
- Understand outliers

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Topic description  |
| 10 min  | [Introduction](#introduction)   | Loss functions  |
| 15 min  | [Demo](#demo)  | RMSE and MAE  |
| 25 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | Real Data is Noisy  |
| 25 min  | [Independent Practice](#ind-practice)  | Topic description  |
| 5 min  | [Conclusion](#conclusion)  | Topic description  |

---

<a name="opening"></a>
## Opening (5 mins)
- Review prior labs/homework, upcoming projects, or exit tickets, when applicable
- Review lesson objectives
- Discuss real world relevance of these topics
- Relate topics to the [Data Science Workflow](https://drive.google.com/file/d/0Bx2SHQGVqWasOGY4dE95OFVvZjQ/view?usp=sharing) - i.e. are these concepts typically used to acquire, parse, clean, mine, refine, model, present, or deploy?

**Check:** Ask students to define, explain, or recall outliers, sum of squared
errors, loss functions.

> Use the included [jupyter notebook]() for the entire lesson, including the guided
and independent practice.

<a name="introduction"></a>
## Introduction: Loss functions (10 mins)

**Check:** What's the difference between MAE and RMSE?

<a name="demo"></a>
## Demo: RMSE and MAE (15 mins)

> You can do this or have students do it.

Compute the RMSE and MAE of the sample data set by hand. Compare the size
of the terms. Add in the outlier and repeat.

**Check**: Which regression metric is more affected by the outlier?

<a name="guided-practice"></a>
## Guided Practice: Real Data is Noisy (25 mins)

In real world data sets there is usually a lot of noise, from many sources. For
example, there are errors from lack of precision in measurement instruments,
errors due to data entry mistakes, and many others. Can you think of any more?

In the guided and independent practice, we'll see how MAE and RMSE perform on
noisy datasets.

<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)


> Grab the [solution code](code/Regression-Metrics-and-Loss-Functions-Solutions.ipynb) here.

**Check:** Were students able to create the desired deliverable(s)? Did it meet requirements / constraints?


<a name="conclusion"></a>
## Conclusion (# mins)
- Review any independent practice deliverable(s)

- Recap topic(s) covered in short takeaway bullet points

- Describe homework or any upcoming tasks

***

### UPCOMING ASSIGNMENTS
|   |   |  |
|---|---|---|
| **HOMEWORK** | [Example Assignment](#)  | Session Due |
| **PROJECTS**  | [Project Title](#)  | Session Due |

### ADDITIONAL RESOURCES

- [Nice paper on RMSE versus MAE](http://www.geosci-model-dev.net/7/1247/2014/gmd-7-1247-2014.pdf)

