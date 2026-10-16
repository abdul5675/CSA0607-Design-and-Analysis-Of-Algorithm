# CO1 Assignment — ShopSphere Scalability Audit

This project analyses the algorithms specified in the ShopSphere assessment.

## Contents
- 12 task folders containing detailed answers.
- Python operation-count model in `Task_8_Implementation_Testing/Source_Code/`.
- Combined report in `Report/Documentation/CO1_Assignment_Report.md`.
- CSV operation estimates in `Task_9_Experimental_Performance/`.
- Optional graph in `Report/Tables_and_Graphs/`.

## Run the program
From the repository root, run:

```powershell
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

If running from inside `CO1_Assignment`, run:

```powershell
python Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

Optional graphs require Matplotlib:

```powershell
python -m pip install matplotlib
```

## Important interpretation
Times in the CSV are operation-count estimates using the assessment's assumption of 10^8 basic operations per second. They are not measured production timings. The model documents assumptions, especially for non-power-of-two recurrence estimates.

## Screenshots
Run the program and capture genuine screenshots of the source code and terminal output. Save them in `Report/Source_Code_Screenshots/` and `Report/Output_Screenshots/`. Do not submit fabricated screenshots.

## GitHub
Review the generated files, then use VS Code Source Control to stage, commit, and push them to the existing repository.
