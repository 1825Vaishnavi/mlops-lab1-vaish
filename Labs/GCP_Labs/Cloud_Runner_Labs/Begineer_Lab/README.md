# Cloud Run Beginner Lab

## Overview
This lab demonstrates deploying a containerized Flask application on Google Cloud Run.

## Modifications Made (Different from original repo)
- Added `/about` route displaying my name
- Added `/health` route for health check
- Modified home route with custom welcome message

## Live Deployment URL
https://vaishnavi-cloud-app-1024717028832.us-central1.run.app

## Test Routes
- Home: https://vaishnavi-cloud-app-1024717028832.us-central1.run.app/
- About: https://vaishnavi-cloud-app-1024717028832.us-central1.run.app/about
- Health: https://vaishnavi-cloud-app-1024717028832.us-central1.run.app/health

## Project Structure
Begineer_Lab/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

## Steps Followed
1. Created GCP project `cloud-runner-lab`
2. Enabled Cloud Run API and Artifact Registry API
3. Created modified Flask app with 3 routes
4. Built Docker image
5. Pushed image to GCP Container Registry
6. Deployed to Google Cloud Run
7. Tested all routes successfully

## Author
**Vaishnavi Gajarla**
Northeastern University
