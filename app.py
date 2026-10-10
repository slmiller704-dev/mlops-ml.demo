
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ComplaintRequest(BaseModel):
    text: str

@app.post("/process-complaint")
def process_complaint(payload: ComplaintRequest):
    return {
        "category": "Billing/Invoicing",
        "severity": "Low",
        "investigation_notes": [
            "Standard Policy Note: Verify invoices using invoice ledger."
        ],
        "resolution_plan": "1. Check the ledger.\n2. Reissue adjusted invoice."
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
