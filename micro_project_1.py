"""ANA500 Micro-Project 1: education and income, through Acquire and Prepare.

Author: Douglas Bobeck
Question: Is the share earning above $50,000 greater among adults with a
bachelor's degree or higher than among adults with less education?
Hypothesis: The bachelor's-or-higher group has the greater share.
This script prepares that comparison. It does not test the hypothesis.
Source: Becker & Kohavi (1996), Adult, https://doi.org/10.24432/C5XW20
"""

from pathlib import Path
import hashlib
import json
import platform

import numpy as np
import pandas as pd


PROJECT = Path(__file__).resolve().parent
INPUT = PROJECT / "data" / "adult_income.csv"
OUTPUT = PROJECT / "deliverables"
COLUMNS = (
    "age workclass fnlwgt education education-num marital-status occupation "
    "relationship race sex capital-gain capital-loss hours-per-week "
    "native-country income"
).split()
NUMERIC = ["age", "fnlwgt", "education-num", "capital-gain",
           "capital-loss", "hours-per-week"]
# education-num is an ordered education code, not literal years in school.
EDUCATION = dict(zip([
    "Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th",
    "12th", "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm",
    "Bachelors", "Masters", "Prof-school", "Doctorate",
], range(1, 17)))
DEGREES = ["Bachelors", "Masters", "Prof-school", "Doctorate"]


def prepare(raw):
    """Return a prepared copy and audit evidence; never modify the input."""
    # 1. ACQUIRE: require the documented schema before transforming values.
    # Importing as strings makes missing markers and conversion rules explicit.
    if list(raw.columns) != COLUMNS or raw.empty:
        raise ValueError("Expected a nonempty Adult CSV with the 15 columns.")
    data = raw.astype("string").copy()

    # 2. PREPARE: trim text and recognize both '?' and empty cells as missing.
    # Keep missing categories unknown rather than guessing a person's job.
    for column in COLUMNS:
        data[column] = data[column].str.strip().replace({"?": pd.NA, "": pd.NA})
    # The UCI test split may append a period to income labels. Normalize only
    # the two documented variants; unrelated or invalid labels must still fail.
    data["income"] = data["income"].replace({"<=50K.": "<=50K", ">50K.": ">50K"})
    missing = data.isna().sum()
    missing_rows = int(data.isna().any(axis=1).sum())

    # Validate the variables required for the planned education comparison.
    if data[["education", "income"]].isna().any().any():
        raise ValueError("Education and income must be present for every row.")
    if not data["income"].isin(["<=50K", ">50K"]).all():
        raise ValueError("Income contains an undocumented category.")
    if not data["education"].isin(EDUCATION).all():
        raise ValueError("Education contains an undocumented category.")

    # Convert six quantitative fields to integers. Reject missing, infinite,
    # fractional, and unparseable values instead of silently truncating them.
    for column in NUMERIC:
        values = pd.to_numeric(data[column], errors="raise")
        array = values.to_numpy(dtype=float, na_value=np.nan)
        if not np.isfinite(array).all() or not (array % 1 == 0).all():
            raise ValueError(f"{column} must contain finite, nonmissing integers.")
        data[column] = values.astype("int64")

    # NumPy arrays allow one elementwise check across all numerical records.
    # These broad plausibility bounds are validation rules, not outlier caps.
    # The observed 90-year ages and 99-hour workweeks are retained, not erased.
    numeric_array = data[NUMERIC].to_numpy(dtype=float)
    lower = np.array([17, 1, 1, 0, 0, 1])
    upper = np.array([120, np.inf, 16, np.inf, np.inf, 168])
    if not ((numeric_array >= lower) & (numeric_array <= upper)).all():
        raise ValueError("A numeric value falls outside the plausibility bounds.")
    if not data["education"].map(EDUCATION).eq(data["education-num"]).all():
        raise ValueError("Education labels disagree with their numeric codes.")

    # Identical attribute profiles are not proof of duplicated people: this
    # dataset contains no person identifier. Count repeats and retain all rows.
    duplicates = int(data.duplicated().sum())
    for column in set(COLUMNS) - set(NUMERIC):
        data[column] = data[column].astype("category")

    # Create explicit variables for a future comparison with np.where.
    # No comparison of group income rates or model fitting occurs in Project 1.
    data["education_group"] = pd.Categorical(np.where(
        data["education"].isin(DEGREES), "Bachelor's or higher", "Below bachelor's"
    ))
    data["income_gt_50k"] = np.where(data["income"].eq(">50K"), 1, 0)

    # Explore distributions with NumPy percentiles and Pandas frequency tables.
    # Zero capital gain/loss values are valid. Do not automatically cap them
    # using IQR: both quartiles can be zero for these sparse monetary fields.
    percentiles = pd.DataFrame(
        np.percentile(numeric_array, [0, 25, 50, 75, 100], axis=0).T,
        index=NUMERIC, columns=["minimum", "Q1", "median", "Q3", "maximum"]
    )
    audit = {
        "input_rows": len(raw), "input_columns": len(raw.columns),
        "output_rows": len(data), "output_columns": len(data.columns),
        "rows_removed": len(raw) - len(data),
        "missing_by_column": {k: int(v) for k, v in missing.items()},
        "rows_with_missing": missing_rows,
        "duplicate_profiles_beyond_first": duplicates,
        "income_counts": data["income"].value_counts().to_dict(),
        "education_group_counts": data["education_group"].value_counts().to_dict(),
        "numeric_percentiles": percentiles.to_dict(orient="index"),
        "prepared_dtypes": data.dtypes.astype(str).to_dict(),
        "hypothesis_tested": False,
    }
    return data, audit


