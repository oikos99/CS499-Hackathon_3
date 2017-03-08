# CS499-Hackathon_3
Google Maps Traffic Prediction



### URL to the frontend Traffic Prediction Page
http://ec2-52-33-204-53.us-west-2.compute.amazonaws.com:5000

 
 
 
### API to receive the sample data SYNTAX
http://ec2-52-33-204-53.us-west-2.compute.amazonaws.com:5000/save?road_id=5&direction=1&dayOfWeek=5&timeOfDay=14&traffic_status=7

### API to prediction the traffic status SYNTAX
http://ec2-52-33-204-53.us-west-2.compute.amazonaws.com:5000/predict?road_id=5&direction=1&dayOfWeek=5&timeOfDay=14


tI used the SCIKIT-LEARN machine learning algorithm's Support Vector Machines (SVM) class to model our traffic prediction.  SVM is set of supervised learning methods used for classification, regression and outliers detection.  It is more effective than Linear Regression especially in high dimensional spaces.  In our traffic prediction, it is ideal because our data consists multiple dimensions and a potential large number of dimensions is greater than the number of samples.  Our SVC uses gamma value of 0.001 and C=100.
Below is an illustration of the SVC model from the SCIKIT-LEARN website:
![](/svm_model.png)
