# LAB1 - MLOps (IE-7374)

## 📌 Overview

This lab demonstrates the implementation of a Continuous Integration (CI) pipeline using GitHub Actions.

The project includes:
- Creating and managing a virtual environment
- Structuring a GitHub repository
- Implementing Python functions with input validation
- Writing test cases using Pytest and Unittest
- Automating testing using GitHub Actions

## 📂 Project Structure
LAB1/
│
├── data/
├── src/
│ └── calculator.py
├── test/
│ ├── test_pytest.py
│ └── test_unittest.py
├── .github/workflows/
│ ├── pytest_action.yml
│ └── unittest_action.yml
├── requirements.txt
└── README.md

## ⚙️ Step 1: Virtual Environment Setup

Create virtual environment:
 bash
python -m venv lab_01

Activate (Windows):

lab_01\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🧮 Step 2: Calculator Module (src/calculator.py)

The calculator module contains four functions:

1️ fun1(x, y)

Adds two numbers.
Raises ValueError if inputs are not numeric.

2️ fun2(x, y)

Subtracts y from x.
Raises ValueError if inputs are not numeric.

3️ fun3(x, y)

Multiplies two numbers.
Raises ValueError if inputs are not numeric.

4️ fun4(x, y, z)

Adds three numbers together.

🧪 Step 3: Testing
🔹 Pytest

Install pytest (if needed):

pip install pytest

Run tests:

pytest

Test cases included:

test_fun1

test_fun2

test_fun3

test_fun4

Each function is tested with multiple input scenarios including negative numbers and zero.

🔹 Unittest

Run unittest suite:

python -m unittest test.test_unittest

The TestCalculator class validates all four functions using assertEqual.

🚀 Step 4: GitHub Actions (CI Implementation)

Two workflows are configured:

✅ Pytest Workflow

Triggered on push to main

Sets up Python 3.8

Installs dependencies

Runs pytest

Generates XML test report

Uploads test artifact

✅ Unittest Workflow

Triggered on push to main

Installs dependencies

Runs unittest suite

Displays success/failure message

This ensures automated testing on every push to the repository.

✅ Results

All Pytest test cases passed successfully.

All Unittest test cases passed successfully.

GitHub Actions workflows executed successfully.

📌 Conclusion

This lab demonstrates:

Modular Python development

Input validation and error handling

Unit testing using Pytest and Unittest

Continuous Integration using GitHub Actions

The successful CI pipeline ensures code reliability and automated validation upon every commit.


