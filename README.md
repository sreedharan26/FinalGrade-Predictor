# FinalGrade-Predictor
This is a basic Machine Learning model which can able to predict the **"Final Grade"** of students based on different attributes.
The attributes/labels that are included in finding the target are:
  * **G1**
  * **G2**
  * **StudyTime**
  * **Failures**
  * **Absences**
## Steps involved in making this project:
  ### 1)Analysing the data
  First we need to have the dataset file in which we need to identify the labels and the target
  ### 2)Choosing a model
  In this model I have selected the **linear-regression** model which chooses a **BFL**(Best Fit Line) for the predictions of Final Grade
  ### 3)Splitting the Data
  Here in this case I splitted the data into two parts 
    * Training data - 90% of total data
    * Testing data - 10% of total data
  ### 4)Training the model
  After giving the data i.e both input and output to the model, it gets trains on the data.
  We can get the BFL from this step.
  Our model's BFL's co-efficients of each label came out as follows
  <img width="682" alt="Screenshot 2023-08-14 at 6 16 19 PM" src="https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/99a89c97-53fc-4317-8fc9-e6c8173c7377">
  and the intercept as 
  <img width="272" alt="Screenshot 2023-08-14 at 6 18 38 PM" src="https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/263e6b28-8736-463b-af1d-6a00736a03b7">
  and the accuracy of the model came out as **82.4%**
  ### 5)Testing the model
  After training the model we need to give the x_test(testing data of x-axis) we will get the predictions of the given data and then we can compare the predicted values to the original value.
  ### 6)Plotting the graph:
    * BFL between "G3" and "G1"
      ![G1](https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/550db4e7-0468-43bc-8745-2be82b85db8f)
    * BFL between "G3" and "G2"
      ![G2](https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/c2eda65a-92f9-4cbf-8ff7-b02c548861e8)
    * BFL between "G3" and "studytime"
      ![studytime](https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/e7fd8e5a-4c15-41ad-b956-bb862fe892f5)
    * BFL between "G3" and "failures"
      ![failures](https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/f5a21810-5030-4fb4-bdfb-30e9ead11f51)
    * BFL between "G3" and "absences"
      ![absences](https://github.com/sreedharan26/FinalGrade-Predictor/assets/60042786/20ff9b1b-7617-4127-a787-f60027ffd30c)

    
