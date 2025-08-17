Diabetes Prediction README: 
I predicted the likelihood of diabetes from different factors, such as glucose, BMI, and more, using a leakage proof workflow, achieving a recall of around 75%. 

My pipeline was EDA -> Split -> Pipeline (false zeroes to Nans, imputed, scaled) -> Model comparison -> Best model (RF) hypertuning -> Diagnostics

Results (test set): 

Best AUC Option: Random Forest - ROC AUC Score: 0.82 - Accuracy: 0.78 - Precision: 0.7 - Recall: 0.61 - F1 Score: 0.65
Highest Recall Option: Random Forest - ROC AUC Score: 0.82 - Accuracy: 0.74 - Precision: 0.6 - Recall: 0.74 - F1 Score: 0.67
Validation: 5-Fold train CV AUC: 0.84 - Test AUC: 0.82. Since these are relatively close, we have limitted overfitting

Based on our goal, we can choose different models. If we want to use this for initial screening, our tuned Random Forest model is going to be best, due to our highest recall compared to all other models. However if we want the most accurate model, our original Random Forest is going to be better

Methods: 
Treated impossible 0's, such as BMI, etc, as missing, and imputed using median
Test/train first, all imputing/scaling happens inside the pipeline
Models: Random Forest, SVC, Logisitic Regression
Tuning: Randomized Search CV, 5-Fold CV, scoring = "roc_auc", on Random Forest. Used n_estimators, max_depth, min_samples_split, min_samples_leaf, max_features.
Diagnostics: Confusion matrix and ROC AUC curve for RF

How to run: 

```bash
pip install -r requirements.txt
# Place dataset at data/diabetes.csv (or use a fetch script)
jupyter notebook Project.ipynb
