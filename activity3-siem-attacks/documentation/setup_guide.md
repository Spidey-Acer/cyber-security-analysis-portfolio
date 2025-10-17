# Setup Guide

Instructions to setup SIEM and environment.
# Quick Setup Guide
## Cyber Security Analytics Portfolio

---

## 🚀 Initial Setup (5 minutes)

### Step 1: Create Repository Structure

```bash
# Create main directory
mkdir UFCFFY-15-M-CSA-Portfolio
cd UFCFFY-15-M-CSA-Portfolio

# Create folder structure
mkdir -p activity1-log-analysis/{data,notebooks,outputs/{figures,results},utils}
mkdir -p activity2-dga-classification/{data/{processed},notebooks,models/saved_models,outputs/{figures,results},src}
mkdir -p activity3-siem-attacks/{documentation,screenshots/{infrastructure,attacks,detection},configs/siem_configs,scripts/attack_scripts}
mkdir -p docs

# Create placeholder files
touch activity1-log-analysis/data/.gitkeep
touch activity2-dga-classification/data/.gitkeep
touch activity3-siem-attacks/screenshots/.gitkeep
```

### Step 2: Initialize Git Repository

```bash
# Initialize git
git init

# Create .gitignore (copy content from artifact)
# Create README.md (copy content from artifact)
# Create requirements.txt (copy content from artifact)

# Initial commit
git add .
git commit -m "Initial repository setup"
```

### Step 3: Setup Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import pandas, numpy, sklearn, shap; print('All packages installed successfully!')"
```

### Step 4: Add Your Data Files

**Important:** Your data file is too large for Git!

```bash
# Place your data file
# Copy p2-pitta_25sept.txt to activity1-log-analysis/data/

# For Activity 2, download the DGA dataset
# Place dga-24000.csv in activity2-dga-classification/data/
```

---

## 📊 Activity 1: Getting Started (10 minutes)

### Create Your Notebook

1. Copy the starter code from the artifact "Activity 1 - STUDENTID-TASK1.ipynb"
2. Save it as: `activity1-log-analysis/notebooks/STUDENTID-TASK1.ipynb`
3. Replace `STUDENTID` with your actual student ID
4. Update the `data_file` path to point to your data file

### Quick Test

```python
# Open Jupyter
jupyter notebook

# Navigate to activity1-log-analysis/notebooks/
# Open STUDENTID-TASK1.ipynb
# Run the first few cells to verify data loads correctly
```

### Troubleshooting Data Loading

If you get parsing errors:

```python
# Try these alternative loading methods:

# Method 1: Specify delimiter
data = pd.read_csv(data_file, sep='\s+', engine='python')

# Method 2: Skip header rows if needed
data = pd.read_csv(data_file, delim_whitespace=True, skiprows=1)

# Method 3: Read as text first to inspect
with open(data_file, 'r') as f:
    print(f.read(1000))  # Print first 1000 chars
```

---

## 🤖 Activity 2: Getting Started (10 minutes)

### Setup Notebooks

```bash
cd activity2-dga-classification/notebooks

# Create your main submission notebook
# Copy code from "Activity 2 - STUDENTID-TASK2.ipynb" artifact
# Save as: STUDENTID-TASK2.ipynb

# Optional: Create exploration notebooks
jupyter notebook 01_data_exploration.ipynb
jupyter notebook 02_feature_engineering.ipynb
jupyter notebook 03_model_training.ipynb
```

### Copy Utility Scripts

```bash
cd ../src

# Copy the feature engineering utility code
# Create feature_engineering.py with code from artifact
```

### Quick Test

```python
# In Jupyter, test data loading
import pandas as pd
df = pd.read_csv('../data/dga-24000.csv')
print(df.head())
print(df['Family'].value_counts())
```

---

## 🛡️ Activity 3: Getting Started (15 minutes)

### Option 1: GoibhniUWE (Recommended for Beginners)

1. **Download GoibhniUWE** from Blackboard
2. **Watch the video tutorial** (linked in assignment)
3. **Extract and run** the VM environment
4. **Document your setup** with screenshots

### Option 2: DetectionLab (Advanced)

1. **Prerequisites:**
   - Vagrant
   - VirtualBox
   - 16GB+ RAM
   - 100GB+ disk space

2. **Setup:**
```bash
git clone https://github.com/clong/DetectionLab.git
cd DetectionLab/Vagrant
vagrant up
```

3. **Access Splunk:** http://localhost:8000

### Option 3: Custom Setup

1. **Components needed:**
   - SIEM platform (Splunk/Wazuh/Elastic)
   - Target VM (Windows/Linux)
   - Attack VM (Kali Linux)

2. **Network configuration:**
   - Create host-only network
   - Configure static IPs
   - Enable logging forwarding

### Documentation Strategy

Create a structure in `activity3-siem-attacks/documentation/`:

```markdown
attack_notes.md
- Document each attack as you perform it
- Include commands used
- Note observations

