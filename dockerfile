#Using the base image with python 3.7
FROM python:3.8

#Set our working directory as app
WORKDIR /app 
#Installing python packages pandas, scikit-learn and gunicorn
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Copy the models directory and server.py files
ADD /app.py app.py
ADD /configs.py configs.py
ADD /final_fit.pkl final_fit.pkl
ADD /variables.pickle variables.pickle
#Exposing the port 1313 from the container
EXPOSE 1313
#Starting the python application
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]