def main():
    # File paths are based on this script's folder.
    # Read the source once and hash its bytes to identify the exact input file.
    source_hash = hashlib.sha256(INPUT.read_bytes()).hexdigest()
    raw = pd.read_csv(INPUT, dtype="string", keep_default_na=False)
    data, audit = prepare(raw)
    audit["input_sha256"] = source_hash
    audit["versions"] = {"Python": platform.python_version(),
                         "NumPy": np.__version__, "Pandas": pd.__version__}

    # Record reproducible evidence. The generated CSV represents missing values
    # as empty fields; Pandas read_csv recognizes them as missing on reload.
    OUTPUT.mkdir(exist_ok=True)
    data.to_csv(OUTPUT / "adult_income_prepared.csv", index=False, na_rep="")
    (OUTPUT / "preparation_audit.json").write_text(
        json.dumps(audit, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    report = "\n".join([
        "ANA500 MICRO-PROJECT 1 | Douglas Bobeck",
        "Scope: Acquire and Prepare. Hypothesis remains untested.",
        f"Input: {len(raw):,} records x {len(raw.columns)} columns",
        f"Prepared: {len(data):,} records x {len(data.columns)} columns",
        f"Rows removed: {audit['rows_removed']}",
        f"Source SHA-256: {source_hash}",
        f"Versions: {audit['versions']}",
        "\nMISSING VALUES (retained as unknown)",
        pd.Series(audit["missing_by_column"]).to_string(),
        f"Rows with at least one missing value: {audit['rows_with_missing']:,}",
        f"Repeated profiles beyond first occurrence: {audit['duplicate_profiles_beyond_first']}",
        "Repeated profiles retained because no person identifier is available.",
        "\nNUMPY NUMERIC DISTRIBUTION SUMMARY (unweighted sample)",
        pd.DataFrame(audit["numeric_percentiles"]).T.to_string(),
        "\nINCOME CATEGORY COUNTS (unweighted sample)",
        data["income"].value_counts().to_string(),
        "\nEDUCATION GROUP COUNTS (no income comparison)",
        data["education_group"].value_counts().to_string(),
        "\nPREPARED DATA TYPES", data.dtypes.to_string(),
        "\nVALIDATION: schema, required values, integer fields, ranges,",
        "income labels, and education-code agreement all passed.",
        "Historical 1994 sample. fnlwgt retained as a survey weight.",
        "These summaries are not weighted population estimates.",
        "No hypothesis test, causal conclusion, model, or recommendation.",
    ]) + "\n"
    (OUTPUT / "preparation_output.txt").write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    main()
