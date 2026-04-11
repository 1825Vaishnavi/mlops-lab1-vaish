from fastapi import FastAPI, HTTPException
from data import WineData, WineResponse
from predict import predict_wine

app = FastAPI(
    title="Wine Classifier API",
    description="Classifies wine type using a Decision Tree model trained on the Wine dataset",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Wine Classification API!"}

@app.get("/health")
async def health():
    return {"status": "running", "model": "DecisionTreeClassifier", "dataset": "Wine"}

@app.post("/predict", response_model=WineResponse)
async def predict(data: WineData):
    try:
        result = predict_wine(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))