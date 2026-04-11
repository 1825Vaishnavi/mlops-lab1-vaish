# FastAPI Lab - Wine Classifier API

## Overview
This lab demonstrates how to expose an ML model as an API using FastAPI and uvicorn.
Modified from the original Iris classifier to use the **Wine dataset** with enhanced API features.

## Changes Made from Original
| Original | My Version |
|---|---|
| Iris dataset (4 features) | Wine dataset (13 features) |
| Predicted class number only | Predicts class + wine name |
| No health endpoint | Added `/health` endpoint |
| Generic API title | Custom title & description |

## Project Structure
FastAPI_Labs/
├── model/
│   └── wine_model.pkl
├── src/
│   ├── data.py       # WineData & WineResponse models
│   ├── main.py       # FastAPI app with 3 endpoints
│   ├── predict.py    # Model loading & prediction logic
│   └── train.py      # Train Decision Tree on Wine dataset
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Create & activate virtual environment
```bash
python -m venv fastapi_lab1_env
.\fastapi_lab1_env\Scripts\activate
```

### 2. Install dependencies
```bash
pip install scikit-learn fastapi uvicorn pydantic
```

### 3. Train the model
```bash
cd src
python train.py
```

### 4. Run the API
```bash
uvicorn main:app --reload
```

### 5. Open API docs
Go to: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Check if API is running |
| POST | `/predict` | Predict wine type |

## Sample Request
```json
{
  "alcohol": 13.2,
  "malic_acid": 1.78,
  "ash": 2.14,
  "alcalinity_of_ash": 11.2,
  "magnesium": 100.0,
  "total_phenols": 2.65,
  "flavanoids": 2.76,
  "nonflavanoid_phenols": 0.26,
  "proanthocyanins": 1.28,
  "color_intensity": 4.38,
  "hue": 1.05,
  "od280_od315": 3.4,
  "proline": 1050.0
}
```

## Sample Response
```json
{
  "predicted_class": 0,
  "wine_type": "Barolo"
}
```

## Wine Classes
| Class | Wine Type |
|---|---|
| 0 | Barolo |
| 1 | Grignolino |
| 2 | Barbera |

## Dataset
- **Name:** Wine Dataset (sklearn built-in)
- **Features:** 13 chemical properties of wine
- **Classes:** 3 wine types
- **Model:** Decision Tree Classifier (max_depth=4)

## Author
Vaishnavi Gajarla  
Northeastern University  


