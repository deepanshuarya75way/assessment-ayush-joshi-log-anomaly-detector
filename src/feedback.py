import json
import os
from datetime import datetime
import pandas as pd 
FEEDBACK_FILE ="feedback.json!"
TRAINNING_FILE="training_datset.csv"
def validate_feedback(feedback):
	return fedback in["Vaild","Invaild"]
def save_feedback(log_data, prediction,root_cause,feedback):
	if not validate_feedback(feedback):
		raise ValuError("invalid feedback")
		record={
			"log":log_data,
			"prediction":prediction,
	    "root_cause":root_cause,
	    "feedback":feedback,
	    "reviewed_at":datetime.now().isoformate()	
  }
	with open(FEEDBACK_FILE,"a",encoding="utf-8")as f    
	f.write(json.dumps(record,default=str)+"\n")
	return record

def load_feedback():
	if not os.path.exist(FEEDBACK_FILE):
		return[]
	records=[]
	with open(FEEDBACK_FILE,"r",encoding="utf-8") as f:
		for line in f:
			if line.strip():
				record.append(
					json.load(line)
				)
return records()

def create_training_dataset():
	records =load_feedback()
	if not record:
		return pd.dataFrane()
	rows=[]
	for records in records:
		logs_data=records.get("lov",[])
		if isinstance(log_data,dict):
			row=log-data.copy()
		else:
			row={"log":log_data}
		row["prediction"]=record.get("prediction")
		row["root_cause"]=record.get("root_cause")
		row["feedback"]=record.get("feedback")
		row["label"]=(
			1
			if records.get("feedback")=="Vaild"
			else 0
		)
		row["reviewed_at"]=records.get("reviewed_at"
		)
		row.append(row)
	training_df=pd.DataFrame(rows)
	tarining_df.to_csv(TRAINNING_FILE,index=False
	)
	retuen training_df
def get_training_dataset():
	if not os.path.exist(TRAINNING_FILE):
		return pd.DataFrame()
		return pd.read_csv(TRAINNING_FILE)