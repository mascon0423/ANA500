# ANA500 Micro-Project 3: Predicting Weekly Work Hours

Douglas Bobeck | October 4, 2026

This project compares linear regression, support vector regression (SVR), and
decision tree regression. It covers Acquire, Prepare, Analyze, Report, and Act.
The work uses Jupyter Notebook, Python, Pandas, NumPy, Matplotlib, and scikit-learn.
Weeks 1 and 2 remain separate and unchanged.

## Question and hypothesis

How accurately can age, education, occupation, and workclass predict weekly work
hours in the Adult dataset? The hypothesis is that these characteristics jointly
predict hours better than always using the training sample's average. Different
job roles and employment arrangements may help explain variation in hours.

Module 2 studied income categories. This module uses hours because it requires
regression and Adult does not provide actual salary amounts. Income classification
remains a separate question for later coursework.

## Submission files

- `Douglas_Bobeck_ANA500_Micro_Project_3.pptx`: editable presentation using the course template.
- `Douglas_Bobeck_ANA500_Micro_Project_3.pdf`: the same presentation as a PDF.
- `Douglas_Bobeck_ANA500_Micro_Project_3_Code.pdf`: Python code and output, including section comments, tables, charts, and conclusions.

Submit the presentation in one allowed format and the code PDF. Include the
[repository link](https://github.com/mascon0423/ANA500) for the Jupyter notebook.
The [Week 3 notebook](https://github.com/mascon0423/ANA500/blob/main/week3/Micro_Project_3.ipynb)
contains the analysis and saved outputs.

## Supporting files

- `Micro_Project_3.ipynb`: Jupyter notebook with executed cells and saved outputs.
- `adult_income.csv`: unchanged source input, copied into this folder for portability.
- `outputs/`: four figures, the model comparison, test predictions for the selected model, and the numbers used in the slides.
- `requirements.txt`: analysis packages and Jupyter requirements.

## Open and reproduce

Open `Micro_Project_3.ipynb` in JupyterLab, select the Python 3 kernel, and choose
**Kernel > Restart Kernel and Run All Cells**. Keep `adult_income.csv` beside the
notebook. The SVR search can take several minutes; it runs sequentially to avoid
background-worker restarts. No API key or online service is required.

The existing Anaconda installation on this computer provides the analysis packages:

```bash
cd '/Users/budrowkiwi/Desktop/National University/ANA500/Week 3'
/Users/budrowkiwi/anaconda3/bin/jupyter lab Micro_Project_3.ipynb
```

For another computer, use Python 3.11 and install `requirements.txt` in an environment.
Running the notebook refreshes only this folder's analytical outputs. The submitted
presentation and PDFs capture the saved run and are exported separately.

## Model comparison

The supplied file contains 32,561 records. The project uses 26,048 training records
and 6,513 test records. Exact repeated full profiles remain in the same partition.
The same three grouped cross-validation folds select settings and the preferred
model on the training set. Scaling and category encoding are fitted inside each fold.
No test scores are used to choose settings or switch the selected model.

The four predictors are original age, education category, occupation, and workclass.
Original numerical hours are the outcome. Hour groups are used only for diagnostic
summaries. Missing workclass and occupation become Unknown. Income and survey
weight are excluded from the predictors. Records are unweighted.

SVR (RBF kernel, C=10, epsilon=2) had the lowest cross-validation RMSE. On the test
set, its MAE was 7.16 hours, RMSE was 10.89 hours, and R-squared was 0.225. Its RMSE
was 12.0% below the training-mean baseline. The decision tree was close at 10.96
hours RMSE; the limited search and single split do not prove a dependable advantage.

## Decision and limitations

Retain SVR as the preferred model in this comparison. Errors are much larger for
short and long workweeks. The model can guide further study, but it is not a
reliable basis for individual scheduling or employment decisions. Define an
acceptable error and obtain current independent data before considering practical use.
Survey weights would need separate investigation for population-level claims.

This is internal evaluation of historical data explored in earlier modules, not
external validation. Results do not establish causes or describe today's workers.
The notebook contains runnable checks of split separation, calculated metrics,
baseline predictions, diagnostic totals, original numerical values, and input integrity.

## Source

Becker, B., & Kohavi, R. (1996). *Adult* [Dataset].
[UCI Machine Learning Repository](https://doi.org/10.24432/C5XW20), CC BY 4.0.
The supplied 32,561-row file matches UCI's training sample from the 1994 Census
database. The separate UCI test file is not used. The source file's SHA-256 is
checked in the notebook. Dataset attribution does not license the course template.
