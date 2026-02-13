# Airflow Lab 2 - ML Pipeline

Student: Vaishnavi  
Date:February 13, 2026

## What I Changed

1. Dataset: Advertising → Iris dataset
2. Model: Logistic Regression → RandomForestClassifier
3. Tasks: 6+ tasks → 3 tasks (load → build → email)
4. Owner: Changed to Vaishnavi
5. DAG Name: `Airflow_Lab2_Modified`

## Setup
```bash
# Clone repo
git clone https://github.com/1825Vaishnavi/mlops-lab1-vaish.git
cd mlops-lab1-vaish/Labs/Airflow_Labs/Lab_2

# Start Docker
docker-compose up -d

# Access Airflow
# Open: http://localhost:8080
# Login: airflow / airflow
```

## Run the DAG

1. Go to http://localhost:8080
2. Enable `Airflow_Lab2_Modified`
3. Click Play button ▶️
4. Watch tasks turn green ✅

## Results

- Tasks: 3 (load_data, build_model, send_success_email)
- Runtime: ~5 seconds
- Model Accuracy: 96.67%
- Status:  Working

## Troubleshooting

DAG not showing?
```bash
docker-compose restart
```

 Syntax error
- Check line 46: `joblib.dump(model, '/tmp/model.pkl')`
- Fixed indentation to 4 spaces

## Files

- `dags/airflow_lab2.py` - Main DAG (modified)
- `docker-compose.yaml` - Docker setup
- `model/` - Saved models

---

GitHub:https://github.com/1825Vaishnavi/mlops-lab1-vaish/tree/main/Labs/Airflow_Labs/Lab_2