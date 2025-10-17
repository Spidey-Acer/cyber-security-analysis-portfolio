# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an academic portfolio for the **Cyber Security Analytics (UFCFFY-15-M)** module at UWE Bristol. The portfolio comprises three separate defensive security activities analyzing logs, malware domains, and SIEM-based attack detection.

**IMPORTANT - Security Scope**: This repository is strictly for **defensive security analysis only**. All work involves detection, analysis, and understanding of security threats - NOT creating malicious tools. The activities analyze existing logs and datasets to identify attacks and build detection systems.

## Portfolio Structure

The repository contains three independent activities, each with its own data, notebooks, and submission requirements:

- `activity1-log-analysis/` - Web server log analysis (20% of grade)
- `activity2-dga-classification/` - Machine learning DGA classifier (35% of grade)
- `activity3-siem-attacks/` - SIEM attack simulation and detection (45% of grade)

Each activity has specific submission artifacts (`STUDENTID-TASK1.ipynb`, `STUDENTID-TASK2.ipynb`, `STUDENTID-TASK3.pdf`) that must be completed independently.

## Development Environment

### Python Environment Setup

```bash
# Create and activate virtual environment
python -m venv venv

# Windows activation
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### Running Jupyter Notebooks

```bash
# Activate virtual environment first
venv\Scripts\activate

# Launch Jupyter
jupyter notebook

# Navigate to the appropriate activity folder
# - activity1-log-analysis/notebooks/
# - activity2-dga-classification/notebooks/
```

### Key Dependencies

- **Data Science**: pandas, numpy, matplotlib, seaborn
- **Machine Learning**: scikit-learn, shap
- **Network Analysis**: networkx (for Activity 1 Q9)
- **Jupyter**: jupyter, notebook, ipykernel

## Activity-Specific Guidance

### Activity 1: Web Server Log Analysis

**Primary Files**:
- `notebooks/STUDENTID-TASK1.ipynb` - Main submission notebook (must have all cells executed)
- `utils/log_analysis_helpers.py` - Helper functions for parsing logs
- `data/p2-pitta_25sept.txt` - Large log file (excluded from git via `.gitignore`)

**Data Loading Pattern**:
The log data uses whitespace-delimited format that requires special handling:
```python
data = pd.read_csv(data_file, delim_whitespace=True)
# Column shifting is required - see notebook for full pattern
```

**Key Analysis Requirements**:
- Questions 1-8: Guided data analysis (frequencies, filtering, visualizations)
- Question 9: NetworkX graph visualization of top 20 IPs (4 marks)
- Question 10: Unguided investigation to identify suspicious activity (8 marks - highest value)

**Common Challenges**:
- Log parsing errors due to inconsistent whitespace
- Large file sizes affecting memory with pandas operations
- NetworkX node sizing requires activity-based scaling

### Activity 2: DGA Classification

**Primary Files**:
- `notebooks/STUDENTID-TASK2.ipynb` - Main submission notebook
- `src/feature_engineering.py` - Comprehensive feature extraction utilities
- `data/dga-24000.csv` - Domain dataset (24,000 samples)

**Architecture**:
The feature engineering module provides two distinct approaches:
1. **Statistical Features** (`extract_linguistic_features`): Length, entropy, character ratios, n-gram statistics, vowel/consonant patterns
2. **TF-IDF N-grams** (`TfidfVectorizer`): Character-level 2-4 grams

**Model Requirements**:
- Must implement at least 3 classifiers (template includes: Logistic Regression, Random Forest, MLP)
- Must achieve >90% accuracy
- Must use confusion matrices for evaluation
- Must use SHAP for explainability (TreeExplainer for Random Forest)

**Feature Engineering Utilities**:
- `calculate_entropy(text)` - Shannon entropy calculation
- `extract_linguistic_features(domain)` - Returns 20+ statistical features
- `extract_advanced_features(domain)` - Includes pronounceability scoring
- `extract_features_batch(domains)` - Efficient batch processing returning DataFrame

**Performance Considerations**:
- SHAP computation can be slow - use sampling for large test sets (`X_sample = X_test[:100]`)
- Random Forest with 100 estimators provides good balance of speed/accuracy
- MLP early_stopping=True prevents overfitting and saves time

### Activity 3: SIEM Attack Simulation

**Primary Files**:
- `documentation/STUDENTID-TASK3.pdf` - Final report (max 1500 words)
- `documentation/attack_notes.md` - Document attack procedures
- `documentation/setup_guide.md` - Infrastructure configuration
- `screenshots/` - Evidence organized by infrastructure/attacks/detection

**Infrastructure Options**:
1. **GoibhniUWE** (recommended for beginners) - Pre-configured VM from Blackboard
2. **DetectionLab** (advanced) - Full SIEM environment with Splunk
3. **Custom** - Student-configured SIEM + target + attack VMs

**Documentation Strategy**:
This activity requires **visual evidence**. Screenshots must show:
- Infrastructure topology and configuration
- Attack execution (commands, tools, progress)
- SIEM detection (alerts, logs, queries, timelines)

Suggested naming: `01_infrastructure_topology.png`, `02_attack1_execution.png`, `03_attack1_detection.png`

**Report Focus**:
The 1500-word limit requires concise technical writing covering:
- Infrastructure design and setup
- Attack methodology and execution
- Detection mechanisms and evidence
- Analysis and conclusions

## Data Files and Git Management

**Large Files Excluded** (see `.gitignore`):
- `*.txt`, `*.log`, `*.csv` (except `dga-24000.csv` which is explicitly included)
- `*.pkl`, `*.h5`, `*.joblib`, `*.model` (trained models)
- `*.png`, `*.jpg`, `*.pdf` (except `STUDENTID-TASK3.pdf`)

Students must obtain:
- `p2-pitta_25sept.txt` - Personalized log file based on UWE username
- `dga-24000.csv` - Available in course materials (this one IS tracked in git)

## Submission Requirements

**Critical Pre-Submission Checklist**:
1. All notebook cells must be **executed with visible outputs** (staff will not re-run)
2. Replace `[ENTER YOUR STUDENT ID]` in all submission files
3. Verify file naming exactly matches requirements:
   - `STUDENTID-TASK1.ipynb`
   - `STUDENTID-TASK2.ipynb`
   - `STUDENTID-TASK3.pdf`
4. Activity 3 report must be ≤1500 words
5. Academic integrity: Acknowledge GenAI usage if applicable

**Deadline**: Thursday, 11th December 2025 at 14:00

## Common Commands

```bash
# Run Jupyter for any activity
jupyter notebook

