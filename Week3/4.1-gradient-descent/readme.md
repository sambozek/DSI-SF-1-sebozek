---
title: Gradient Descent
duration: "1:25"
creator:
    name: Marc Harper
    city: LA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lesson Title
Week 3 | Lesson 4.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Basic review of derivatives (should be somewhat in the prework)
- Define the gradient descent algorithm
- Step through example of gradient descent
- When would the gradient descent algo get stuck or fail? Discuss

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Make plots and scatter plots with matplotlib


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
| 10 min  | [Introduction](#introduction)   | Derivatives  |
| 15 min  | [Demo](#demo)  | Gradient Descent  |
| 25 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | Gradient Descent |
| 25 min  | [Independent Practice](#ind-practice)  | Gradient Descent  |
| 5 min  | [Conclusion](#conclusion)  | Topic description  |

---

<a name="opening"></a>
## Opening (5 mins)
- Review prior labs/homework, upcoming projects, or exit tickets, when applicable
- Review lesson objectives
- Discuss real world relevance of these topics
- Relate topics to the [Data Science Workflow](https://drive.google.com/file/d/0Bx2SHQGVqWasOGY4dE95OFVvZjQ/view?usp=sharing) - i.e. are these concepts typically used to acquire, parse, clean, mine, refine, model, present, or deploy?

**Check:** Ask students to define, explain, or recall any relevant prework
concepts such as local minimums of functions, loss functions, derivatives
(if your students have calculus experience).

<a name="introduction"></a>
## Introduction: Derivatives (10-30 mins)

> Review derivatives first. Depending on the mathematics background of your
class you will want to adjust your timing appropriately. There's not enough
time to teach calculus from scratch of course, but you can get a lot of
intuitive understanding out of a good demo and a few analogies.

> How much time you spend on derivatives should depend strongly on the experience
of your students.

> [Derivatives on Khan Academy](https://www.khanacademy.org/math/differential-calculus/taking-derivatives/derivative_intro/v/calculus-derivatives-1)
> [Partial Derivates](https://www.khanacademy.org/math/differential-calculus/taking-derivatives/chain_rule/v/chain-rule-with-triple-composition)

The derivative of a function measures the rate of change of the values of the
function with respect to another quantity.

![tangent](https://upload.wikimedia.org/wikipedia/commons/0/0f/Tangent_to_a_curve.svg)

The gradient is a derivative for multi-variable functions that gives us the
direction in which the function changes most quickly. Not all functions have
derivatives at every point. For example, the absolute value function does not
have a well-defined derivative at the origin because there are many possible
tangent lines:

![absolute value](https://upload.wikimedia.org/wikipedia/commons/6/6b/Absolute_value.svg)

This is one reason why squared error is used as a loss function whenever
possible. Even though we've seen a scenario in which the least absolute
deviation model (LAD) produced a better fit, finding the LAD can be tricky
because of the lack of derivative at the origin. However many loss functions
do have derivatives at every point and we can use derivatives and gradients
to minimize loss functions, thereby finding bit fit models for a variety of
machine learning algorithms.

<a name="demo"></a>
## Demo: Gradient Descent (15-20 mins)

> Use the included [Jupyter notebook](code/starter-code/Gradient-Descent-Starter.ipynb)
to explain the gradient descent algorithm and walk through a demo.

### Advantages and Disadvantages

Advantages:
* Relatively simple algorithm to code, many [packages available](http://scikit-learn.org/stable/modules/sgd.html)
* Efficient (linear complexity in the size of the training set)
* Works for a variety of models

Disadvantages:
* Only works for differentiable functions
* Can get stuck in local minimums (rather than global optimums)
* Can be sensitive to learning rate and scaling
* For smaller datasets other algorithms can outperform gradient descent

**Check:**

<a name="guided-practice"></a>
## Guided Practice: Gradient Descent (# mins)

Work through the examples in this [Worksheet](https://s3-us-west-2.amazonaws.com/ga-dat-2015-suneel/worksheets/Gradient+Descent/GD_worksheet_1.pdf) together.


**Check:** Why does the learning rate make a difference in convergence?
**Check:** On which functions can we use gradient descent?

<a name="ind-practice"></a>
## Independent Practice: TGradient Descent (# minutes)

Complete the [jupyter notebook](code/starter-code/Gradient-Descent-Starter.ipynb) for this exercise.

> [Solution code](code/solution-code/Gradient-Descent-Solution.ipynb)

> **Check:** Were students able to compute the gradients of the example
functions? Do they intuitively understand the use of the gradient even if
their calculus skills are rusty?


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


- [Derivatives on Khan Academy](https://www.khanacademy.org/math/differential-calculus/taking-derivatives/derivative_intro/v/calculus-derivatives-1)
- [Partial Derivates](https://www.khanacademy.org/math/differential-calculus/taking-derivatives/chain_rule/v/chain-rule-with-triple-composition)
- A [nice demo](https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/) of gradient descent for linear regression.

