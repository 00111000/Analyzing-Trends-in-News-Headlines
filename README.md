# Analyzing Trends in News Headlines
---

* Performed data analysis of news headlines by
	* Scraping websites and
	* Extracting metadata for each news headline using IBM's Watson Natural Language Understanding API
* Explored data by plotting charts to uncover patterns and trends
* Recorded the findings in a Jupyter Notebook

## Visualizations from the notebook

![Most Frequently Mentioned Countries](https://github.com/00111000/SCREENSHOTS/blob/master/v1.png)

![Most Famous President/Prime Minister](https://github.com/00111000/SCREENSHOTS/blob/master/v2.png)
![Sentiment Composition of All Headlines](https://github.com/00111000/SCREENSHOTS/blob/master/v3.png)

## There is always room for improvements...

* Improving the code
	*  This was my first time using Python modules such as `matplotlib`, `pandas`, and `numpy`. To end up with the desired chart, the datasets were manipulated using `pandas`. The methods used to manipulate the datasets were not the most ideal. It is in my plans to shorten the code as well as improve my understanding of `dataframes` and `series`.
* Getting rid of redundant datasets
	* In my current notebook, I am using 7 different datasets, which were manipulated to the contain the desired data using `JSON_to_CSV.py`. This is not the ideal solution, in the future, I am planning on getting rid of the  other 6 sets, while keeping the `Complete.csv` set and manipulating it using `pandas` to derive the other sets.

## Technologies used

* Watson NLU API
* Python (matplotlib, pandas, numpy)
* Jupyter Notebooks
