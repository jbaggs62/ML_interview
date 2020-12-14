
# About Me
ML interview project for State Farm  
Applicant : Jacob Baggs  
Current Role: Data Analyst State Farm and Graduate Student
Role: Machine Learning Engineer Level 1
Goal Statement: Looking to leverage past experience in analytics to deliever machine learning model into production.


# App Breakdown 

## Structure
The main code is all in app.py. The test unit test are located in ./test. Various config setup and imports are located in config.py. The pickled model is called final_fit.pkl and the variables that go into the model are variables.pickle. 

## How it works
The code works by using three main function inside a flask app. There is one parent function that has two smaller function inside the code that handles the data. The parent function query_example is responsible for getting the request in the form of Post and converting to a data frame. The cleaning function process the request using the same data processing steps written in the jupyter notebook. Following the clean the data is than sent to another function, create final dataframe, that handles create the dummy variables for the appropitate fields. Once this data is ready it is then export out and reloaded in due to a dimensional issue that I was not able to solve in the alloted time frame. The model is than imported and the dataframe use the statsmodel predict method to come up with the prediction. Following that we then construct our response and return it to our requestor. This is all converted to a docker file that can be built and test using the build_run.sh script using the code 
~~~
bash build_run.sh
~~~ 
it will run the code and return output based on a precreated request.

 ##### * for a more in depth look in how the code work please review my comments to see how everything works at a more granular level 

## Orchestrating it in the cloud
In order to deal with high demand I would leverage k8s, clouldwatch and eks in order to put our code into production and handle large volumes of request. Leverage cloudwatch alarms to help eks spin up additional horizontal scaling of the containers in order to keep our response times low. However, an improvment on this would be using a ML Dev ops services like SageMaker or Kubeflow. This would allow us to gather important metrics such as model drift and handle the container mangement for scaling due to increase in demands.



## Things that need work still

* unit test, could increase code coverage and make the test better
* dimension issue, there has to be a better way to deal with it for the prediction without create a seperate file.
* k8s orchestrating file 
* ci/cd pipeline so we can rapidly deploy code changes 
* logging, there is always room to improve on logging, so service issue are much faster to respond too
* Terraform files to automatically handle our infrastrucutre via code
* automatic code scans in ci/cd pipeline for sec and quality purpose 


## Final thoughts
I believe this project can complete the business end goal. However as state above there is still a way to go to deliver the optimial solution. In the workplace, I would lean on my team and leverage their experience to better my unit testing, help fix the dimension issue, help creating the k8s file, and feedback on logging. This was an interesting process and I hope you like my solution. I hope to have earn an oppurtunity to interview in person.
