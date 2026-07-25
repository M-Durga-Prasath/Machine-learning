## 1. Confusion Matrix

A confusion matrix compares actual values with predicted values.

|                  | Predicted Positive | Predicted Negative |
|------------------|-------------------:|-------------------:|
| **Actual Positive** | TP (True Positive) | FN (False Negative) |
| **Actual Negative** | FP (False Positive) | TN (True Negative) |

- **TP:** Correctly predicted positive.
- **FP:** Incorrectly predicted positive.
- **FN:** Missed positive prediction.
- **TN:** Correctly predicted negative.

---

## 2. Accuracy

**Formula**

```text
Accuracy = (TP + TN) / Total
```

**Meaning**

- Overall percentage of correct predictions.
- Useful when classes are balanced.

---

## 3. Precision

**Formula**

```text
Precision = TP / (TP + FP)
```

**Meaning**

- Out of all predicted positives, how many were actually positive.
- Focuses on reducing **False Positives (FP)**.

**Remember:**

> High Precision = Fewer False Positives.

---

## 4. Recall

**Formula**

```text
Recall = TP / (TP + FN)
```

**Meaning**

- Out of all actual positives, how many the model found.
- Focuses on reducing **False Negatives (FN)**.

**Remember:**

> High Recall = Fewer False Negatives.

---

# Precision vs Recall

| Precision                                     | Recall                                         |
|-----------------------------------------------|------------------------------------------------|
| Measures correctness of positive predictions. | Measures how many actual positives were found. |
| Reduces False Positives.                      | Reduces False Negatives.                       |
| "Are predicted positives correct?"            | "Did we find all positives?"                   |

**Easy Memory**

- **Precision → Quality**
- **Recall → Coverage**

---

## 5. F1 Score

**Formula**

```text
F1 = 2 × (Precision × Recall)
     -------------------------
      Precision + Recall
```

**Why F1 Exists**

- Accuracy can be misleading on imbalanced datasets.
- Precision and Recall often trade off.
- F1 combines both into a single score.
- Best when both Precision and Recall are important.

**Remember**

> F1 = Balance between Precision and Recall.

---

## 6. ROC Curve

ROC (Receiver Operating Characteristic) shows how:

- True Positive Rate (TPR) changes
- False Positive Rate (FPR) changes

when the prediction threshold changes.

Lower threshold:
- More positives detected
- More false positives

Higher threshold:
- Fewer false positives
- More missed positives

---

## 7. ROC-AUC

**AUC = Area Under the ROC Curve**

**What it measures**

- How well the model separates positive and negative classes.
- Higher AUC means better ranking ability.

### Interpretation

- **AUC = 1.0** → Perfect classifier
- **AUC ≈ 0.9** → Excellent
- **AUC ≈ 0.8** → Good
- **AUC = 0.5** → Random guessing

**Remember**

> ROC-AUC measures the model's ability to rank positives above negatives across all thresholds.

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


### Difference between Precision and Recall

- **Precision:** Out of predicted positives, how many are correct?
- **Recall:** Out of actual positives, how many did the model find?

---

### Why does F1 exist?

- To balance Precision and Recall into one metric.
- Useful when classes are imbalanced or both metrics matter.

---

### What does ROC-AUC measure?

- It measures how well a model distinguishes positive and negative classes across different thresholds.
- Higher AUC = Better discrimination.

---

- **Accuracy** → Overall correctness.
- **Precision** → Quality of positive predictions.
- **Recall** → Coverage of actual positives.
- **F1 Score** → Balance of Precision and Recall.
- **ROC Curve** → TPR vs FPR at different thresholds.
- **ROC-AUC** → Overall ranking ability of the model.