setup_guide.md
- Document your infrastructure setup
- Include configuration details
- List challenges and solutions
```

---

## 📸 Screenshot Strategy for Activity 3

### Essential Screenshots to Capture:

1. **Infrastructure Setup (5-7 screenshots)**
   - Network topology
   - VM configurations
   - SIEM dashboard setup

2. **Attack Execution (3-5 per attack)**
   - Command/tool execution
   - Target system state
   - Progress indicators

3. **Detection Evidence (3-5 per attack)**
   - SIEM alerts
   - Log entries
   - Timeline views
   - Query results

### Screenshot Naming Convention:

```
01_infrastructure_topology.png
02_siem_initial_dashboard.png
03_attack1_bruteforce_execution.png
04_attack1_siem_detection.png
05_attack1_log_evidence.png
...
```

---

## 📝 Workflow Tips

### Activity 1 Workflow

1. **Day 1-2:** Complete Questions 1-8 (guided questions)
2. **Day 3-4:** Work on Question 9 (network graph)
3. **Day 5-7:** Investigate suspicious activity (Question 10)
4. **Day 8:** Review and ensure all cells executed

### Activity 2 Workflow

1. **Week 1:** Data exploration and feature engineering approach 1
2. **Week 2:** Feature engineering approach 2 and model training
3. **Week 3:** Performance comparison and SHAP analysis
4. **Week 4:** Refinement and documentation

### Activity 3 Workflow

1. **Week 1:** Infrastructure setup and documentation
2. **Week 2:** Attack execution and screenshot collection
3. **Week 3:** Detection analysis and evidence gathering
4. **Week 4:** Report writing (1500 words)

---

## 🔍 Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'X'"
**Solution:** 
```bash
pip install X
# Or reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: "Large file won't load in pandas"
**Solution:**
```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv(file, chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
data = pd.concat(chunks)
```

### Issue: "Jupyter kernel dies when running models"
**Solution:**
- Reduce dataset size for testing
- Use `n_jobs=1` in sklearn models
- Increase VM memory allocation
- Save models incrementally

### Issue: "SHAP taking too long"
**Solution:**
```python
# Use smaller sample
sample_size = 100
X_sample = X_test[:sample_size]
shap_values = explainer.shap_values(X_sample)
```

---

## ✅ Pre-Submission Checklist

### Week Before Submission

- [ ] All notebooks have cells executed
- [ ] Student ID updated in all files
- [ ] Word count verified for Activity 3 (≤1500)
- [ ] All screenshots included and referenced
- [ ] Academic integrity checked (citations, originality)
- [ ] Files named correctly:
  - `STUDENTID-TASK1.ipynb`
  - `STUDENTID-TASK2.ipynb`
  - `STUDENTID-TASK3.pdf`

### Day of Submission

- [ ] Test open all files to verify they work
- [ ] Check file sizes (Blackboard limits)
- [ ] Submit to correct assignment dropbox
- [ ] Verify submission confirmation received
- [ ] Keep backup copies

---

## 📚 Useful Resources

### Python & Data Science
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)

### Machine Learning
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Confusion Matrix Guide](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

### SIEM & Security
- [Splunk Fundamentals](https://docs.splunk.com/)
- [Wazuh Documentation](https://documentation.wazuh.com/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Atomic Red Team](https://atomicredteam.io/)

### Academic Writing
- [UWE Harvard Referencing](https://www.uwe.ac.uk/study/study-support/study-skills/referencing)
- [Academic Writing Guide](https://www.uwe.ac.uk/study/study-support/study-skills/reading-and-writing)

---

## 🆘 Getting Help

1. **Module Q&A Form:** [Online Form](https://forms.office.com/e/yxFJZDraRG)
2. **Module Leader:** Phil.Legg@uwe.ac.uk
3. **On-site Teaching Sessions:** Attend labs for hands-on help
4. **Blackboard Forums:** Check for common questions/answers

---

Good luck with your portfolio! 🎓