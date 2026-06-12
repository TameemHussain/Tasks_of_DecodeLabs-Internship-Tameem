# ─────────────────────────────────────────────────────────
#  Image Recognition System — Handwritten Digit Recognition
#  Model    : SVM (Support Vector Machine) with RBF kernel
#  Dataset  : sklearn digits (8x8 pixel images, 0–9)
#  Libraries: scikit-learn, Pillow, NumPy
# ─────────────────────────────────────────────────────────

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ── 1. Load Dataset ───────────────────────────────────────
print("=" * 58)
print("  Handwritten Digit Recognition  —  SVM + sklearn")
print("=" * 58)

digits = load_digits()

print(f"\n[Dataset] sklearn digits")
print(f"  Total samples  : {len(digits.data)}")
print(f"  Image size     : 8 x 8 pixels (64 features)")
print(f"  Classes        : {list(range(10))}  (digits 0-9)")
print(f"  Samples/class  : ~{len(digits.data) // 10}")

# Show what one image looks like as pixel grid
print("\n[Sample] Digit '5' ka pixel grid (0=white, 16=black):")
sample_idx = list(digits.target).index(5)
pixel_grid = digits.images[sample_idx]
for row in pixel_grid:
    print("  " + "  ".join(f"{int(v):2d}" for v in row))


# ── 2. Preprocess ─────────────────────────────────────────
X = digits.data        # shape: (1797, 64)
y = digits.target      # shape: (1797,)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

print(f"\n[Split] Train: {len(X_train)}  |  Test: {len(X_test)}")
print(f"[Norm]  Pixels StandardScaler se normalize kiye")


# ── 3. Train Model ────────────────────────────────────────
print("\n[Training] SVM with RBF kernel...")
model = SVC(kernel='rbf', C=10, gamma='scale', probability=True)
model.fit(X_train, y_train)
print("[Training] Complete ✓")


# ── 4. Evaluate ───────────────────────────────────────────
y_pred = model.predict(X_test)
acc    = accuracy_score(y_test, y_pred)

print(f"\n[Accuracy] {acc * 100:.1f}%")

print("\n[Classification Report]")
print(classification_report(y_test, y_pred,
      target_names=[str(i) for i in range(10)]))

print("[Confusion Matrix]  (rows=actual, cols=predicted)")
cm = confusion_matrix(y_test, y_pred)
header = "       " + "  ".join(f"{i:2}" for i in range(10))
print(header)
print("      " + "─" * (len(header) - 6))
for i, row in enumerate(cm):
    line = "  ".join(f"{v:2}" for v in row)
    print(f"  {i}  |  {line}")


# ── 5. Predict Single Sample ──────────────────────────────
print("\n[Demo] Akele sample ko predict karo:")
sample      = X_test[0]
actual      = y_test[0]
predicted   = model.predict([sample])[0]
proba       = model.predict_proba([sample])[0]
confidence  = proba[predicted] * 100

print(f"  Actual    : {actual}")
print(f"  Predicted : {predicted}  ({'✓ Correct' if predicted == actual else '✗ Wrong'})")
print(f"  Confidence: {confidence:.1f}%")
print(f"\n  Top 3 class probabilities:")
top3 = sorted(enumerate(proba), key=lambda x: x[1], reverse=True)[:3]
for cls, prob in top3:
    bar = "█" * int(prob * 30)
    print(f"    Digit {cls}: [{bar:<30s}] {prob*100:.1f}%")


# ── 6. Predict on Custom Image ────────────────────────────
def predict_custom_image(image_path):
    """
    Apni khud ki image predict karo.
    Image automatically 8x8 grayscale mein resize hogi.
    """
    img   = Image.open(image_path).convert('L')
    img   = img.resize((8, 8), Image.LANCZOS)
    arr   = np.array(img)
    arr   = 16 - (arr / 255.0 * 16)       # invert: white bg → 0, dark → 16
    flat  = arr.flatten().reshape(1, -1)
    flat  = scaler.transform(flat)
    pred  = model.predict(flat)[0]
    proba = model.predict_proba(flat)[0]
    return pred, proba[pred]


# ── 7. Save Sample Predictions as Image ───────────────────
def save_prediction_grid(n=10):
    """Test set se n predictions save karo as PNG."""
    cell = 80
    cols = 5
    rows = (n + cols - 1) // cols
    img  = Image.new('RGB', (cols * cell, rows * cell), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)

    for i in range(min(n, len(X_test))):
        # Reconstruct original pixel values from scaled data
        original_flat = scaler.inverse_transform([X_test[i]])[0]
        pixels = original_flat.reshape(8, 8)
        pixels = np.clip(pixels, 0, 16)

        col = i % cols
        row = i // cols
        ox  = col * cell + 5
        oy  = row * cell + 5

        thumb_size = 50
        thumb = Image.new('L', (8, 8))
        for r in range(8):
            for c in range(8):
                v = int(255 - (pixels[r, c] / 16.0) * 255)
                thumb.putpixel((c, r), v)
        thumb = thumb.resize((thumb_size, thumb_size), Image.NEAREST)
        img.paste(thumb, (ox, oy))

        pred   = y_pred[i]
        actual = y_test[i]
        color  = (34, 139, 34) if pred == actual else (200, 50, 50)
        draw.text((ox,      oy + thumb_size + 2), f"P:{pred}", fill=color)
        draw.text((ox + 25, oy + thumb_size + 2), f"A:{actual}", fill=(80, 80, 80))

    out_path = "/mnt/user-data/outputs/predictions_grid.png"
    img.save(out_path)
    print(f"\n[Saved] Predictions grid → {out_path}")


save_prediction_grid(n=20)
print("\n" + "=" * 58)
print("  Done! Model trained aur evaluated successfully.")
print("=" * 58)
