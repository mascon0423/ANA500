# ANA500 Micro-Project 1: Education and Income

**Douglas Bobeck | September 20, 2026**

This project uses NumPy and Pandas to acquire, explore, and prepare Adult income
data. It ends at **Step 2: Prepare** of the data science process.

## Problem and hypothesis

The project investigates how income category varies with educational attainment.
The question is whether the share earning above $50,000 is greater among adults
with a bachelor's degree or higher than among adults with less education.
The hypothesis is that the bachelor's-or-higher group has the greater share.
Higher education may provide access to occupations with higher earnings, but
that is a proposed explanation, not a demonstrated result.

**The hypothesis is not tested here.** This project contains no model, causal
claim, significance test, or comparison of income rates by education group.

## Run in PyCharm

Open this folder as the PyCharm project. Select its `.venv` Python interpreter,
open `micro_project_1.py`, and choose **Run 'micro_project_1'**. Input/output paths
are anchored to the script, so the working-directory setting does not matter.
The script includes section comments explaining the methods and decisions.

From a terminal in the project directory:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python micro_project_1.py
.venv/bin/python check_micro_project_1.py
```

The existing environment uses Python 3.13.3, NumPy 2.5.3, and Pandas 3.0.6.
No API keys, environment variables, network connection, or extra runtime
dependencies are required after installation. Running the script regenerates
the prepared CSV, JSON audit, and text output. The submitted presentation and
code PDF are snapshots of the verified run, not automatically regenerated.

## Deliverables

- [Completed PowerPoint](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pptx)
- [Presentation PDF](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pdf)
- [Commented code and executed output PDF](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1_Code.pdf)
- [Runnable Python source](micro_project_1.py)
- [Prepared CSV](deliverables/adult_income_prepared.csv)
- [Preparation audit](deliverables/preparation_audit.json)
- [Execution output](deliverables/preparation_output.txt)

The deck uses the course template's title, Problem Statement, Hypothesis,
Acquire, and Prepare slides. Prepare is expanded to three slides for readability.
The later Analyze, Report, and Act slides are omitted for this assignment.

## Dataset and attribution

Becker, B., & Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning
Repository. https://doi.org/10.24432/C5XW20

- [UCI dataset and license](https://archive.ics.uci.edu/dataset/2/adult)
- [Original attribute and split documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names)
- [Original training data](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data)
- UCI lists the dataset under **CC BY 4.0**. Attribution applies to the raw data
  and the derived prepared CSV. This statement does not license the course template.

The supplied `adult income.csv` was copied unchanged to `data/adult_income.csv`.
On September 20, 2026, all values and their row order were verified against UCI's
`adult.data`, after accounting for its missing header and delimiter whitespace.
The source is the **1994 Census database**, not a current income survey.

The local file has **32,561 records and 15 columns**, matching the training split.
The full UCI dataset has 48,842 records; the separate test split is not used.
The exact input SHA-256 is recorded in `preparation_audit.json`.

### Field guide

| Field | Meaning or role |
|---|---|
| age | Adult's age |
| workclass | Employment class |
| fnlwgt | Final survey weight, not a person identifier |
| education | Educational attainment category |
| education-num | Ordered education code from 1 to 16, not literal school years |
| marital-status | Marital status category |
| occupation | Occupation category |
| relationship | Household relationship category |
| race | Race category recorded in the source |
| sex | Sex category recorded in the source |
| capital-gain | Capital gains |
| capital-loss | Capital losses |
| hours-per-week | Work hours per week |
| native-country | Native-country category |
| income | Annual income at/below $50,000 or above $50,000 |

## Preparation decisions and results

- Trim whitespace and convert `?` and empty cells to recognized missing values.
- Retain unknown workclass (1,836), occupation (1,843), and native-country (583)
  values. These affect **2,399 records** in total because the counts overlap.
  Education and income are complete, so ancillary missingness does not require
  dropping rows for this question. Missing values export as empty CSV fields.
- Validate the schema, numeric parsing, income categories, and the mapping
  between education and education-num. Convert numeric fields to integers and
  textual fields to Pandas categorical objects.
- Retain **24 repeated profiles beyond the first occurrence**. No person ID
  exists to establish that these are erroneously duplicated people. A later
  sensitivity analysis could compare results with and without repeated profiles.
- Keep valid zero gains/losses and plausible extreme values. The broad bounds
  used for validation are not automatic clipping thresholds.
- Use NumPy arrays for range checks and percentiles. Sample medians are age 37
  and work hours 40 per week. These summaries do not test the hypothesis.
- Add education_group and income_gt_50k with NumPy. Bachelor's or higher includes
  Bachelors, Masters, Prof-school, and Doctorate. The two groups contain 8,067
  and 24,494 records, respectively.
- Preserve all **32,561 records**. The prepared dataset has **17 columns**.

These are unweighted sample summaries. Survey-weighted population inference
would require a separate analytical design. The data cannot establish that
education causes income differences or describe today's income distribution.

## Verification

`check_micro_project_1.py` verifies the known file counts, independent example
transformations, missing-value handling, invalid-input rejection, and preservation
of the raw input. Run it with the same interpreter as the main script.

No formatter, linter, or CI configuration existed in the new project. One useful
future gate is to run this existing check on each GitHub push.
