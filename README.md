# ANA500 Python for Data Science

Douglas Bobeck

This repository contains the completed work for Weeks 1 through 4. Each project
includes its analysis, presentation, and Python code and output PDF.

| Week | Analysis | Submission files |
|---|---|---|
| 1: Data preparation | [Python script](micro_project_1.py) | [PowerPoint](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pptx), [slides PDF](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pdf), [code PDF](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1_Code.pdf) |
| 2: Income visualizations | [Jupyter notebook](week2/Micro_Project_2.ipynb) | [PowerPoint](week2/Douglas_Bobeck_ANA500_Micro_Project_2.pptx), [slides PDF](week2/Douglas_Bobeck_ANA500_Micro_Project_2.pdf), [code PDF](week2/Douglas_Bobeck_ANA500_Micro_Project_2_Code.pdf) |
| 3: Weekly work hours regression | [Jupyter notebook](week3/Micro_Project_3.ipynb) | [PowerPoint](week3/Douglas_Bobeck_ANA500_Micro_Project_3.pptx), [slides PDF](week3/Douglas_Bobeck_ANA500_Micro_Project_3.pdf), [code PDF](week3/Douglas_Bobeck_ANA500_Micro_Project_3_Code.pdf) |
| 4: Deep learning forecasts | [Jupyter notebook](week4/Micro_Project_4.ipynb) | [PowerPoint](week4/Douglas_Bobeck_ANA500_Micro_Project_4.pptx), [slides PDF](week4/Douglas_Bobeck_ANA500_Micro_Project_4.pdf), [code PDF](week4/Douglas_Bobeck_ANA500_Micro_Project_4_Code.pdf) |

See the [Week 2 guide](week2/README.md), [Week 3 guide](week3/README.md), and [Week 4 guide](week4/README.md) for
their methods, results, and instructions for running the notebooks. Each week
has its own requirements file. The remaining sections describe Week 1.

## Micro-Project 1: Education and Income

**Douglas Bobeck | September 20, 2026**

This project uses NumPy and Pandas to acquire, explore, and prepare Adult income
data. It ends at **Step 2: Prepare** of the data science process.

## Problem and hypothesis

This project looks at the relationship between education and income.
The question is whether the share earning above $50,000 is greater among adults
with a bachelor's degree or higher than among adults with less education.
The hypothesis is that adults with at least a bachelor's degree are more likely
to earn above $50,000. More education may help people qualify for jobs with
higher pay. That explanation would need to be tested.

**The hypothesis is not tested here.** This project contains no model, causal
claim, significance test, or comparison of income rates by education group.

## Tools used

Python 3.13.3, Pandas 3.0.6, and NumPy 2.5.3 were used to prepare the data.
The script was run in PyCharm.

## Reproduce results

From a terminal in the project directory:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python micro_project_1.py
.venv/bin/python check_micro_project_1.py
```

After installing the dependencies, the project runs locally. Running the script
saves the prepared CSV, JSON audit, and text output in `deliverables`.
The presentation and code PDF contain the results from that run and are updated
separately when the project changes.

## Deliverables

- [Completed PowerPoint](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pptx)
- [Presentation PDF](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1.pdf)
- [Python code and output (PDF)](deliverables/Douglas_Bobeck_ANA500_Micro_Project_1_Code.pdf)
- [Python code](micro_project_1.py)
- [Prepared CSV](deliverables/adult_income_prepared.csv)
- [Preparation audit](deliverables/preparation_audit.json)
- [Output](deliverables/preparation_output.txt)

The slides follow the course template and cover the problem statement,
hypothesis, Acquire, and Prepare.

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
  Education and income are complete, so these missing values do not require
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

These summaries count each row equally. Using survey weights to estimate the
larger population would need a separate analysis. The data do not show that
education causes higher income or describe today's income distribution.

## Verification

`check_micro_project_1.py` verifies the known file counts, independent example
transformations, missing-value handling, invalid-input rejection, and preservation
of the raw input. Run it with the same interpreter as the main script.
