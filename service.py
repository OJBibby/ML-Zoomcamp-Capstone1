import bentoml
from typing import Literal
from bentoml.io import JSON
from pydantic import BaseModel

class FraudDetection(BaseModel):
	income: float
	name_email_similarity: float
	current_address_months_count: int
	customer_age: int
	days_since_request: float
	intended_balcon_amount: float
	payment_type: Literal['AA', 'AB', 'AC', 'AD', 'AE']
	zip_count_4w: int
	velocity_6h: float
	velocity_24h: float
	velocity_4w: float
	bank_branch_count_8w: int
	date_of_birth_distinct_emails_4w: int
	employment_status: Literal['CA', 'CB', 'CC', 'CD', 'CF']
	credit_risk_score: int
	email_is_free: int
	housing_status: Literal['BA', 'BB', 'BC', 'BD', 'BE']
	phone_home_valid: bool
	phone_mobile_valid: bool
	bank_months_count: int
	has_other_cards: bool
	proposed_credit_limit: float
	foreign_request: bool
	source: Literal['INTERNET', 'TELEAPP']
	session_length_in_minutes: float
	device_os: Literal['windows', 'linux', 'macintosh', 'x11', 'other']
	keep_alive_session: bool
	device_distinct_emails_8w: int
	month: int


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