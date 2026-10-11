# ANA500 Micro-Project 4: Predicting Weekly Work Hours with Neural Networks

Douglas Bobeck | October 11, 2026

This project continues Week 3's Adult dataset analysis. It compares MLP and RNN
regression with the earlier traditional models, tests additional predictors, and
investigates errors for short and long workweeks. It completes Acquire, Prepare,
Analyze, Report, and Act using Jupyter Notebook.

## Submission files

- [PowerPoint](Douglas_Bobeck_ANA500_Micro_Project_4.pptx)
- [Presentation PDF](Douglas_Bobeck_ANA500_Micro_Project_4.pdf)
- [Python code and output PDF](Douglas_Bobeck_ANA500_Micro_Project_4_Code.pdf)
- [Executed Jupyter notebook](Micro_Project_4.ipynb)

Submit the presentation in an accepted format and the code PDF. Both include the
[repository link](https://github.com/mascon0423/ANA500/tree/main/week4), which contains
[the notebook](https://github.com/mascon0423/ANA500/blob/main/week4/Micro_Project_4.ipynb).

## Question and hypothesis

Can neural networks and additional demographic information improve weekly work-hour
predictions, including the overprediction of short workweeks and underprediction
of long workweeks found in Week 3? The hypothesis requires improvement in overall
RMSE and in MAE for both the under-35 and over-40 hour groups relative to Week 3 SVR.

## Results

Cross-validation selected MLP - expanded. On the same 6,513 test records as Week 3, its RMSE was 10.65 hours, MAE was 7.25 hours, and R-squared was 0.259. The preferred neural model was MLP - expanded, with test RMSE 10.65 hours, 2.2% lower than Week 3's SVR. The CV-selected method also had the lowest test RMSE. Performance at short and long workweeks still needs attention; average error alone is insufficient for individual decisions.

I included an RNN to address the assignment instruction. With seven predictors, the MLP's test RMSE was 10.65 hours, lower than the RNN's 10.78 hours. The expanded SVR had RMSE 10.71 hours. The original four-feature SVR had RMSE 10.89 hours. Comparing both feature sets helps separate gains from additional information from gains associated with a different model.

For under 35 hours, MAE changed from 13.81 with Week 3 SVR to 12.62 with MLP - expanded (n=1,124). Mean bias changed from +13.25 to +12.08 hours. For over 40 hours, MAE changed from 11.02 with Week 3 SVR to 10.29 with MLP - expanded (n=1,971). Mean bias changed from -10.73 to -9.83 hours. The three stated criteria support the hypothesis on this test sample.

The MLP did not lead on every measure. Expanded RNN had lower MAE for short workweeks (11.64 versus 12.62 hours). Expanded SVR had lower overall MAE (7.07 versus 7.25 hours). RMSE was the selection criterion established before test scoring, so these tradeoffs inform the interpretation rather than change the selected model.

For RNN - expanded, the three tested field orders produced CV RMSE values from 10.647 to 10.673 hours. The reversed order's CV RMSE was slightly lower than the MLP's 10.667; this diagnostic was not used to choose another model or tested on the test set. The original-order MLP and RNN CV scores were also very close, so the results do not establish a decisive architecture advantage. The RNN processes an imposed field order rather than an observed time sequence. An MLP is a more direct representation of these tabular records, but representation alone does not establish which model will have the smallest error. The tested sizes, stopping choices, order, and initialization all affect the comparison.

This project illustrates why the data structure, the quantity being predicted, and validation results should guide model choice. Including a model because it is part of an assignment does not mean it must be the preferred method. I would retain the CV-selected method for further analysis and investigate missing information about short and long workweeks before expanding model complexity.

## Data and evaluation

The unchanged `adult_income.csv` has 32,561 records. Work hours remain a continuous
outcome. Age stays numerical. Missing workclass and occupation become Unknown;
valid extreme hours and repeated full profiles are retained. All records are
unweighted; `fnlwgt` is a survey weight, not a person identifier or predictor.

The original inputs are age, education, occupation, and workclass. Expanded inputs
add marital status, relationship, and sex. Income, hour groups, and the duplicate
education code are excluded. Source demographic labels and historical associations
are limitations; the analysis does not justify individual employment decisions.

The same 26,048 training records, 6,513 test records, and three grouped CV folds
are reconstructed using Week 3's source, cleaning, grouping, and seed. Repeated
full profiles stay in the same partition. The four traditional core models reproduce
Week 3's scores. Expanded SVR tests the same C/epsilon grid used there.

Neural sizes are chosen by mean outer-fold RMSE. A separate grouped stopping split
inside each outer training portion determines epochs. Preprocessing and target
scaling are fitted only on the appropriate training data. A fresh network refits
the complete outer training portion for that duration before scoring the outer
validation fold. Final fitting uses the median selected epoch across folds.

The RNN uses a sequence of encoded fields within each person, with field identity
included and hidden state reset for every record. It never links different people.
Field order is artificial. Reverse and shuffled orders are retrained for a CV-only
sensitivity check and do not change model selection.

The prior test results motivated this follow-up, so these are internal comparisons,
not independent external validation. One seed, a limited search, and historical
data restrict generalization. Current independent data, further seeds and splits,
fairness checks, and acceptable-error criteria are needed before operational use.

## Open and reproduce

Keep the notebook, `adult_income.csv`, and `week3_reference.json` together. Open
the notebook in JupyterLab and choose **Kernel > Restart Kernel and Run All Cells**.
Use the Python 3 kernel. Computation runs on the CPU and may take several minutes.
No API key is required.

On this computer:

```bash
cd '/Users/budrowkiwi/Desktop/National University/ANA500/Week 4'
/Users/budrowkiwi/anaconda3/bin/jupyter lab Micro_Project_4.ipynb
```

On another computer, use Python 3.11 and the versions in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
jupyter lab Micro_Project_4.ipynb
```

The notebook checks source integrity, partition separation, Week 3 score agreement,
RNN field identity and record independence, diagnostic totals, and independently
calculated errors. Fixed seed 42 and deterministic CPU operations support repeatability
in the recorded environment; other library versions or hardware can change results.
Running all cells refreshes analysis outputs. The slides and PDFs are exported separately.

## Supporting files

`outputs/` contains five figures, model comparisons, all test predictions, errors
by workweek group, neural candidates and fold scores, inner learning curves,
RNN order sensitivity, and a summary. `split_membership.csv` records zero-based
source row numbers; validation fold 0 identifies test rows. `week3_reference.json`
copies the relevant published Week 3 results for reproducibility checks.

The earlier bike-rental version is preserved separately as an archived example.
The files in this folder are the current Week 4 submission.

## Sources and license

Becker, B., & Kohavi, R. (1996). [Adult](https://doi.org/10.24432/C5XW20).
UCI Machine Learning Repository. CC BY 4.0. Source: 1994 Census database.
[Original field documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names).
The supplied CSV matches the 32,561-row UCI training sample used in earlier weeks;
the separate UCI test file is not used.

[Week 3 reference](https://github.com/mascon0423/ANA500/tree/main/week3),
[MLP regression](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression),
[GroupKFold](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.GroupKFold.html),
[PyTorch RNN](https://docs.pytorch.org/docs/stable/generated/torch.nn.RNN.html),
and [reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html).
Dataset attribution does not license the course presentation template.
