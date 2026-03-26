from fastapi import FastAPI
from pydantic import BaseModel
from agents import run_demographic_agent, run_financial_agent, run_manager_agent

app = FastAPI(title="Eco-Guard API", description="نظام التحقق من بيانات المسوحات الأسرية")

class SurveyRecord(BaseModel):
    age: int
    marital_status: str
    education: str
    occupation: str
    family_size: int
    region: str
    income: float
    actual_expenses: float
    housing_type: str
    electricity_bill: float

@app.get("/health")
def health():
    return {"status": "running", "system": "Eco-Guard"}

@app.post("/agent/demographic")
def demographic(record: SurveyRecord):
    result = run_demographic_agent(record.dict())
    return result

@app.post("/agent/financial")
def financial(record: SurveyRecord):
    result = run_financial_agent(record.dict())
    return result

@app.post("/agent/manager")
def manager(record: SurveyRecord):
    demo = run_demographic_agent(record.dict())
    financial = run_financial_agent(record.dict())
    result = run_manager_agent(demo, financial, record.dict())
    return result

@app.post("/analyze")
def analyze(record: SurveyRecord):
    demo = run_demographic_agent(record.dict())
    financial = run_financial_agent(record.dict())
    manager = run_manager_agent(demo, financial, record.dict())
    return {
        "demographic": demo,
        "financial": financial,
        "manager": manager
    }