import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "https://eco-guard-production.up.railway.app")

def call_demographic_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/demographic", json=record, timeout=30)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "score": 0, "issues": [str(e)], "notes": "فشل الاتصال بالوكيل الديموغرافي", "agent": "الوكيل الديموغرافي"}

def call_financial_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/financial", json=record, timeout=30)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "score": 0, "issues": [str(e)], "notes": "فشل الاتصال بالوكيل المالي", "agent": "الوكيل المالي"}

def call_manager_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/manager", json=record, timeout=30)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "trust_score": 0, "issues": [str(e)], "recommendation": "فشل الاتصال بالوكيل القيادي", "agent": "الوكيل القيادي"}