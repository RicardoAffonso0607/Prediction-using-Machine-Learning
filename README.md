# Prediction using Machine Learning

## Overview
This is a simple machine learning project implemented in Python. The project focuses on training two different IA's to predict results.   

With the "main.py" file, there is two databases, the "clients.csv" (to train the IA's) and the "new_clients.csv" to make the predictions.

## Libraries used
- [SciKit Learn](https://scikit-learn.org/stable/index.html): Used for train the IA's and make the predictions.
- [Pandas](https://pandas.pydata.org/): Used for data manipulation.

## How do I make it?
First, I had used the Pandas library to open the "clients.csv" file. The SciKit Learn library have been used after to prepare the data (dividing the data into training and test).

With all this ready. I've used the "RandomForestClassifier()" and "KNeighborsClassifier()" models to train the IA and decide which one is better.

Calculing the accuracy, I found: the RandomForest got 82,46% and the KNeighbors 73,24%.

For this reason, I utilized the RandomForest to make the prediction in the "new_clients.csv" file.

That was the prediction:

<img src="https://github.com/RicardoAffonso0607/Prediction-using-Machine-Learning/assets/127418054/34624387-ce4d-46cc-aa75-e3ba14f69b96" />

Here we can see that it predicted the first client is a "Poor" choice, the second one is a "Good" choice and the third one is "Standart".

After that, I was curious to find what colummn was the most important to the decision calculation.

<img src="https://github.com/RicardoAffonso0607/Prediction-using-Machine-Learning/assets/127418054/8eec5eaa-e100-4e73-b098-ade23cb14917" />

Interpreting this data, we can see the "debt", "credits" and "loan interest" weighs the most.

## How to Run

1. Clone the repository:
   ````bash
   git clone https://github.com/RicardoAffonso0607/Prediction-using-Machine-Learning
2. Make sure that you've already installed the Pandas and SciKit Learn libraries:
   ```bash
   pip install pandas
   pip install –U scikit-learn
3. Unzip the files
4. Run the Project:
   ```bash
   python main.py # Windows
   python3 main.py # Linux

## Conclusion

This project was important to understand how the basics of Machine Learning work in Python.

## Acknowledgments

Thank Hashtag Programação for making the databases available and to guide me in this project. Please follow them in YouTube: https://www.youtube.com/@HashtagProgramacao

