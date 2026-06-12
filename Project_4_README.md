# Handwritten Digit Recognition System

A machine learning system that recognizes handwritten digits (0–9) using an SVM classifier trained on the sklearn digits dataset.

---

## Requirements

```bash
pip install scikit-learn pillow numpy
```

---

## How to Run

```bash
python recognition_system.py
```

---

## How It Works

| Step | Description |
|------|-------------|
| Dataset | Loads sklearn's built-in `digits` dataset — 1,797 images at 8×8 pixels each |
| Preprocessing | 80/20 train-test split with `StandardScaler` normalization |
| Model | Support Vector Machine (SVM) with RBF kernel (`C=10`, `gamma='scale'`) |
| Evaluation | Prints accuracy score, classification report, and confusion matrix |
| Demo | Predicts a single sample and displays confidence bars |
| Output | Saves `predictions_grid.png` — green = correct, red = incorrect |

---

## Predict Your Own Image

```python
pred, confidence = predict_custom_image("my_digit.png")
print(f"Digit: {pred}  |  Confidence: {confidence*100:.1f}%")
```

> The image should contain a single clearly written digit — dark ink on a white background works best.

---

## Expected Output

```
Accuracy: 98.1%

Actual    : 5
Predicted : 5  (✓ Correct)
Confidence: 95.1%

Top 3 class probabilities:
  Digit 5: [████████████████████████████  ] 95.1%
  Digit 9: [                              ]  1.2%
  Digit 8: [                              ]  1.1%
```

---

## Dataset Details

| Property | Value |
|----------|-------|
| Total samples | 1,797 |
| Classes | 10 (digits 0–9) |
| Samples per class | ~179 |
| Image size | 8 × 8 pixels |
| Features | 64 (flattened pixel values) |

---

## Project Structure

```
recognition_system.py   ← main script
predictions_grid.png    ← output: visual grid of predictions
README.md               ← this file
```
