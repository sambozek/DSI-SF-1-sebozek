
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project # 4: Web Scraping, Logistic Regression, and kNN

### Description

This week, we learned about web scraping and logistic regression. Now, we're going to put both of these skills to the test!

You're working as a data scientist for a government contracting firm that's rapidly expanding. Now that they have their most valuable employee (you!), they need to leverage data to win more contracts. Your firm offers technology and scientific solutions and wants to be competitive in the hiring market. Your principal thinks the best way to gauge salary amounts is to take a look at what the Federal Government themselves pays for these professionals.

The Federal Government regularly posts job openings for internal positions on its job site, [usajobs.gov](https://www.usajobs.gov), as a means of seeking new talent. Often, the Federal Government and private firms, like your contracting firm, compete for potential employees from the same talent pool. Your job is to understand what factors most directly impact salaries and effectively and accurately find clients appropriate jobs.

#### Project Summary

In this project, we're going to be using a dataset that you will scrape from the web and clean. We're working with real world data, so prepare to get your data hands dirty!

Your job is to:

1. Collect data from [USAJobs](http://www.usajobs.gov) on Federal hiring for your analysis.
2. Find out what factors most directly impact Federal employee salaries (Title, location, department, etc.). In this case, we do not want to predict mean salary as would be done in a regression. Your boss believes that salary is better represented in categories than continuously
  - Select and parse data from at least 1000 postings for jobs, potentially from multiple job title searches.
  - Choose 3 pairs of salary categories (i.e. one pair might be: [25k-50k vs. 100k-125k]) and build logistic regressions that predict the probability of one category over the other given other predictors scraped from the site.
  - Test, validate, and describe your models. What factors predict salary category? How do your models perform?
3. Sometimes clients come to your firm with specific constraints. For example, a client may have a strict requirement for location, job title/category, and department, and want to know given that what salary to expect.
  - The most common combinations of constraints and requests clients come to you with are:
    1. Given their location and position info (full time, part time, etc.), what department should they expect to work in?
    2. Given department and agency, what salary category should they expect?
    3. Given salary category, department, and agency, are they more likely to find jobs for U.S. citizens or federal employees?
  - Select 2 categories of job based on title (your preference) with sufficient postings. Construct kNN models to answer the three client constraint questions above for each category.
  - Cross-validate one or more of your kNN models. How does changing the neighbors affect the performance?
4. Author a report to your Principal detailing your analysis.

**BONUS PROBLEMS:**
1. Your boss would rather tell a client incorrectly that they would get a lower salary job than tell a client incorrectly that they would get a high salary job. Adjust one of your logistic regression models to ease his mind, and explain what it is doing and any tradeoffs. Plot the ROC curve.
2. Text variables and regularization:
  - **Part 1**: Job descriptions contain more potentially useful information you could leverage. Scan descriptions for words you think would be important and add them as predictors to a model.
  - **Part 2**: Make a logistic regression for one of your salary category models with at least 30 predictors (word presence variables from bonus pt. 1 can get you here..). Gridsearch parameters for Ridge and Lasso for this model and report the best model.
3. Construct a multinomial logistic regression that can predict between all salary categories. Add more job title categories than you had originally to give your model better power. Evaluate the performance of your multinomial model.


**Goal:** Scrape & clean data, run logistic regression and kNN, derive insights, present findings.

---

### Requirements

- Scrape and prepare your data using [Import.io](https://www.import.io) and Pandas.
- A Jupyter Notebook with your regression analysis for a peer audience of data scientists.
- A written report directed to your (non-technical!) Principal

 **Pro Tip:** You can find a good example report [here](https://www.dlsweb.rmit.edu.au/lsu/content/2_assessmenttasks/assess_tuts/reports_ll/report.pdf).

- ***Non-statistical Bonuses:***
 - Generate your data manually using the Python package [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#). OR scrapy with xpath!
 - Create a blog post of at least 500 words (and 1-2 graphics!) describing your data, analysis, and approach. Link to it in your Jupyter notebook.

---

### Necessary Deliverables / Submission

- Materials must be in a clearly labeled Jupyter notebook.
- Materials must be pushed to student's github master branch.
- Materials must be submitted by the end of Week 5.

---

### Dataset

1. We'll be utilizing a dataset derived from live web data: [USAJobs](https://www.usajobs.com)

2. To get the data, use import.io or the BeautifulSoup package to scrape the webpage.

---

### Suggested Ways to Get Started

- Read in your dataset
- Write pseudocode before you write actual code. Thinking through the logic of something helps.  
- Read the docs for whatever technologies you use. Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success!
- Document **everything**.
- Look up sample executive summaries online.

### Additional Resources
- [Advice on How to Write for a Non-Technical Audience](http://programmers.stackexchange.com/questions/11523/explaining-technical-things-to-non-technical-people)
- [Documentation for BeautifulSoup can be found here](http://www.crummy.com/software/BeautifulSoup/).

---

### Project Feedback + Evaluation

[Attached here is a complete rubric for this project.](./project-04-rubric.md)

Your instructors will score each of your technical requirements using the scale below:

    Score | Expectations
    ----- | ------------
    **0** | _Incomplete._
    **1** | _Does not meet expectations._
    **2** | _Meets expectations, good job!_
    **3** | _Exceeds expectations, you wonderful creature, you!_

 This will serve as a helpful overall gauge of whether you met the project goals, but __the more important scores are the individual ones__ above, which can help you identify where to focus your efforts for the next project!
