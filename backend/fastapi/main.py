from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.get("/decision")
async def make_decision(input_data: str):
    try:
        logging.info("Received decision request")
        # Simulate decision making process
        result = {"decision": "approve", "confidence": 0.95}
        return result
    except Exception as e:
        logging.error(f"Error processing decision: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")