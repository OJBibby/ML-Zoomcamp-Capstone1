import bentoml
from typing import Literal
from bentoml.io import JSON
from pydantic import BaseModel

class FraudDetection(BaseModel):
	age: int
	sex: Literal['female', 'male']
	bmi: float
	children: int
	smoker: Literal['yes', 'no']
	region: Literal['northwest', 'northeast', 'southwest', 'southeast']

model_ref = bentoml.xgboost.get("fraud_detection_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("fraud_detection_classifier", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=FraudDetection), output=JSON())
def classify(fraud_info):
	fraud_data = fraud_info.dict()
	vector = dv.transform(fraud_data)
	prediction = model_runner.predict.run(vector)
	return prediction