# FEDERATED-LEARNING-
# 🤖 CloudyFL: A Cloudlet-Based Federated Learning Framework for Sensing User Behavior

> 📍 NSS College of Engineering, Palakkad  
> 🧑‍💼 Presented by: **Hafsa Y**  
> 🎓 Guide: Prof. Dr. Deepak Mishra, Avionics Dept, IIST  

---

## 🚀 Overview

CloudyFL is a cloudlet-assisted **Federated Learning (FL)** framework for **on-device user behavior recognition** using wearable sensors. It enables **privacy-preserving** and **efficient learning** from distributed IoT data without sharing raw data.This is the replication of method used in cloudyFL paper.Main intention is to  understand the difference between FedRS and FedAvg.

---

## 📊 Dataset

- **UCI Daily and Sports Activities Dataset**
- 9 sensors per body unit:  
  - `x, y, z` Accelerometer  
  - `x, y, z` Gyroscope  
  - `x, y, z` Magnetometer
- Units: Torso, Left/Right Arm, Left/Right Leg
- Input shape: `(N, 125, 45)`  
  - `N`: Number of samples  
  - `125`: Time steps  
  - `45`: Sensor features

---

## Model Architecture

### ✅ Bi-LSTM + Attention

1. **Bi-directional LSTM**: Hidden size = 128 → Output: `(B, 125, 256)`
2. **Attention Layer**:
   - Weight: `softmax(Wa · out)` → `(B, 125)`
   - Context Vector: `ctx = Σ (weight · out)`
3. **Fully Connected Layer**: `logits = Wf · ctx + b`
4. **Restricted Softmax**: Top-k class logits selected, then softmax applied

> Optimizer: **Adam**  
> Loss Function: **Cross-Entropy**

---

## Training Pipeline (Federated Setup)

### Step-by-step:

1. **Create Zones**: Divide dataset into 5 clients (Non-IID actor-based)
2. **Initialize Model** per zone with global weights
3. **Local Training** using attention-based Bi-LSTM
4. **Send Weights to Server**
5. **FedAvg Aggregation**:
   \[
   w_{global} = \frac{1}{K} \sum_{k=1}^{K} w_k
   \]
6. **Update Global Model**
7. **Send Global Model to Clients**
8. Repeat for multiple rounds
9. Compare Local vs Global Performance
10. Evaluate: Accuracy, Precision, Recall, F1-score

---
## 📂 Project Structure

project/
├── data/ # Preprocessed UCI sensor data
├── models/ # BiLSTM and Attention definitions
├── zones/ # Client-specific (zone-wise) data splits
├── train_local.py # Local training logic
├── aggregate.py # FedAvg / FedRS implementation
├── evaluation.py # Accuracy, Precision, F1-score computations
└── main.py 

## 🔒 Privacy & Security

CloudyFL defends against gradient leakage using:

| Technique              | Purpose                                             |
|------------------------|-----------------------------------------------------|
| 🔐 Differential Privacy | Adds noise to model updates (local DP)              |
| 🔐 Secure Aggregation  | Encrypts gradients before aggregation                |
| 🔐 Homomorphic Encryption | Enables computation on encrypted data              |
| 🔐 Split Learning      | Only activations are sent; raw data never leaves device |

> Attack Mitigation: Defends against "Deep Leakage from Gradients" (Zhu et al., 2019)

---

##  Algorithms Used

| Algorithm | Description |
|----------|-------------|
| **FedAvg** | Standard federated averaging of weights |
| **FedRS**  | Restricted softmax for non-IID data to avoid gradient noise |

### ❌ Why Not Only FedRS?

- Biased to local classes (poor generalization)
- Overfitting risk
- Class imbalance issues
- Sensitive to temperature tuning
- Not privacy-aware by itself

---

 📈 Final Global Evaluation

| Metric    | Value   |
|-----------|---------|
| Accuracy  | 0.8973  |
| Precision | 0.9144  |
| Recall    | 0.8973  |
| F1-Score  | 0.8944  |

---

## 📚 Related Work

## 📚 Related Work

- [CloudyFL: A Cloudlet-Based Federated Learning Framework](https://ieeexplore.ieee.org/document/9694135) – Qingyuan Gong et al.
- [FedML-HE: Efficient HE-Based FL System](https://arxiv.org/abs/2106.07976)
- [Differential Privacy for Sensitive Health Data](https://arxiv.org/abs/1812.01484) – Choudhury et al.

---

##  Tools & Frameworks

- Python 🐍
- PyTorch 🔥
- UCI HAR Dataset 📊

---

## 🌐 Repositories You Can Explore

- [`OpenMined/PySyft`](https://github.com/OpenMined/PySyft)
- [`adap/flower`](https://github.com/adap/flower)
- [`google-parfait/tensorflow-federated`](https://github.com/google-parfait/tensorflow-federated)
- [`FedML-AI/FedML`](https://github.com/FedML-AI/FedML)

---
## Dataset 
['UCI DSA Dataset'](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities)
## Acknowledgements

- Guide: **Dr. Deepak Mishra**, Avionics, IIST
- Department: **Electronics & Communication**, NSSCE
- Tools: UCI, PyTorch