# Test data science environment
python -c "import pandas, numpy, sklearn, shap; print('All packages installed!')"

# Check pandas/numpy versions (compatibility issues rare but possible)
pip list | grep -E "pandas|numpy|scikit-learn|shap"

# For Activity 2: Test feature engineering module
cd activity2-dga-classification/src
python feature_engineering.py  # Runs example test cases
```

## Working with Notebooks

**Activity 1 Workflow**:
1. Ensure `data/p2-pitta_25sept.txt` exists
2. Questions 1-8 are sequential - complete in order
3. Question 9 (NetworkX) requires understanding of node sizing logic
4. Question 10 is open-ended - requires analytical reasoning beyond code execution

**Activity 2 Workflow**:
1. Data exploration first (understand class distribution, domain characteristics)
2. Implement Feature Approach 1 (statistical) - test with all 3 classifiers
3. Implement Feature Approach 2 (n-grams) - test with all 3 classifiers
4. Compare results and select best model for SHAP analysis
5. Complete analysis with conclusions section

**Markdown Cells**: Both main notebooks use markdown extensively for documentation. When adding analysis, maintain the clear sectioned structure with headers.

## Academic Context

**Module**: UFCFFY-15-M Cyber Security Analytics 2025-26
**Institution**: UWE Bristol
**Module Leader**: Prof. Phil Legg (Phil.Legg@uwe.ac.uk)
**Q&A Form**: https://forms.office.com/e/yxFJZDraRG

**Grading Breakdown**:
- Activity 1: 20% (Questions 1-8: 1 mark each, Q9: 4 marks, Q10: 8 marks)
- Activity 2: 35% (Feature engineering, classification, explainability)
- Activity 3: 45% (Infrastructure, attack execution, detection, reporting)
- Pass mark: 50% overall (across all three activities)

**GenAI Usage**: Allowed in assistive role only. Must be acknowledged in submissions.

## Notes for Claude Code

**When analyzing suspicious activity** (Activity 1 Q10):
- Look for high-volume IPs (statistical outliers: mean + 3*std)
- Calculate error rates (404s, 400s, 500s) per IP
- Analyze temporal patterns (off-hours activity: midnight-6am)
- Identify scanning behavior (many 404s from single IP)
- Check for injection patterns in query strings (SQL keywords in `cs-uri-query`)

**When engineering features** (Activity 2):
- Use the existing `feature_engineering.py` module - it's comprehensive
- Statistical features work well for tree-based models (Random Forest)
- N-gram features excel with Logistic Regression and MLP
- Combine approaches if struggling to reach 90% accuracy threshold

**When working with SHAP**:
- Use `TreeExplainer` for Random Forest (faster than KernelExplainer)
- Sample data for visualization (`X_sample = X_test[:100]`) to avoid long waits
- `shap.summary_plot()` requires `show=False` in Jupyter to render properly

**Data Privacy**: This is coursework - no real-world sensitive data. However, log analysis should still follow professional practices (aggregation, anonymization where appropriate).
