# Docker Lab 1 - Wine Dataset Classification
## Build the Docker Image
docker build -t wine-model:v1 
## Save the Docker Image
docker save wine-model:v1 > my_image.tar

## Run the Docker Container
docker run wine-model:v1

## Output
Model Accuracy: 94.44%
Wine dataset model training was successful!

## Changes Made
- Changed dataset from Iris to Wine
- Changed model from Random Forest to Decision Tree
- Added accuracy score evaluation
- Updated Python version from 3.10 to 3.11
- Changed test size from 0.2 to 0.3
