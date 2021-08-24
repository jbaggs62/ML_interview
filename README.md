
# About Me
ML interview project   
Applicant : Jacob  
Current Role: MLE and Graduate Student
Goal Statement: Looking to leverage past experience in analytics to deliever machine learning model into production.


# App Breakdown 

## Structure
The main code is all in app.py. The test unit test are located in ./test. Various config setup and imports are located in config.py. The pickled model is called final_fit.pkl and the variables that go into the model are variables.pickle. 

## How it works
The code works by using three main functions inside a flask app. There is one parent function that has two smaller functions inside the code that handles the data. The parent function query_example is responsible for getting the request in the form of Post and converting to a dataframe. The cleaning function processes the request using the same data processing steps written in the jupyter notebook. Following the clean the data is then sent to another function, creates final dataframe, that handles the dummy variables for the appropitate fields. Once this data is ready it is then exported out and reloaded in due to a dimensional issue that I was not able to solve in the allotted time frame. The model is than imported and the dataframe uses the statsmodel predict method to come up with the prediction. Following that we then construct our response and return it to our requestor. This is all converted to a docker file that can be built using the build_run.sh script using the code 
~~~
make sure you are in the project root directory 
then run the following commands
bash build_run.sh
~~~ 
If you want to test the code you can run the bash commands below after run the build_run script. The unit test require you to install nose package and unittest. 
~~~
cd ./test
bash ./test.sh
~~~
 ##### * for a more in-depth look into how the code works please review my comments to see how everything works at a more granular level 

## Orchestrating it in the cloud
In order to deal with high demand I would leverage k8s, clouldwatch, load balancer and eks in order to put our code into production and handle large volumes of requests. Leverage cloudwatch alarms and load balancer to help eks spin up additional horizontal scaling of the containers in order to keep our response times low. However, an improvment on this would be using a ML Dev ops services like SageMaker or Kubeflow. This would allow us to gather important metrics such as model drift and handle the container mangement for scaling due to increase in demands. The business partner could call our endpoint via an api gateway and we can return the response to them all in the cloud.


