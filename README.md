# MicrosoftBing-search-query-prediction

# Problem statement:
The world is going through COVID-19 pandemic caused due to Novel
Coronavirus and people are mostly in their homes across the world due to
lockdown and they are searching for various things related to Coronavirus on
internet using popular search engines such as Chrome, Bing, Yahoo,
DuckDuckGo etc.     

Now, the problem task is to attempt to explore the intent of the people by just
using the queries (searches) in the last four months Jan to April 2020 and also
build a predicting model which predicts the Country of origin from where the
search query was issued , as search queries made by people can really help in
understanding what’s going in people’s mind during this pandemic and
exploring the queries at global level as well as state level granularity will enable
state and central authorities to take appropriate action and eventually helping
out and benefitting the Citizens.        

# Motivation:      
As a Computer Engineering Student and my deep interested in Machine
learning and Deep learning including NLP tasks, I have my inner passion to
help out researchers / scientists working day and night for helping us by
providing some technological solution using my knowledge.
I have always believed AI can bring great revolutionary ideas in field of
healthcare.         

# Dataset Collection:          
After searching on various platforms, I found the dataset relevant for this
problem and currently only this dataset is actually available for this problem and
Microsoft Bing Team has been very generous to provide the dataset on their
GitHub.         
Dataset Link: https://github.com/microsoft/BingCoronavirusQuerySet         
Some info about dataset:        
* Data range: 2020-01-01 to 2020-04-30       
* All the private data has already been removed by the Bing Team.    
* Only searches that were issued many times by multiple users were
included.      
* Dataset includes queries from all over the world that had an intent related
to the Coronavirus or Covid-19.      


# Methods Explored :   
* Bag oF Words model    
* N-grams model     
* tf-idf model     
* Skim-Gram model       
* Clustering techniques    
* Classification techniques      
  
# Modelling :    
> Preprocessing steps :      
![vis1](/images/text1.png)     
* Tokenization :   
![vis1](/images/text2.JPG)      
![vis1](/images/text3.JPG)      

* Cleaning : 
Removing punctuation, stopwords, HTML tags, XML tags etc.. 




* See reference links at the end for more details. 


> Models  : 


# Deployment and Hosting:     
* The final model which is trained and saved is then loaded and deployed
with Flask backend server and hosted on pythonanywhere.com cloud
service.    
The code for the same is available at my github repo:      
https://github.com/souravs17031999/MicrosoftBing-search-queryprediction     
* Server Link (Live website) :     
https://souravsdlboy.pythonanywhere.com/bing_search      

## Live WebApp : [Server Link](https://souravsdlboy.pythonanywhere.com/bing_search)

# Exploring Data with Sample visualizations :     
![DATA](/images/data.JPG)   
![vis1](/images/vis1.JPG)   
![vis2](/images/vis2.JPG)   
![vis3](/images/vis3.JPG)   
![vis4](/images/vis4.JPG)   
![vis5](/images/vis5.JPG)     
![vis6](/images/webapp.JPG)     


NOTE : For more visualizations, check out the live webapp.

> Few links for references : 
* [Tokenization](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)
* [Cleaning](https://machinelearningmastery.com/clean-text-machine-learning-python/)
* [Normalization](https://en.wikipedia.org/wiki/Text_normalization)
* [Lemmatization](https://en.wikipedia.org/wiki/Lemmatisation)
* [Steaming](https://en.wikipedia.org/wiki/Stemming)


⭐️ this Project if you liked it !

NOTE : Few images are taken from google images and copyrights reserved with their respective owners.
