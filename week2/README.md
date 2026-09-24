# ANA500 Micro-Project 2

Douglas Bobeck

This project examines which demographic, educational, and employment characteristics are associated with earning above $50,000 in the Adult dataset. It covers Acquire, Prepare, Analyze, and Report. The analysis uses Jupyter Notebook, Pandas, NumPy, Matplotlib, and Seaborn.

## Submission files

- `Douglas_Bobeck_ANA500_Micro_Project_2.pptx`: presentation using the course template.
- `Douglas_Bobeck_ANA500_Micro_Project_2.pdf`: the same slides as a PDF.
- `Douglas_Bobeck_ANA500_Micro_Project_2_Code.pdf`: Python code and output, including comments, figures, and conclusions from the executed notebook.
- `Micro_Project_2.ipynb`: editable Jupyter notebook with saved outputs.

The `outputs` folder contains six chart images and the numbers used in the slides. Week 1 remains unchanged.

## Open the notebook

Open `Micro_Project_2.ipynb` in JupyterLab, select the Python 3 kernel, and choose **Kernel > Restart Kernel and Run All Cells**. The notebook is self-contained and does not import the Week 1 script. Its verification cell checks group counts, percentage denominators, combined groups, and the unchanged input file.

On the computer used for this project, Anaconda already provides the required packages. From Terminal:

```bash
cd /Users/budrowkiwi/PycharmProjects/ANA500
/Users/budrowkiwi/anaconda3/bin/jupyter lab week2/Micro_Project_2.ipynb
```

JupyterLab opens and edits Jupyter notebooks. This launch command was checked with the existing Anaconda installation. The older `jupyter notebook` launcher in that installation has a dependency conflict, so use JupyterLab.

For another computer, use Python 3.11, install the packages in `requirements.txt` in an environment, and run `jupyter lab`. The tested analysis versions are Python 3.11.5, NumPy 1.26.4, Pandas 2.2.2, Matplotlib 3.8.4, and Seaborn 0.12.2.

The input is `../data/adult_income.csv` when opened from this repository's `week2` folder. A course-folder copy can use `../adult income.csv`. Keep the notebook beside one of those input locations. Running all cells refreshes only the Week 2 outputs.

## Findings and limits

The overall share earning above $50,000 is 24.1%. The rate differs across age, education, occupation, and weekly work hours. Among adults ages 45-59 with a bachelor's degree or higher who work over 40 hours, it is 72.7% (n=1,089).

The charts compare unweighted percentages in a historical sample. They do not estimate independent effects, establish causation, or measure predictive accuracy. Missing occupations remain visible as Unknown, and the combined chart does not display percentages for groups with fewer than 100 records. Classification is left for later coursework.

## Data source

Becker, B., & Kohavi, R. (1996). *Adult* [Dataset]. [UCI Machine Learning Repository](https://doi.org/10.24432/C5XW20). License: CC BY 4.0.

The supplied CSV contains the 32,561-record training sample drawn from the 1994 Census database. The separate test split is not used. [Attribute definitions and survey weight documentation](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names).
