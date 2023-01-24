# Bank Account Fraud Detection
Data used is sampled from a larger dataset from: https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022.  
Data was sampled using the script contained in sample.py. As the original dataset was heavily imbalanced, undersampling was used.

It is important for banks to be able to detect fraudulent activity in order to protect the bank's, and customer's, interests.  
This model could be used to flag activity for closer inspection.
The return will be the probability that an instance is fraudulent.

# Creating the model service:

Enter pipenv by typing:

	pipenv install
	pipenv shell

To build the model run:

	python train.py

To start the service type:

	bentoml serve service.py:svc

Model will be running on localhost:3000

To containerize via bentoml type (make sure docker is running):

	bentoml build

	bentoml containerize fraud_detection_classifier:latest

To then run through docker type (replace image id with id generated in last step):

	docker run -it --rm -p 3000:3000 <image id> serve --production

Alternatively to pipenv, run through docker using my Dockerfile by typing (might take some time):

	docker build -t fraud-detection .
	docker run -p 3000:3000 -it --rm fraud-detection

Model was hosted on AWS using the commands in ./cloud_pics/cloud_prep.txt.
Screenshots of model running on the AWS cloud and a response from the cloud are in ./cloud_pics/.
