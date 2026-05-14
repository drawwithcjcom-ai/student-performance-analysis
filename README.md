# 📘 Student Performance Analyzer

## Overview
This Python program analyzes student marks across subjects, organizes them into a structured dictionary, and generates a detailed performance report. It highlights individual scores, identifies students above or below thresholds, finds subject toppers, calculates totals and averages, and determines the overall class topper.

## Features
- Organizes raw student data into a dictionary for easy lookup.  
- Displays subject‑wise marks for each student.  
- Identifies students scoring **above 80** and **below 40**.  
- Finds the highest scorer in **Math, Science, and English**.  
- Calculates each student’s **total marks** and **average percentage**.  
- Determines the **overall topper** based on average scores.

## Example Output
```
Student's Name : Alice
Marks Scored in Math is : 85
Marks Scored in Science is : 90
Marks Scored in English is : 88

Above 80 Students..
Alice
Charlie
Ethan

No students have scored below 40..

Math highest mark : Charlie , got 92
Science highest mark : Charlie , got 95
English highest mark : Ethan , got 91

Alice has scored a total of 263 and average is 88 %
Bob has scored a total of 240 and average is 80 %
Charlie has scored a total of 276 and average is 92 %
Diana has scored a total of 217 and average is 73 %
Ethan has scored a total of 263 and average is 88 %

Charlie is the topper with 92 %
```

## Tech Stack
- **Language:** Python 3  
- **Library:** `math` (for ceiling function in average calculation)

## How to Run
1. Save the script as `student_performance.py`.  
2. Run in terminal:  
   ```
   python student_performance.py
   ```
3. View the full performance report in the console.

---
