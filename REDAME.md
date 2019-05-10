# Multivision Project

This project was developed by Multivision team. Based on a scraping test, developers proponents have to solve one challenge demonstrate that understand the basic concept of scraping web pages. It's a pre-test to qualify each likely future team member.


## Getting Started

This `Readme` file will help you understand how the Multivision project was solved and run it on your local machine.


### Prerequisites

First of all you need to install the package Anaconda in your computer. Go to [Anaconda Web Page](https://www.anaconda.com/) download and install that package into your machine. The Anaconda has python included so you don't need to download and install python as well. It's a self explanatory and easy installation.


### Setup Scrapy

Now that you have installed Anaconda use windows search tool (botton on left screen of your computer) and type `Anaconda Prompt`. The prompt will be open and you have to type follow instruction into it:

```
conda install -c conda-forge scrapy
```
From now on you have installed in your machine Scrapy framework that will create a better condition to handle and crawl a large amount of data.


## The Scrapy Process

These are the basics steps followed to write the code for scraping the web page provided.

* open https://www.drukzo.nl.joao.hlop.nl/python.php web site
* quick overview on html code from web page provided - using right click and press `inspect`
* open anaconda prompt
* type `scrapy shell`
* run a crawler on web site using the `fetch('https://www.drukzo.nl.joao.hlop.nl/python.php')` command
* print html code from web page using `print(response.text)` command
* create a scrapy project with all basic folder structure
* create a standard `spider` called `drukso.py`
* costumize `drukso.py` code
* modify `settings.py` file to export a csv data file
* get back to scrapy shell and run the spider using the command `scrapy crawl test`

Step by step code line comments can help to understand scrapping process too. We recommend read carrefully each comment line code. 

