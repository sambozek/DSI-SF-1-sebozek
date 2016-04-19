---
title: iPython Notebooks, Data Values, CSV Library
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) iPython Notebooks, Data Values, CSV Library
Week 1 | Lesson 3.2

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Demonstrate how to use the notebook, code vs Markdown mode
- Show how to save and share the notebook via Jupyter
- Intro to csv library

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Install Anaconda
- Create an Anaconda environment with iPython Notebook installed
- From iPython Notebook, install Jupyter


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   |  Anaconda, iPython notebook, Jupyter, Code vs. Markdown, and csv library |
| 10 min  | [Demo / Guided Practice ](#demo)  | Anaconda  |
| 10 min  | [Demo / Guided Practice ](#demo)  | iPython notebook  |
| 10 min  | [Demo / Guided Practice ](#demo)  | Jupyter  |
| 10 min  | [Demo / Guided Practice ](#demo)  | Code vs. Markdown  |
| 10 min  | [Demo / Guided Practice ](#demo)  | csv library  |
| 30 min  | [Independent Practice](#ind-practice)  |  |
| 5 min  | [Conclusion](#conclusion)  |   |



<a name="Anaconda, iPython notebook, Code vs. Markdown, and csv library"></a>
## Introduction: (5 mins)

Anaconda is a completely free Python distribution. It includes more than 400 
of the most popular Python packages for science, math, engineering, and data analysis.
[Anaconda](https://www.continuum.io/downloads)

iPython Notebook is an interactive computational environment, in which you 
can combine code execution, rich text, mathematics, plots and rich media.
[iPython Notebook](http://ipython.org/notebook.html)

The Jupyter Notebook is a web application that allows you to create and share 
documents that contain live code, equations, visualizations and explanatory text. 
Uses include: data cleaning and transformation, numerical simulation, 
statistical modeling, machine learning and much more.
[Jupyter](http://jupyter.org/)

Lastly, we will take a peek at the csv library. 


<a name="Anaconda"></a>
## Demo / Codealong: Anaconda (10 mins)

For those of you who haven't installed Anaconda yet. Please go to the 
[Anaconda website](https://www.continuum.io/downloads) and follow the install 
instructions for your OS. Any questions, please ask the instructor, TA, or a 
fellow student. 

<a name="iPython Notebook"></a>
## Demo / Codealong: iPython Notebook (10 mins)

iPython Notebook comes as part of Anaconda. When you launch Anaconda there should 
be the ability to install iPython Notebook. 


<a name="Jupyter"></a>
## Demo / Codealong: Jupyter (10 mins)

Lastly, let's install Jupyter. Open up a new iPython notebook and type: 

```bash
pip install jupyter 
```

to install Jupyter. And then, we're off! 


<a name="Code vs. Markdown"></a>
## Demo / Codealong: Code vs. Markdown (10 mins)

Let's play around with iPython Notebook first to get a feel for it. Let's create a new notebook by clicking on the "New" dropdown and selecting under "Notebooks", "Python 2". Let's change the title right away to
something like "Practice", so we can easily ID it later. 

The notebook starts off in the "Code" mode, which means that the cell is ready to accept
any code we write. Let's toggle it to "Markdown" mode. Practice writing a cell of code and
then a cell of Markdown and run it. 

Next, click through the dropdown menus: File, Edit, View, Insert, Cell, Kernel, and Help, 
just to get a look at what's available. Don't worry, you'll become more familiar with 
these through usage. 

Let me show you how to use Jupyter to display an .ipynb file in 
[Jupyter's NBviewer](https://nbviewer.jupyter.org/). Remember, it must be PUBLICLY
available and not PRIVATE in order to work. Now, create your own Jupyter/iPython Notebook, 
upload it to your GitHub account, make it publicly available, and then view it through
Jupyter's NBviewer. 

<a name="csv module"></a>
## Demo / Codealong: csv module (10 mins)

Let's take a look at the Python csv module. The csv module’s reader and 
writer objects read and write sequences. We'll be using a small Sales data set
to practice. Let's read a csv file first. 
[demo code](https://github.com/generalassembly-studio/dsi-course-materials/blob/W1-L3.2-ready-to-merge/curriculum/04-lessons/week-01/3.2-lesson/code/Demo%20Code%20-%20Week%201%20Lesson%203.2%20-%20iPython%20Notebooks%2C%20Data%20Values%2C%20CSV%20Library.ipynb)

In iPython notebook type: 
```bash
import csv
print 'Opening File. Data: '
print ''
with open('sales.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
f.close()
print ''
print 'file closed'   # Always remember to close the file after writing to it!
```

The output will be the contents of sales.csv file. Now, let's write to a csv file. 

In iPython notebook type: 
```bash
print 'Adding the following record: '
data = ['123456', 'cosmos', 'neil', 'lucy', 'universe', '1', '1,000,000', 'presented']
print ''
print data
with open('sales.csv', 'a') as fp:
    a = csv.writer(fp, delimiter=',')
    fp.write('\n')
    a.writerows([data])
    
fp.close()
print ''
print 'file closed'    # Always remember to close the file after writing to it!
```

Now, let's see the file again, with the data you just added: 
```bash
print 'The new data that was just added, can be seen on the last line: '
with open('sales.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

f.close()
print ''
print 'file closed'
```


<a name="ind-practice"></a>
## Independent Practice: Topic (30 minutes)
- Practice creating an Jupyter/iPython Notebook that uses both code and MarkDown cells. 
Upload it to GitHub, make it publicly available, and then view it through Jupyter's NBviewer. 
- Practice reading and writing csv files. 


<a name="conclusion"></a>
## Conclusion (5 mins)
Today we were introduced to Anaconda, iPython Notebook, Jupyter, and how to read and write csv files. 
Nice. Next we'll be introduced to NumPy. Sounds like fun!
