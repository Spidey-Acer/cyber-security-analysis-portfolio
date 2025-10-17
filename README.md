# UFCFFY-15-M Cyber Security Analytics Portfolio

**Student ID:** [YOUR_STUDENT_ID]  
**Module:** Cyber Security Analytics 2025-26  
**Institution:** UWE Bristol

## 📋 Portfolio Overview

This repository contains three portfolio activities for the Cyber Security Analytics module:

1. **Activity 1 (20%)** - Web Server Log Analysis
2. **Activity 2 (35%)** - DGA Classification with Machine Learning
3. **Activity 3 (45%)** - SIEM-Based Attack Simulation

**Submission Deadline:** Thursday, 11th December 2025 at 14:00

---

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd UFCFFY-15-M-CSA-Portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your Data Files
- Place `p2-pitta_25sept.txt` in `activity1-log-analysis/data/`
- Place `dga-24000.csv` in `activity2-dga-classification/data/`

---

## 📁 Repository Structure

```
├── activity1-log-analysis/       # Web server log analysis
├── activity2-dga-classification/ # DGA ML classification
├── activity3-siem-attacks/       # SIEM attack simulation
└── docs/                         # Assignment documentation
```

---

## 📊 Activity 1: Web Server Log Analysis

**Location:** `activity1-log-analysis/`

### Tasks
- Analyze web server logs to identify malicious activity
- Complete 10 questions using Python/Pandas
- Identify suspicious IP addresses and explain reasoning

### Key Files
- `STUDENTID-TASK1.ipynb` - Main submission notebook
- `exploration.ipynb` - Scratch work and experiments

---

## 🤖 Activity 2: DGA Classification

**Location:** `activity2-dga-classification/`

### Tasks
- Build ML classifier for Domain Generation Algorithms
- Test at least 2 feature engineering approaches
- Implement 3 different classifiers
- Achieve >90% accuracy
- Explain model performance with SHAP

### Key Files
- `STUDENTID-TASK2.ipynb` - Main submission notebook
- Feature engineering and model training scripts in `src/`

---

## 🛡️ Activity 3: SIEM Attack Simulation

**Location:** `activity3-siem-attacks/`

### Tasks
- Set up virtualized infrastructure (GoibhniUWE, DetectionLab, etc.)
- Execute attacks on the system
- Detect attacks using SIEM platform
- Write comprehensive report (max 1500 words)

### Key Files
- `STUDENTID-TASK3.pdf` - Final report
- Screenshots documenting infrastructure, attacks, and detection

---

## 📝 Submission Checklist

Before submitting to Blackboard, ensure:

- [ ] `STUDENTID-TASK1.ipynb` - All cells executed and saved
- [ ] `STUDENTID-TASK2.ipynb` - All cells executed and saved
- [ ] `STUDENTID-TASK3.pdf` - Report completed (≤1500 words)
- [ ] Student ID updated in all notebooks
- [ ] All outputs visible (staff won't re-run notebooks)
- [ ] Academic integrity declaration acknowledged

---

## 🎯 Grading Criteria

| Activity | Weight | Focus Areas |
|----------|--------|-------------|
| Activity 1 | 20% | Data analysis, suspicious activity identification |
| Activity 2 | 35% | Feature engineering, ML implementation, explainability |
| Activity 3 | 45% | Infrastructure setup, attack execution, detection |

**Pass Mark:** 50% overall

---

## 📚 Resources

- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [DetectionLab](https://www.detectionlab.network/)
- [Atomic Red Team](https://atomicredteam.io/)

---

## ⚠️ Important Notes

- **Use your unique dataset** for Activity 1 (based on UWE username)
- **Large files excluded from git** - Data files are in `.gitignore`
- **GenAI usage allowed** in assistive role only (must acknowledge)
- **Academic integrity** - All work must be your own

---

## 📧 Contact

**Module Leader:** Prof. Phil Legg (Phil.Legg@uwe.ac.uk)  
**Q&A Form:** [Online Q&A](https://forms.office.com/e/yxFJZDraRG)

---

## 📄 License

This is academic coursework for UWE Bristol. All rights reserved.