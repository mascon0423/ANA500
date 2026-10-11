# ANA500 Micro-Project 4: Forecasting Hourly Bike Rentals

Douglas Bobeck | October 11, 2026

This project uses deep learning regression to predict next-hour recorded bike rentals.
It compares a dense neural network, a basic RNN, and an LSTM against two simple baselines.
The analysis uses Jupyter Notebook and completes Acquire, Prepare, Analyze, Report, and Act.

## Submission files

- [PowerPoint](Douglas_Bobeck_ANA500_Micro_Project_4.pptx)
- [Presentation PDF](Douglas_Bobeck_ANA500_Micro_Project_4.pdf)
- [Python code and output PDF](Douglas_Bobeck_ANA500_Micro_Project_4_Code.pdf)
- [Executed Jupyter notebook](Micro_Project_4.ipynb)

Submit the presentation in an accepted format and the code PDF. Include the
[repository link](https://github.com/mascon0423/ANA500/tree/main/week4), which contains
[the notebook](https://github.com/mascon0423/ANA500/blob/main/week4/Micro_Project_4.ipynb).
Both links also appear in the submission materials.

## Question and hypothesis

How accurately can the preceding 24 hours of recorded rentals and known calendar
information forecast the next hour's rentals? The hypothesis is that a deep neural
network using recent activity and calendar patterns will outperform repeating the
previous hour or the same hour yesterday.

Week 4 changes from Adult records to a genuine hourly series so the RNN has a
meaningful sequence. Weeks 1-3 remain separate.

## Data and evaluation

The included `hour.csv` contains 17,379 hourly records from Capital Bikeshare in
Washington, D.C., in 2011-2012. Its checksum is verified in the notebook. The source
README also reports 17,379 records; the UCI landing page's 17,389 figure differs.

The full hourly calendar has 165 missing hours. Missing hours remain unknown,
not zero. Requiring a complete 24-hour history leaves 15,657 eligible target hours
and excludes 1,722 recorded target hours. Results apply to eligible windows.

Training uses 2011. Validation uses January-June 2012 and chooses the checkpoint
and preferred model. Testing uses July-December 2012. Counts are scaled using 2011
only. All neural models use 24 past counts plus seven known calendar features.
No target-hour weather, casual-user counts, or registered-user counts enter the models.

These are rolling one-hour forecasts. At each test hour, prior actual counts are
available as inputs; future counts are not. Model weights remain fixed. This is
not a forecast of six months made at once. The source has local clock labels but
no timezone offsets, so daylight-saving transitions are not separately resolved.

## Results and decision

The dense network was selected on validation RMSE and also performed best on the
test period: MAE 35.61 rentals, RMSE 55.18, and R-squared 0.937. Its RMSE is 57.8%
below the validation-selected previous-hour baseline. Basic RNN test RMSE is 79.65,
and LSTM test RMSE is 85.70. All three neural models outperform both baselines.

Keep the dense network as a candidate for a monitored trial on current data.
Compare weekly errors with baselines and agree on acceptable error before using
forecasts for operations. One historical split, one seed, omitted weather, and
gap exclusions limit general conclusions. The forecasts have no calibrated
prediction intervals. System-wide recorded rentals do not determine unmet demand
or station inventory needs.

## Open and reproduce

Keep `hour.csv` next to `Micro_Project_4.ipynb`. Open the notebook in JupyterLab,
choose the Python 3 kernel, and select **Kernel > Restart Kernel and Run All Cells**.
The analysis runs on the CPU and can take several minutes. No API key is required.

On the computer used for this project:

```bash
cd '/Users/budrowkiwi/Desktop/National University/ANA500/Week 4'
/Users/budrowkiwi/anaconda3/bin/jupyter lab Micro_Project_4.ipynb
```

On another computer, use Python 3.11 and install the listed dependencies in an
isolated environment, then run JupyterLab from this folder:

```bash
python -m pip install -r requirements.txt
jupyter lab Micro_Project_4.ipynb
```

The notebook contains runnable checks of window alignment, chronological splits,
source integrity, baseline formulas, group totals, and model metrics. Fixed seed 42,
CPU execution, and deterministic operations support repeatability in the recorded
environment; different hardware or library versions can still change results.
Running all cells refreshes this folder's analytical outputs. The presentation
and PDFs capture the saved run and are exported separately.

## Supporting files

`outputs/` includes five figures, model comparisons, training curves, every test
forecast, error by clock hour, and an analysis summary. `SOURCE_README.txt` is the
unchanged source documentation. No trained model file is required because the
notebook fits the models and reproduces the analysis.

## Sources and license

Fanaee-T, H. (2013). [Bike Sharing](https://doi.org/10.24432/C5W894). UCI Machine
Learning Repository. CC BY 4.0. Downloaded October 11, 2026.

Fanaee-T, H., & Gama, J. (2013). [Event labeling combining ensemble detectors and
background knowledge](https://doi.org/10.1007/s13748-013-0040-3). Progress in Artificial
Intelligence. This publication is specified in the dataset's README.

[PyTorch RNN documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.RNN.html),
[LSTM documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.LSTM.html),
and [reproducibility guidance](https://docs.pytorch.org/docs/stable/notes/randomness.html).
Dataset attribution does not license the course presentation template.
