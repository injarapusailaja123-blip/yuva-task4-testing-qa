# Expense Tracker System - Testing and QA | Task 4

**Author:** Sailaja Injarapu  
**Internship:** Yuva Internship - Python Development  
**Task:** Task 4 - Testing and Quality Assurance

## About Project
Expense Tracker helps users to add, view, delete expenses and calculate total. Data saved permanently in expenses.txt.

In Task 4, I tested this project deeply with Unit, Integration, System, UAT testing to make it reliable and production-ready.

## Technologies
- Python 3.10.11
- unittest (Built-in)
- VS Code Debugger
- Git, GitHub

## File Structure
yuva-task4-testing-qa/
- src/main.py - Main application
- test_main.py - 12 Unit Tests
- TESTING.md - All test cases documentation
- README.md
- requirements.txt
- .gitignore

## How to Run App
python src/main.py

Menu:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Calculate Total
5. Exit

## How to Run Tests
python -m unittest test_main.py -v

Expected: 12 tests, All PASS

## Test Summary
- Unit Tests: 12 - All PASS
- Integration Tests: 3 - All PASS
- System Tests: 1 - PASS
- UAT: 3 Scenarios - PASS
- Edge Cases: 6 - PASS
- Total: 20 Test Cases - All PASS

## Bugs Fixed
1. File not found on first run - Fixed with os.path.exists() + try-except FileNotFoundError
2. Crash on text input for amount - Fixed with try-except ValueError

## Performance
1000 expenses -> calculate_total() in 0.02 seconds - Fast and efficient

## GitHub
https://github.com/injarapusailaja123-blip/yuva-task4-testing-qa
