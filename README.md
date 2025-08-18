# Diabetes Prediction — Leakage-Safe ML Pipeline

Predict the likelihood of diabetes from clinical measurements (e.g., Glucose, BMI) using a clean, leakage-safe workflow:  
EDA → split → pipeline (false zeros → NaNs, impute, scale) → model comparison → RF hyperparameter tuning → diagnostics.

## Results (test set)

**Best AUC option — Random Forest (baseline)**  
- ROC AUC: **0.818**  
- Accuracy: **0.773**  
- Precision: **0.702**  
- Recall: **0.611**  
- F1: **0.653**

**Higher-recall option — Random Forest (tuned)**  
- ROC AUC: **0.817**  
- Accuracy: **0.740**  
- Precision: **0.606**  
- Recall: **0.741**  
- F1: **0.667**

**Validation:** 5-fold CV AUC on train = **0.841**; test AUC ≈ **0.817–0.818** → small gap -> **limited overfitting**.

> **Which to choose?**  
> - For overall discrimination (ranking): pick **baseline RF** (slightly higher AUC).  
> - For screening (catch more positives): pick **tuned RF** (higher recall).  
>   You can also threshold-tune the tuned RF to hit a target recall.

## Method

- **Data handling:** Treat biologically implausible zeros in (Glucose, BloodPressure, SkinThickness, Insulin, BMI) as missing (NaN).
- **Leakage-safe split:** Train/test split first; all imputation and scaling happen inside scikit-learn pipelines.
- **Models compared:** Logistic Regression, Random Forest, SVM (`class_weight="balanced"` for imbalance).
- **Tuning:** `RandomizedSearchCV` (5-fold Stratified CV, `scoring="roc_auc"`) over RF  
  (`n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`).
- **Diagnostics:** Confusion matrix and ROC curve for the chosen model.  

## How to run

### 1. Clone the repo
```bash
git clone https://github.com/Aakash050/Diabetes_Classification_Aakash_Kapadia.git
cd Diabetes_Classification_Aakash_Kapadia

### 2. Install dependencies
pip install -r requirements.txt

### 3. Install dependencies
### Recomended 
python fetch.py
### Or Download here and place in data folder
https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv
data/diabetes.csv

### 4. Run the notebook
jupyter notebook Project.ipynb

## IN CASE OF ALL ELSE FAILING: Getting the dataset
Download the CSV from [Plotly dataset](https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv)
and save it at:
`data/diabetes.csv`


