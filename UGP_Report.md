# 📝 Project Report

## 📌 Real World Application of Hankel Transformation

### 🔹 Introduction

Integral transforms are mathematical operations that convert a function into another function using an integral. This simplifies solving certain problems in a transformed space.

**General definition:**

```
F(s) = ∫ K(s, t) f(t) dt (from a to b)
```

Where:
- `f(t)`: original function  
- `F(s)`: transformed function  
- `K(s,t)`: kernel of the transform  

#### 🔸 Types of Integral Transforms

1. **Fourier Transform** – time → frequency
2. **Laplace Transform** – solving differential equations
3. **Hankel Transform** – radial/cylindrical symmetry
4. **Z-Transform** – discrete-time signal processing
5. **Wavelet Transform** – time-frequency analysis

---

### 🔹 Hankel Transform

Designed for problems with radial symmetry (distance from center matters, angle doesn't). Also known as **Fourier-Bessel Transform**.

#### Formula:

```
Fv(k) = ∫ f(r) Jv(kr) r dr (from 0 to ∞)
```

- `Jv`: Bessel function of first kind  
- `v`: order of Bessel function  

#### Inverse:

```
f(r) = ∫ Fv(k) Jv(kr) r dr (from 0 to ∞)
```

---

### 🔹 Bessel Functions

Solutions to Bessel's differential equation:

```
x²(d²y/dx²) + x(dy/dx) + (x² − α²)y = 0
```

Series representation:

```
Jα(x) = Σ (−1)^m / (m! * Γ(m + α + 1)) * (x/2)^(2m+α)
```

- `Γ(z)`: gamma function  
- Integer α: finite at origin  
- Negative α: diverge as x → 0  
- Behave like damped sine waves

---

### 🔹 Uses of Hankel Transform

- 🌍 Seismology (circular Earth models, earthquakes, undersea volcanoes)
- 🧠 Medical Imaging (especially MRI)
- 🔬 Light diffraction through circular apertures
- 🔄 Radial signal processing
- 🔥 Heat flow in disks or rods

---

## 🧪 Application on Medical Images

---

### 🎯 Motivation & Objective

Used **Brain MRI images** (radial symmetry, accessible).  
Goals:
- Explore Hankel transform on medical images
- Reduce computation
- Pre-extract radial features for ML models

---

### 📥 Initial Data Collection

Downloaded from Kaggle → manually filtered.

**[Dataset link](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c)**

---

### 🔧 Dataset Preprocessing

- Converted images to grayscale  
- Resized for uniformity  
- Combined into two folders:  
  - `processed_dataset/positive/`  
  - `processed_dataset/negative/`  

---

### 🔄 Processing Stages

---

#### ✅ 1. Predefined Hankel Transform

- Used `scipy`'s built-in transform
- Didn’t work well due to asymmetry in tumour images
- Resulted in **warnings: "integral slowly convergent or divergent"**

---

#### ✅ 2. Custom Radial Profile → Hankel Transform

- Computed average pixel intensity per ring (radially)
- Plotted radial profile + Hankel transform

➡️ Found **no strong differentiation** between classes (radial means flattened differences)

---

#### ✅ 3. Divide Image into Patches (16)

- Each patch analyzed separately
- Applied Hankel Transform with `k = 50`
- Extracted features:
  - Mean, Std, Skewness, Kurtosis, Peak

Saved:
- Per-image `.csv` with features
- Summary: Average & Peak values

---

#### 📊 Plotted Results:
- Slight distinction in **skewness & kurtosis**
- Calculated **correlation** between classes (positive vs. negative)

➡️ Inter-class correlation: low  
➡️ Intra-class (within class): high between mean & std

---

#### ✅ 4. Trained Random Forest Classifier

- Train/Val/Test: **70:15:15**
- Random seed fixed
- Accuracy (Unweighted): **89.137%**

##### Issues:
- Class imbalance (positive > negative)
- Solution 1: **Class-Weighted**  
  ➡️ Accuracy: **87.351%**

- Solution 2: **Synthetic samples (SMOTE)**  
  ➡️ Accuracy: **85.119%**, better **recall**, small **precision** drop

---

## ✅ Result & Learnings

- Gained understanding of Hankel Transform’s real-world limits
- MRI images had challenges (non-perfect radial symmetry)
- Feature differentiation weak in raw form
- Random Forest + extracted features gave good baseline

---

## 📚 References

1. Wikipedia  
2. Google  
3. ResearchGate  
4. IEEE Xplore  
5. Kaggle  
6. Brain MRI Dataset: [Kaggle](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c)
