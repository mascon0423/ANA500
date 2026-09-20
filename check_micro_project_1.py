"""Run with: python check_micro_project_1.py. No test framework required."""
import pandas as pd
from micro_project_1 import INPUT, prepare

raw = pd.read_csv(INPUT, dtype="string", keep_default_na=False)
original = raw.copy(deep=True)
prepared, audit = prepare(raw)
pd.testing.assert_frame_equal(raw, original)
assert prepared.shape == (32561, 17)
assert audit["rows_with_missing"] == 2399
assert audit["missing_by_column"]["workclass"] == 1836
assert audit["missing_by_column"]["occupation"] == 1843
assert audit["missing_by_column"]["native-country"] == 583
assert audit["duplicate_profiles_beyond_first"] == 24
assert audit["income_counts"] == {"<=50K": 24720, ">50K": 7841}
assert prepared["income_gt_50k"].sum() == 7841
assert prepared["capital-gain"].eq(0).sum() == raw["capital-gain"].eq("0").sum()
assert not audit["hypothesis_tested"]

# Check an independent two-record example, including whitespace, unknowns,
# a legitimate zero, period-suffixed income, and education-code agreement.
sample = raw.iloc[[0, 2]].copy()
sample.loc[sample.index[0], "education"] = " Bachelors "
sample.loc[sample.index[0], "income"] = " >50K. "
sample.loc[sample.index[1], "occupation"] = " ? "
sample.loc[sample.index[1], "native-country"] = ""
clean, _ = prepare(sample)
assert clean["education_group"].tolist() == ["Bachelor's or higher", "Below bachelor's"]
assert clean["income_gt_50k"].tolist() == [1, 0]
assert pd.isna(clean.iloc[1]["occupation"])
assert pd.isna(clean.iloc[1]["native-country"])

# Invalid boundary inputs must raise before any generated output is written.
for column, value in [("age", "bad"), ("age", "17.5"), ("age", "inf"),
                      ("age", "?"), ("hours-per-week", "169"),
                      ("education-num", "9"), ("income", "unknown"),
                      ("education", "?"), ("education", "Unknown degree")]:
    invalid = sample.copy()
    invalid.loc[invalid.index[0], column] = value
    try:
        prepare(invalid)
    except (ValueError, TypeError):
        pass
    else:
        raise AssertionError(f"Accepted invalid {column}")
try:
    prepare(raw.drop(columns="age"))
except ValueError:
    pass
else:
    raise AssertionError("Accepted an incomplete schema")
print("PASS: dataset counts, transformations, source preservation, and invalid inputs.")
