# 🎯 MEGA COMPREHENSIVE IMPLEMENTATION PLAN
## Cyber Security Analytics Portfolio - Template to Submission Ready

**Current Status:** ~8-10% Complete (Templates Ready, No Execution)
**Target:** 100% Submission Ready by December 11, 2025
**Time Required:** ~80-100 hours of focused work

---

## 📅 TIMELINE OVERVIEW (Recommended 4-Week Sprint)

```
Week 1 (20-25 hours): Activity 2 Complete + Activity 1 Execution
Week 2 (25-30 hours): Activity 1 Complete + Activity 3 Infrastructure + Attack Planning
Week 3 (25-30 hours): Activity 3 Attack Execution + Detection + Screenshots
Week 4 (15-20 hours): Activity 3 Report Writing + Final Review + Submission Prep
```

---

# 🚀 PHASE 1: QUICK WINS (Activity 2 - Priority 1)
**Estimated Time:** 8-12 hours
**Grade Impact:** 35% of total portfolio
**Why First:** Complete template exists, straightforward execution, builds confidence

## Task 1.1: Environment Setup & Data Verification
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
I need to set up my Python environment for Activity 2 (DGA Classification). Please:

1. Verify my virtual environment is activated
2. Check that all required packages are installed (scikit-learn, shap, pandas, numpy, matplotlib, seaborn)
3. Verify the DGA dataset exists at: activity2-dga-classification/data/dga-24000.csv
4. If the dataset is missing, tell me where to obtain it according to the course materials
5. Load the first 10 rows of the dataset to confirm it's readable
6. Check the dataset has the expected columns: 'Domain' and 'Family'

Start by checking these items and report any issues.
```

---

## Task 1.2: Replace Student ID
**Time:** 5 minutes

### Custom Prompt for Claude Code:
```
Replace [ENTER YOUR STUDENT ID] with my actual student ID: [YOUR_ID_HERE]

Update it in the following file:
- activity2-dga-classification/notebooks/STUDENTID-TASK2.ipynb

Make sure to:
1. Update the comment at the top: # Student ID: [YOUR_ID_HERE]
2. Do NOT change the filename yet (we'll do that at submission time)
3. Show me what you changed
```

---

## Task 1.3: Execute Notebook Sections 1-6 (Data Loading & Model Training)
**Time:** 2-3 hours (includes computation time)

### Custom Prompt for Claude Code:
```
I need to execute Activity 2 notebook sections 1-6 (Data Loading through Model Training with N-gram Features).

Please help me run this systematically:

1. Open: activity2-dga-classification/notebooks/STUDENTID-TASK2.ipynb
2. Starting from Section 1, execute each section sequentially
3. After each section completes, show me a summary of:
   - Key outputs (sample data, shapes, counts)
   - Any warnings or errors
   - Execution time for long-running operations
4. If any section fails, stop and help me debug before continuing
5. For the model training sections (5 & 6), report the accuracy scores as they complete

Pause after Section 6 so I can review the accuracy results before continuing.

Expected outputs:
- Section 1: Dataset shape, class distribution
- Section 2: Visualizations (domain length boxplot)
- Section 3: Statistical features extracted (16 features)
- Section 4: N-gram features extracted (500 features)
- Section 5: 3 model accuracies with statistical features
- Section 6: 3 model accuracies with n-gram features

Start with Section 1.
```

---

## Task 1.4: Execute Section 7-8 (Performance Comparison & Confusion Matrix)
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
Continue executing Activity 2 notebook - Sections 7-8.

Section 7 - Performance Comparison:
- Execute the comparison table generation
- Generate the bar chart comparing both feature approaches
- Report which model/feature combination performed best

Section 8 - Confusion Matrix:
- Execute confusion matrix for the best performing model
- Generate the confusion matrix visualization
- Execute the classification report
- Summarize which malware families are most easily confused (look for off-diagonal values)

Report if we've achieved the >90% accuracy requirement.
```

---

## Task 1.5: Execute Section 9 (SHAP Analysis)
**Time:** 15-30 minutes (SHAP can be slow)

### Custom Prompt for Claude Code:
```
Execute Activity 2 Section 9 - SHAP Explainability Analysis.

Please:
1. Execute the SHAP TreeExplainer code with the Random Forest model
2. Generate the SHAP summary plot
3. Save the plot output
4. Identify the top 5 most important features from the SHAP analysis
5. Explain what these features tell us about DGA domain characteristics

If SHAP is taking too long (>5 minutes), reduce the sample size to 50 and re-run.

Show me the SHAP visualization and feature importance rankings.
```

---

## Task 1.6: Complete Section 10 (Conclusions & Analysis)
**Time:** 2-3 hours (thinking and writing)

### Custom Prompt for Claude Code:
```
Help me complete Activity 2 Section 10 - Conclusions and Recommendations.

Based on the results from Sections 1-9, help me write a comprehensive analysis covering:

1. **Feature Engineering Impact:**
   - Compare statistical features vs n-gram features performance
   - Which approach worked better overall?
   - Why do you think one outperformed the other?
   - Give specific accuracy comparisons

2. **Model Performance:**
   - Which classifier performed best?
   - Did we achieve >90% accuracy? (required for full marks)
   - How did the three classifiers compare?
   - Why might one classifier be better suited than others?

3. **Misclassification Analysis:**
   - Based on the confusion matrix, which malware families are most confused?
   - What domain characteristics might make them similar?
   - Are there any families with particularly low accuracy?

4. **Key Insights from SHAP:**
   - What are the top 5 most important features?
   - What do these features reveal about DGA domains?
   - How do DGA domains differ from legitimate domains?

5. **Recommendations for Improvement:**
   - What additional features could improve accuracy?
   - Would ensemble methods help?
   - What about real-time deployment considerations?

Write this in first-person academic style (e.g., "I found that...", "The analysis reveals...").
Use the actual numbers and results from our experiments.
Be specific and reference concrete findings.
Aim for 400-600 words total.

Insert this analysis directly into the notebook's Section 10 markdown/print statements.
```

---

## Task 1.7: Final Review & Save Activity 2
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
Perform a final review of Activity 2 notebook before marking it complete:

Checklist:
1. ✓ All cells have been executed (check for cell execution numbers)
2. ✓ All outputs are visible (no blank output cells)
3. ✓ All visualizations rendered correctly (8+ plots total)
4. ✓ Student ID is updated in the header
5. ✓ Section 10 conclusions are complete (not placeholder text)
6. ✓ Confusion matrix shows actual results
7. ✓ SHAP plot is generated and visible
8. ✓ Accuracy requirements met (>90%)
9. ✓ No error messages in any cell outputs
10. ✓ Notebook saved with all outputs

Go through the notebook and verify each item. Report any issues found.

If everything looks good, save the notebook and confirm Activity 2 is submission-ready.
```

---

# 🎯 PHASE 2: DATA ANALYSIS (Activity 1 - Priority 2)
**Estimated Time:** 10-15 hours
**Grade Impact:** 20% of total portfolio
**Challenge:** Question 10 requires original analysis and critical thinking

## Task 2.1: Environment & Data Setup
**Time:** 15 minutes

### Custom Prompt for Claude Code:
```
Set up Activity 1 (Web Server Log Analysis):

1. Check if data file exists: activity1-log-analysis/data/p2-pitta_25sept.txt
2. If missing, remind me I need to obtain this from Blackboard (it's personalized to my UWE username)
3. Update student ID in: activity1-log-analysis/notebooks/STUDENTID-TASK1.ipynb
   Replace with: [YOUR_ID_HERE]
4. Verify the notebook can find the data file path correctly
5. Test load the first 100 rows to verify the parsing works

Report any issues with data file location or parsing.
```

---

## Task 2.2: Execute Questions 1-8 (Guided Analysis)
**Time:** 1-2 hours

### Custom Prompt for Claude Code:
```
Execute Activity 1 notebook Questions 1-8 sequentially.

For each question, execute the code and report:
- The key finding (e.g., "Q1: Found 2,847 unique IP addresses")
- Any visualizations generated
- Any errors or warnings

Questions overview:
- Q1: IP frequency (1 mark)
- Q2: URL frequency (1 mark)
- Q3: IP-URL pairs (1 mark)
- Q4: Filter cs-uri-query (1 mark)
- Q5: Filter User-Agent (1 mark)
- Q6: Filter 404s before 7am (1 mark)
- Q7: Bar chart of status codes (1 mark)
- Q8: Line chart by date (1 mark)

Execute them all and summarize the key findings from each.
Pause after Q8 before moving to Q9 (NetworkX graph).
```

---

## Task 2.3: Execute Question 9 (NetworkX Graph)
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
Execute Activity 1 Question 9 - Network Graph visualization.

This question is worth 4 marks (highest except Q10).

Please:
1. Execute the NetworkX graph generation code
2. Verify the graph shows:
   - 1 web server node (red, large)
   - 20 client IP nodes (blue, sized by activity)
   - Edges connecting clients to server
3. Ensure the visualization renders correctly
4. The node sizing should be proportional to request volume

Show me the graph and confirm it looks correct.
Report the top 5 most active IPs by node size.
```

---

## Task 2.4: Question 10 - Suspicious Activity Analysis (CRITICAL)
**Time:** 5-8 hours (most important question)

### 🎯 MULTI-STAGE ANALYSIS PROMPTS

#### Stage 1: Data Exploration
**Time:** 30 minutes

```
Help me start Question 10 - Suspicious Activity Investigation (8 marks - highest value).

First, let's explore the data comprehensively:

1. Execute Analysis 1 (High-Volume IPs):
   - Show me the top 20 IPs by request count
   - Calculate mean, median, std dev of requests per IP
   - Identify statistical outliers (mean + 3*std)
   - Report which IPs are anomalous and by how much

2. Execute Analysis 2 (Error Rates):
   - Calculate error rate (4xx, 5xx) for top 100 IPs
   - Show me the top 15 IPs by error rate
   - Which IPs have error rates >30%? >50%?

3. Execute Analysis 3 (Temporal Patterns):
   - Show hourly activity distribution
   - Which IPs are most active between midnight-6am?
   - Are there any IPs ONLY active during off-hours?

4. Execute Analysis 4 (Scanning Behavior):
   - Which IPs have >20 404 errors?
   - Which IPs have >50 404 errors?
   - Show me the URLs they were trying to access

Provide specific numbers and IP addresses for each finding.
```

#### Stage 2: Deep Dive on Suspicious IPs
**Time:** 2 hours

```
Now let's do a deep dive on the suspicious IPs identified in Stage 1.

For each suspicious IP (you should have identified 3-10), analyze:

1. **Request Volume Analysis:**
   - Total requests
   - Requests per hour distribution
   - Compare to normal user behavior (mean requests)
   - Percentage of total traffic

2. **Error Pattern Analysis:**
   - Count by status code (200, 301, 400, 403, 404, 500, etc.)
   - Error rate percentage
   - Most common errors
   - Are errors random or targeted?

3. **Temporal Behavior:**
   - Most active hours
   - Request rate (requests per minute during active periods)
   - Sustained activity or bursts?
   - Working hours vs off-hours ratio

4. **Target Analysis:**
   - Top 10 URLs/paths accessed
   - Unique URLs attempted
   - Are they accessing normal paths or probing?
   - Any admin/sensitive paths (/admin, /login, /config, etc.)?

5. **User-Agent Analysis:**
   - What User-Agent string(s)?
   - Is it a normal browser or tool/script?
   - Does User-Agent change or stay consistent?

For EACH suspicious IP, create a profile with these details.
Present findings in a structured format.
```

#### Stage 3: Attack Classification
**Time:** 1 hour

```
Based on the suspicious IP profiles from Stage 2, help me classify the attack types:

For each suspicious IP, determine the attack type:

**Common Attack Patterns:**
1. **Web Scraping/Crawling:** High volume, low error rate, consistent User-Agent
2. **Vulnerability Scanning:** High error rate (404s), accessing unusual paths, automated tool User-Agent
3. **Brute Force:** Repeated attempts on login/auth endpoints, high 401/403 errors
4. **Directory Traversal:** Many 404s, trying common file/directory names
5. **SQL Injection Probing:** Special characters in query strings, database error codes
6. **DDoS/Flooding:** Extremely high volume, short time window, often same resource
7. **Reconnaissance:** Systematic probing, mapping site structure, moderate volume

For each suspicious IP, provide:
- Primary attack type (most likely)
- Secondary indicators (supporting evidence)
- Confidence level (High/Medium/Low)
- Specific evidence (quote examples from logs)

Format as a threat assessment table.
```

#### Stage 4: Evidence Documentation
**Time:** 1 hour

```
Help me document concrete evidence for each suspicious IP identified.

For the investigation report, I need specific examples. For each suspicious IP:

1. **Quote 3-5 specific log entries** that demonstrate malicious behavior:
   - Show timestamp, status code, URL accessed, and any relevant fields
   - Highlight what makes each entry suspicious

2. **Create a timeline** of the attack:
   - Start time (first request)
   - Peak activity time
   - End time (last request)
   - Duration of attack
   - Request rate during attack

3. **Calculate impact metrics:**
   - Total requests from this IP
   - Percentage of total server traffic
   - Bandwidth consumed (if available)
   - Server resources affected

4. **Identify patterns:**
   - Sequential vs random URL access
   - Timing patterns (regular intervals?)
   - Progression (reconnaissance → exploitation?)

Present this as formal evidence for the investigation report.
Use actual data from the logs with specific examples.
```

#### Stage 5: Write Investigation Report
**Time:** 2-3 hours

```
Help me write the final Question 10 investigation report based on Stages 1-4 findings.

The report should follow this structure:

**INVESTIGATION METHODOLOGY** (150-200 words)
- Explain the analytical approach used
- What types of suspicious activity were you looking for?
- What metrics and thresholds did you use?
- Why are these indicators relevant for detecting attacks?

**SUSPICIOUS IP ADDRESSES IDENTIFIED** (Main Section)

For EACH suspicious IP (minimum 3, aim for 5-8):

**IP Address: X.X.X.X**
- **Attack Type:** [Classification from Stage 3]
- **Severity:** [Critical/High/Medium/Low]
- **Evidence Summary:**
  - Total Requests: [number] ([X]% of total traffic)
  - Error Rate: [X]% ([number] errors out of [number] requests)
  - Active Period: [date/time range]
  - Request Rate: [X] requests per minute at peak

- **Behavioral Indicators:**
  - [List 3-5 specific suspicious behaviors]
  - [e.g., "Accessed 127 non-existent URLs in 15 minutes"]
  - [e.g., "100% of requests resulted in 404 errors"]

- **Sample Log Evidence:**
  - [Quote 2-3 specific log lines]
  - [Explain why each is suspicious]

- **Assessment:**
  - [2-3 sentences explaining why this IP is malicious]
  - [What was the attacker trying to achieve?]

**CROSS-IP ANALYSIS** (100-150 words)
- Were any attacks coordinated?
- Common patterns across multiple suspicious IPs?
- Timeline correlation?

**RECOMMENDATIONS** (150-200 words)
- Immediate actions (IP blocking, rate limiting)
- Detection improvements (rules, alerts, monitoring)
- Prevention measures (input validation, security hardening)
- Incident response (log retention, forensics)

**CONCLUSION** (100 words)
- Summary of findings
- Overall threat assessment
- Key takeaways

**GRADING CRITERIA ALIGNMENT:**
This addresses:
- ✓ Identifying all suspicious activity (3 marks) - Multiple IPs with evidence
- ✓ Analytical reasoning (3 marks) - Deep analysis and classification
- ✓ Clarity and presentation (2 marks) - Well-structured report

Write this in first-person, professional security analyst tone.
Use specific numbers and evidence from our actual analysis.
Replace the placeholder text in the notebook with this complete investigation.
```

---

## Task 2.5: Final Review & Save Activity 1
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
Perform final review of Activity 1 notebook:

Checklist:
1. ✓ All cells executed (Q1-Q10)
2. ✓ All outputs visible
3. ✓ Student ID updated
4. ✓ Q7 bar chart rendered
5. ✓ Q8 line chart rendered
6. ✓ Q9 NetworkX graph rendered
7. ✓ Q10 investigation complete (not placeholder text)
8. ✓ Q10 identifies specific suspicious IPs with reasoning
9. ✓ Q10 analysis is detailed and demonstrates analytical reasoning
10. ✓ No error messages

Verify each item and report issues.
If complete, save the notebook and confirm Activity 1 is submission-ready.
```

---

# 🛡️ PHASE 3: SIEM ATTACK SIMULATION (Activity 3 - Priority 3)
**Estimated Time:** 45-60 hours
**Grade Impact:** 45% of total portfolio (HIGHEST)
**Complexity:** Requires infrastructure setup, practical attacks, and formal report

## Task 3.1: Choose Infrastructure Approach
**Time:** 1-2 hours (research and decision)

### Custom Prompt for Claude Code:
```
Help me choose the best infrastructure approach for Activity 3 (SIEM Attack Simulation).

Compare the three options:

**Option 1: GoibhniUWE (Recommended for beginners)**
- Pre-configured VM from Blackboard
- Quick setup
- Known to work with course requirements
- Pros/cons for my situation?

**Option 2: DetectionLab (Advanced)**
- Full enterprise SIEM environment
- Splunk, Windows AD, attack simulation
- Requires: 16GB RAM, 100GB disk, Vagrant, VirtualBox
- Pros/cons for my situation?

**Option 3: Custom Setup**
- Full control over configuration
- Choose own SIEM (Splunk/Wazuh/ELK)
- Most documentation required
- Pros/cons for my situation?

Based on:
- My technical skill level: [beginner/intermediate/advanced]
- Available hardware: [RAM, disk space, processor]
- Time remaining until deadline
- Desired grade target: [50-60% / 60-70% / 70%+]

Recommend which option I should use and why.
Provide a step-by-step setup guide for the recommended option.
```

---

## Task 3.2: Infrastructure Setup & Documentation
**Time:** 4-8 hours (varies by option chosen)

### Custom Prompt for Claude Code:
```
Help me set up and document my SIEM infrastructure for Activity 3.

I've chosen: [GoibhniUWE / DetectionLab / Custom]

Please help me:

1. **Setup Guidance:**
   - Provide step-by-step instructions for setting up this environment
   - What VMs do I need running?
   - Network configuration requirements
   - SIEM platform access (URL, credentials)
   - Logging configuration

2. **Documentation Template:**
   Create entries in: activity3-siem-attacks/documentation/attack_notes.md

   Document:
   - Environment chosen and why
   - VM inventory (name, OS, IP, role)
   - Network topology (IP ranges, connectivity)
   - SIEM platform details (version, access method)
   - Log sources configured
   - Any issues encountered and how resolved

3. **Screenshot Checklist:**
   Tell me which screenshots to capture for infrastructure documentation:
   - Network topology
   - VM configurations
   - SIEM dashboard
   - Log source connections
   - [Suggest 5-7 specific screenshots]

4. **Verification:**
   How do I verify the setup is working correctly?
   - Test log collection
   - Verify SIEM is receiving data
   - Check search functionality

Guide me through this process step by step.
Stop at key points for me to complete actions and report back.
```

---

## Task 3.3: Attack Planning & Selection
**Time:** 2-3 hours

### Custom Prompt for Claude Code:
```
Help me plan which attacks to execute for Activity 3.

Requirements:
- Need at least 2-3 different attack types for a good grade
- Attacks must be detectable via SIEM
- Must be able to document with screenshots
- Should demonstrate understanding of attack techniques and detection

Suggest 3-5 attacks appropriate for my environment: [GoibhniUWE/DetectionLab/Custom]

For each suggested attack, provide:

1. **Attack Name & Type**
2. **Difficulty:** [Easy/Medium/Hard]
3. **Time to Execute:** [Estimate]
4. **Tools Required:** [Available in Kali/Attacker VM?]
5. **Target Requirements:** [What needs to be on target?]
6. **Expected Detection Evidence:**
   - What logs should be generated?
   - What SIEM alerts should trigger?
   - What queries will find the activity?
7. **MITRE ATT&CK Mapping:** [Technique ID and name]
8. **Grading Value:** [Why this attack demonstrates competency]

Based on my setup and time available, recommend:
- 3 attacks for 60-70% grade target
- 5 attacks for 70%+ grade target

Prioritize attacks that:
- Are reliably detectable
- Have clear log evidence
- Demonstrate different attack vectors
- Are achievable with available tools
```

---

## Task 3.4: Attack Execution Framework
**Time:** 15-25 hours (for 3-5 attacks)

### 🎯 ATTACK EXECUTION TEMPLATE (Use for EACH attack)

#### Attack Execution - Part A: Preparation
**Time per attack:** 30 minutes

```
Prepare for executing Attack [N]: [Attack Name]

Attack Type: [Brute Force / Port Scan / SQL Injection / etc.]
Target: [IP address and service]
Tools: [Nmap / Hydra / Metasploit / etc.]

Help me prepare:

1. **Pre-Attack Checklist:**
   - Verify target VM is running and accessible
   - Verify SIEM is collecting logs from target
   - Verify attack tools are installed on attacker VM
   - Test basic connectivity (ping, etc.)

2. **Attack Plan Documentation:**
   Create a plan in: activity3-siem-attacks/documentation/attack_notes.md

   Include:
   - Date/Time I'm starting
   - Objective of this attack
   - Expected indicators in SIEM
   - Step-by-step commands I'll execute
   - Expected outcomes

3. **Screenshot Preparation:**
   Tell me which screenshots to capture:
   - Before: Baseline state
   - During: Attack execution
   - After: Attack results
   - [List 3-5 specific screenshots]

4. **SIEM Baseline:**
   What query should I run in SIEM to see the "before" state?
   This will help contrast with "after" attack detection.

Provide the attack execution plan and confirm I'm ready to proceed.
```

#### Attack Execution - Part B: Execute Attack
**Time per attack:** 1-3 hours

```
Guide me through executing Attack [N]: [Attack Name]

Provide step-by-step instructions:

**Step 1: [Action]**
- Command to run: [exact command]
- Expected output: [what should happen]
- Screenshot to capture: [what to capture]
- How to verify success: [validation]

**Step 2: [Action]**
[Repeat pattern]

[Continue for all steps of the attack]

**Important:**
- Pause after each step for me to execute and report results
- If something doesn't work, help me troubleshoot
- Remind me to capture screenshots at key moments
- Document any errors or unexpected behavior

After each step, I'll report back:
"Step [N] complete. Output: [paste output]"

Then you provide the next step.

Start with Step 1.
```

#### Attack Execution - Part C: Detection Analysis
**Time per attack:** 2-4 hours

```
Analyze SIEM detection for Attack [N]: [Attack Name]

Now that the attack is complete, help me analyze the detection:

1. **SIEM Query Development:**
   - What query should I run to find evidence of this attack?
   - Provide specific SIEM query syntax for [Splunk/Wazuh/ELK]
   - What time window should I search?
   - What log sources should I check?

2. **Log Analysis:**
   Guide me to find:
   - Initial attack indicators (first log entry)
   - Peak attack activity (most intense moment)
   - Attack completion (final log entry)
   - Any anomalous patterns

3. **Evidence Collection:**
   What specific log entries should I screenshot?
   - Alert triggers (if any)
   - Key log entries showing attack
   - Timeline view
   - Query results
   - [5-10 specific screenshots]

4. **Detection Effectiveness Assessment:**
   Help me evaluate:
   - Was the attack detected? (Yes/No)
   - How long after attack start was it detected?
   - Were there any false positives/negatives?
   - What wasn't captured that should have been?
   - Could detection be improved? How?

5. **Documentation:**
   Update attack_notes.md with:
   - SIEM queries used
   - Key log entries (quote 3-5 examples)
   - Detection timeline
   - Analysis of effectiveness
   - Screenshot inventory

Walk me through this analysis process for this specific attack.
Provide actual SIEM query examples I can use.
```

#### Attack Execution - Part D: Post-Attack Documentation
**Time per attack:** 1 hour

```
Complete documentation for Attack [N]: [Attack Name]

Help me finalize documentation in attack_notes.md:

1. **Attack Summary Section:**
   - Date/Time executed
   - Duration of attack
   - Success level (Complete/Partial/Failed)
   - Challenges encountered
   - Target impact observed

2. **Technical Details:**
   - Exact commands used (copy from terminal)
   - Tool configurations
   - Network traffic generated
   - Files created/modified

3. **Detection Summary:**
   - SIEM query that found the attack
   - Number of log events generated
   - Alert rules triggered
   - Detection timeline

4. **Lessons Learned:**
   - What worked well
   - What was difficult
   - Unexpected findings
   - How to improve detection
   - Real-world relevance

5. **Screenshot Organization:**
   - Rename and organize screenshots with descriptive names
   - Create a mapping: screenshot filename → what it shows
   - Verify all screenshots are clear and relevant

6. **MITRE ATT&CK Mapping:**
   - Map this attack to MITRE ATT&CK framework
   - Technique ID and name
   - Tactic category
   - Link to https://attack.mitre.org/techniques/[ID]/

Review the documentation and ensure it's complete for report writing later.
```

---

## Task 3.5: Report Writing (1500 words max)
**Time:** 10-15 hours (most critical)

### 🎯 REPORT WRITING PROMPTS (SEQUENTIAL)

#### Part A: Report Structure & Outline
**Time:** 1 hour

```
Help me create a detailed outline for Activity 3 report (max 1500 words).

The report must cover:
- Infrastructure setup and configuration
- Attack execution methodology
- SIEM detection and analysis
- Evaluation and recommendations

Create a structured outline with:

1. **Section Titles**
2. **Word Count Allocation** (total 1500)
3. **Key Points to Cover** in each section
4. **Figures/Screenshots to Reference** in each section

Suggested structure:
- Introduction (100 words)
- Infrastructure Setup (250 words)
- Attack Methodology (300 words)
- Attack 1: [Name] (150 words)
- Attack 2: [Name] (150 words)
- Attack 3: [Name] (150 words)
- Detection Analysis (300 words)
- Evaluation & Recommendations (250 words)
- Conclusion (100 words)
- References (not counted)

Adjust based on number of attacks I performed: [2/3/4/5]

Provide the complete outline with:
- What each section should contain
- Which screenshots to reference
- Key technical details to include
- Word count targets
```

#### Part B: Write Infrastructure Section
**Time:** 2 hours

```
Help me write the Infrastructure Setup section of Activity 3 report.

Based on my documentation in attack_notes.md, write a professional academic section covering:

**Infrastructure Setup (Target: 250 words)**

Should include:
1. **Environment Overview** (50 words)
   - What platform chosen (GoibhniUWE/DetectionLab/Custom) and why
   - Overall architecture

2. **Component Details** (100 words)
   - VMs deployed (OS, roles, IPs)
   - Network configuration
   - SIEM platform (version, capabilities)

3. **Configuration** (70 words)
   - Log sources configured
   - Alert rules setup
   - Any custom configurations

4. **Challenges & Solutions** (30 words)
   - Key setup issues encountered
   - How they were resolved

**Requirements:**
- Academic, professional tone (third person or first person as appropriate)
- Reference Figure 1 (network diagram), Figure 2 (SIEM dashboard)
- Technical accuracy
- Concise - every word counts toward 1500 limit
- Include specific details (versions, IPs, configurations)

Pull information from my attack_notes.md documentation.
Write the complete section with proper paragraph structure.
Indicate where to insert figure references: [INSERT FIGURE X: Description]
```

#### Part C: Write Attack Methodology Section
**Time:** 2 hours

```
Write the Attack Methodology section of Activity 3 report.

**Attack Methodology (Target: 300 words)**

This section should explain the overall approach BEFORE describing individual attacks.

Cover:

1. **Attack Selection Rationale** (80 words)
   - Why these specific attacks were chosen
   - What they demonstrate
   - Relevance to real-world threats
   - Coverage of different attack vectors

2. **Testing Approach** (120 words)
   - Systematic methodology used
   - How attacks were documented
   - Screenshot strategy
   - Ethical considerations (controlled environment)

3. **Detection Strategy** (100 words)
   - How SIEM was prepared for detection
   - Baseline establishment
   - Query development approach
   - Alert configuration

**Requirements:**
- Demonstrates understanding of attack lifecycle
- Shows professional methodology
- References MITRE ATT&CK framework
- Academic tone
- Sets up individual attack descriptions

Write this section to flow naturally before the individual attack descriptions.
```

#### Part D: Write Individual Attack Sections
**Time:** 3-4 hours (30-60 min per attack)

```
Write the section for Attack [N]: [Attack Name] for Activity 3 report.

For this attack, I executed: [brief description]

**Attack [N]: [Name] (Target: 150 words per attack)**

Structure each attack description:

1. **Attack Overview** (30 words)
   - Attack type and objective
   - Tools used
   - Target system/service
   - MITRE ATT&CK technique reference

2. **Execution** (50 words)
   - Key steps taken (high-level, not every command)
   - Critical actions performed
   - Attack outcome
   - Reference figures (attack execution screenshot)

3. **Detection** (50 words)
   - How SIEM detected the attack
   - SIEM query used (brief mention or in appendix)
   - Log sources that captured activity
   - Alert triggered (if any)
   - Reference figures (SIEM detection screenshots)

4. **Analysis** (20 words)
   - Detection effectiveness
   - Key observations
   - What this demonstrates

**Requirements:**
- Pull details from attack_notes.md for this specific attack
- Be concise - only most important details
- Reference specific figures: [Figure X: Attack execution], [Figure Y: SIEM detection]
- Technical but accessible writing
- Focus on what was learned

Write the complete attack section.

[REPEAT THIS PROMPT FOR EACH ATTACK PERFORMED]
```

#### Part E: Write Detection Analysis Section
**Time:** 2 hours

```
Write the Detection Analysis section of Activity 3 report.

**Detection Analysis (Target: 300 words)**

This section analyzes SIEM effectiveness across ALL attacks performed.

Cover:

1. **Overall Detection Effectiveness** (100 words)
   - Summary of detection success for each attack
   - Which attacks were detected quickly/slowly/missed
   - Overall detection rate
   - Log source effectiveness comparison

2. **Detection Patterns** (100 words)
   - Common indicators across attacks
   - Most useful log sources
   - SIEM query patterns that worked well
   - Alert accuracy (true positives vs false positives)

3. **Detection Gaps** (50 words)
   - What wasn't detected that should have been
   - Blind spots in logging/monitoring
   - Evasion possibilities noticed

4. **Correlation Insights** (50 words)
   - How multiple log sources together provided full picture
   - Value of cross-source correlation
   - Timeline reconstruction capabilities

**Requirements:**
- Comparative analysis across all attacks
- Demonstrates critical thinking about detection
- Specific examples from actual findings
- Reference relevant figures (SIEM dashboards, queries)
- Shows understanding of SIEM capabilities and limitations

Use actual data from my attacks and detection results.
Write with analytical depth - this shows security analyst thinking.
```

#### Part F: Write Evaluation & Recommendations Section
**Time:** 1-2 hours

```
Write the Evaluation & Recommendations section of Activity 3 report.

**Evaluation & Recommendations (Target: 250 words)**

This is where you demonstrate professional security analyst thinking.

Cover:

1. **Infrastructure Evaluation** (60 words)
   - Strengths of the setup used
   - Limitations encountered
   - Scalability considerations
   - Real-world applicability

2. **Detection Improvements** (80 words)
   - Specific recommendations for better detection
   - Additional log sources needed
   - Alert rule enhancements
   - Query optimization suggestions
   - Integration opportunities

3. **Security Hardening** (60 words)
   - How to prevent the attacks demonstrated
   - Configuration changes recommended
   - Security controls to implement
   - Defense-in-depth strategies

4. **Lessons for Practice** (50 words)
   - Key takeaways for real SOC operations
   - Importance of logging strategy
   - Balance between detection and noise
   - Continuous improvement approach

**Requirements:**
- Practical, actionable recommendations
- Based on actual experience from the exercise
- Shows understanding of broader security context
- Professional security analyst perspective
- Forward-thinking

This section demonstrates you didn't just do the exercise - you learned from it.
Write thoughtfully and specifically based on what you actually experienced.
```

#### Part G: Write Introduction & Conclusion
**Time:** 1 hour

```
Write the Introduction and Conclusion sections for Activity 3 report.

**Introduction (Target: 100 words)**

Should include:
- Purpose of the exercise (simulate attacks + detect with SIEM)
- Environment used (briefly)
- Attacks performed (list)
- Structure of this report
- Learning objectives

Make it engaging but professional.
Set expectations for what reader will learn.

---

**Conclusion (Target: 100 words)**

Should include:
- Summary of what was accomplished
- Key findings (2-3 most important)
- Overall success of detection strategy
- Broader implications for security operations
- Final thought on importance of SIEM in defense

Make it impactful and memorable.
Tie back to introduction.
Leave reader with key takeaway.

---

Write both sections.
These should frame the entire report professionally.
```

#### Part H: References & Final Formatting
**Time:** 1 hour

```
Help me complete references and final formatting for Activity 3 report.

**References:**

Based on what I cited in my report, help me create proper UWE Harvard references for:

1. **Tools Used:**
   - Nmap / Hydra / Metasploit / [other tools]
   - Official tool documentation

2. **SIEM Platform:**
   - Splunk / Wazuh / ELK documentation
   - Version-specific references

3. **MITRE ATT&CK:**
   - Framework reference
   - Specific techniques cited

4. **Any Academic Sources:**
   - CVE references if applicable
   - Security papers referenced

Format each reference in UWE Harvard style.

---

**Formatting Checklist:**

1. **Document Structure:**
   - Title page with student ID
   - Section headings clear and consistent
   - Page numbers
   - Professional layout

2. **Figures:**
   - All screenshots numbered (Figure 1, Figure 2, etc.)
   - Each figure has descriptive caption
   - All figures referenced in text
   - High quality and readable
   - Organized logically

3. **Technical Elements:**
   - Code/commands in monospace font
   - IP addresses, filenames formatted consistently
   - Tables formatted clearly
   - Technical terms used correctly

4. **Quality Checks:**
   - Word count: [actual count] / 1500 (should be 1400-1500)
   - Spell check complete
   - Grammar check complete
   - No placeholder text remaining
   - Student ID present and correct

5. **PDF Export:**
   - Export to PDF format
   - Rename to: [STUDENTID]-TASK3.pdf
   - Verify all figures visible in PDF
   - Verify all text renders correctly

Guide me through final checks and PDF creation.
```

---

## Task 3.6: Final Review & Submission Prep
**Time:** 2 hours

### Custom Prompt for Claude Code:
```
Perform comprehensive final review of Activity 3 before submission.

**Review Checklist:**

1. **Documentation Files:**
   - [ ] attack_notes.md complete and detailed
   - [ ] setup_guide.md has infrastructure details
   - [ ] All screenshots organized and named clearly

2. **Report Content:**
   - [ ] Word count: 1400-1500 words (not including references)
   - [ ] All sections complete (no placeholders)
   - [ ] Student ID present and correct
   - [ ] 15-25 screenshots included
   - [ ] All figures referenced in text
   - [ ] All figures have captions
   - [ ] References in UWE Harvard format
   - [ ] Professional academic tone throughout

3. **Technical Accuracy:**
   - [ ] All IP addresses correct
   - [ ] All commands accurate
   - [ ] All SIEM queries validated
   - [ ] MITRE ATT&CK references correct
   - [ ] No security concerns in sharing (no real credentials/IPs)

4. **Visual Quality:**
   - [ ] All screenshots clear and readable
   - [ ] No sensitive information visible
   - [ ] Screenshots show relevant information
   - [ ] Consistent screenshot quality

5. **PDF Quality:**
   - [ ] Filename: [STUDENTID]-TASK3.pdf
   - [ ] All images render correctly
   - [ ] No formatting issues
   - [ ] File size reasonable (<25MB for Blackboard)

Go through each item systematically.
Report any issues found.
When complete, confirm Activity 3 is submission-ready.
```

---

# 📦 PHASE 4: FINAL SUBMISSION PREPARATION
**Estimated Time:** 2-3 hours
**Critical:** Do not skip this phase!

## Task 4.1: Rename Submission Files
**Time:** 15 minutes

### Custom Prompt for Claude Code:
```
Prepare final submission filenames for all three activities.

My Student ID is: [YOUR_STUDENT_ID_HERE]

Please:

1. **Rename files to submission format:**

   Current → Submission Name:
   - activity1-log-analysis/notebooks/STUDENTID-TASK1.ipynb
     → activity1-log-analysis/notebooks/[STUDENTID]-TASK1.ipynb

   - activity2-dga-classification/notebooks/STUDENTID-TASK2.ipynb
     → activity2-dga-classification/notebooks/[STUDENTID]-TASK2.ipynb

   - activity3-siem-attacks/documentation/STUDENTID-TASK3.pdf
     → activity3-siem-attacks/documentation/[STUDENTID]-TASK3.pdf

2. **Verify files:**
   - Check each file exists
   - Verify each file has content (not empty)
   - Confirm each filename matches exactly

3. **Create submission copies** in a dedicated folder:
   - Create: submission/
   - Copy all three files there
   - This is what I'll upload to Blackboard

Execute the renames and confirm files are ready for submission.
```

---

## Task 4.2: Pre-Submission Validation
**Time:** 1-2 hours

### Custom Prompt for Claude Code:
```
Perform comprehensive pre-submission validation of ALL THREE activities.

Go through this detailed checklist:

**ACTIVITY 1 VALIDATION:**
1. [ ] File named correctly: [STUDENTID]-TASK1.ipynb
2. [ ] Student ID updated in notebook header (not placeholder)
3. [ ] All cells executed (verify execution numbers sequential)
4. [ ] All outputs visible (no blank output cells)
5. [ ] Q1-Q8 show actual results
6. [ ] Q9 NetworkX graph rendered and visible
7. [ ] Q10 investigation complete with specific IPs and analysis
8. [ ] No error messages in any outputs
9. [ ] File size reasonable (<50MB)
10. [ ] Can open and view the notebook successfully

**ACTIVITY 2 VALIDATION:**
1. [ ] File named correctly: [STUDENTID]-TASK2.ipynb
2. [ ] Student ID updated in notebook header (not placeholder)
3. [ ] All cells executed (verify execution numbers)
4. [ ] All outputs visible
5. [ ] All visualizations rendered (8+ plots)
6. [ ] Section 1-6: All model training complete with accuracy scores
7. [ ] Section 7: Performance comparison chart visible
8. [ ] Section 8: Confusion matrix generated and visible
9. [ ] Section 9: SHAP plot generated and visible
10. [ ] Section 10: Conclusions complete (not placeholder text)
11. [ ] Accuracy >90% achieved (required)
12. [ ] No error messages
13. [ ] File size reasonable (<50MB)

**ACTIVITY 3 VALIDATION:**
1. [ ] File named correctly: [STUDENTID]-TASK3.pdf
2. [ ] Student ID present in report
3. [ ] PDF opens correctly
4. [ ] Word count 1400-1500 (not counting references)
5. [ ] All sections complete
6. [ ] 15-25 screenshots included
7. [ ] All screenshots visible and clear
8. [ ] All figures numbered and captioned
9. [ ] All figures referenced in text
10. [ ] References included (UWE Harvard format)
11. [ ] No placeholder text
12. [ ] Professional formatting
13. [ ] File size <25MB

**OVERALL VALIDATION:**
1. [ ] All three files ready
2. [ ] All files in submission/ folder
3. [ ] Academic integrity: GenAI acknowledged if used
4. [ ] No sensitive data included (real passwords, external IPs)
5. [ ] Ready to upload to Blackboard

For each item, report:
- ✓ PASS
- ✗ FAIL with explanation
- ⚠ WARNING with concern

Report all issues found so I can fix them before submission.
```

---

## Task 4.3: Create Submission Package
**Time:** 30 minutes

### Custom Prompt for Claude Code:
```
Create the final submission package for Blackboard upload.

Help me:

1. **Verify Submission Folder:**
   - Confirm submission/ folder contains all three files:
     - [STUDENTID]-TASK1.ipynb
     - [STUDENTID]-TASK2.ipynb
     - [STUDENTID]-TASK3.pdf

2. **File Size Check:**
   - Report file size of each submission file
   - Confirm all are under Blackboard limits
   - If any are too large, suggest compression

3. **Create Backup:**
   - Create submission_backup/ folder
   - Copy all three files there
   - Zip the backup folder
   - This is my safety copy

4. **Pre-Upload Checklist:**
   Print a final checklist I can review:
   - [ ] Student ID correct in all files
   - [ ] All files named correctly
   - [ ] All files open successfully
   - [ ] All content complete
   - [ ] All outputs/figures visible
   - [ ] Backup created
   - [ ] Deadline: Thursday, 11th December 2025 at 14:00

5. **Upload Instructions:**
   Provide step-by-step:
   - Where to upload (Blackboard assignment link)
   - Upload order (if matters)
   - What confirmation to expect
   - What to do after upload (verify submission)

Confirm everything is ready for submission.
```

---

## Task 4.4: Post-Submission Verification
**Time:** 15 minutes

### Custom Prompt for Claude Code:
```
After I've uploaded to Blackboard, help me verify successful submission.

Guide me to check:

1. **Submission Confirmation:**
   - Did Blackboard show submission confirmation?
   - Can I see submission timestamp?
   - Are all three files listed?

2. **Download Test:**
   - Download what I just uploaded
   - Open each file
   - Verify they're the correct versions
   - Confirm everything displays properly

3. **Submission Record:**
   Create a record of submission:
   - Date/time submitted: [record]
   - Files submitted: [list all three]
   - File sizes: [list]
   - Confirmation number: [if available]

   Save this in: SUBMISSION_RECORD.md

4. **Backup Verification:**
   - Confirm backup zip exists
   - Test extract backup zip
   - Verify backup files match submission

If any issues found during verification, guide me on remediation before deadline.

Confirm: "All three activities successfully submitted and verified!"
```

---

# 🎓 BONUS: EXCELLENCE ENHANCEMENTS
**Optional - For 70%+ Grade Target**

## Enhancement 1: Advanced Question 10 Analysis (Activity 1)

```
Enhance my Activity 1 Question 10 analysis to excellence level.

Add these advanced elements:

1. **Attack Timeline Visualization:**
   Create a matplotlib timeline showing:
   - When each suspicious IP was active
   - Intensity of activity over time
   - Overlapping attack periods

2. **Attack Correlation Analysis:**
   - Are suspicious IPs coordinated?
   - Do they target the same resources?
   - Sequential or simultaneous?
   - Could this be a distributed attack?

3. **Risk Scoring:**
   Create a risk score (1-10) for each suspicious IP based on:
   - Volume of requests
   - Error rate
   - Timing patterns
   - Target sensitivity
   - User-Agent characteristics

   Present as a ranked threat table.

4. **Network Forensics:**
   - Geolocation analysis (if possible from IPs)
   - ASN/ISP identification
   - Known malicious IP check (conceptual)

5. **Incident Response Recommendations:**
   For each suspicious IP, recommend:
   - Immediate action (block/monitor/investigate)
   - Evidence preservation steps
   - Notification requirements
   - Follow-up investigation needs

This elevates from "found suspicious IPs" to "comprehensive security incident analysis."

Add these elements to my existing Q10 analysis.
```

---

## Enhancement 2: Advanced Feature Engineering (Activity 2)

```
Enhance Activity 2 with additional advanced features.

Add a third feature engineering approach:

**Approach 3: Combined Features (Hybrid)**

1. **Create hybrid feature set:**
   - Combine best statistical features from Approach 1
   - Add character n-gram features from Approach 2
   - Add new advanced features:
     - Pronounceability score (already in feature_engineering.py)
     - Edit distance from known good domains
     - Longest common substring patterns
     - Dictionary word detection
     - TLD-specific features

2. **Train models on hybrid features:**
   - Same 3 classifiers
   - Compare against Approach 1 and 2
   - Demonstrate improvement

3. **Feature Importance Deep Dive:**
   - Use SHAP for feature importance
   - Compare important features across all 3 approaches
   - Create feature importance comparison visualization
   - Explain why certain features matter

4. **Error Analysis:**
   - Identify which specific domains are misclassified
   - Analyze characteristics of misclassified domains
   - Suggest targeted improvements

Add this as "Section 10.5: Advanced Analysis" in the notebook.
This demonstrates deeper understanding of feature engineering.
```

---

## Enhancement 3: Advanced SIEM Analysis (Activity 3)

```
Enhance Activity 3 report with advanced SIEM capabilities.

Add these elements to demonstrate expertise:

1. **Custom Detection Rule Creation:**
   - Document 2-3 custom SIEM rules you created
   - Show rule logic
   - Explain detection rationale
   - Test and validate effectiveness

2. **Attack Chain Reconstruction:**
   - Map attacks to MITRE ATT&CK kill chain
   - Show progression through attack stages
   - Correlate multiple log sources
   - Create visual kill chain diagram

3. **False Positive Analysis:**
   - Identify potential false positive scenarios
   - Demonstrate rule tuning
   - Show before/after tuning comparison
   - Explain detection accuracy tradeoffs

4. **Incident Response Playbook:**
   - Create mini-playbook for one attack type
   - Detection → Investigation → Response → Recovery
   - Show decision tree
   - Document required data/tools

5. **Performance Metrics:**
   - Calculate detection metrics:
     - True Positive Rate
     - False Positive Rate
     - Mean Time to Detect (MTTD)
     - Alert volume analysis
   - Present in professional metrics dashboard format

6. **Threat Hunting:**
   - Demonstrate proactive hunting query
   - Find activity that didn't trigger alerts
   - Show value beyond automated detection

These additions show you're operating at professional SOC analyst level.
Add as appendices or integrate into main report (watch word count).
```

---

# 📊 PROGRESS TRACKING

## Recommended: Use this tracking table

Copy this to a file: PROGRESS_TRACKER.md

```markdown
# Portfolio Progress Tracker

## Activity 1 (20%)
- [ ] Environment setup
- [ ] Student ID updated
- [ ] Q1-Q8 executed
- [ ] Q9 NetworkX graph complete
- [ ] Q10 Stage 1: Data exploration
- [ ] Q10 Stage 2: Deep dive analysis
- [ ] Q10 Stage 3: Attack classification
- [ ] Q10 Stage 4: Evidence documentation
- [ ] Q10 Stage 5: Report writing
- [ ] Final review & save
**Status:** __% complete

## Activity 2 (35%)
- [ ] Environment setup
- [ ] Student ID updated
- [ ] Sections 1-2 executed
- [ ] Sections 3-4 executed
- [ ] Sections 5-6 executed
- [ ] Section 7 executed
- [ ] Section 8 executed
- [ ] Section 9 executed
- [ ] Section 10 completed
- [ ] Final review & save
**Status:** __% complete

## Activity 3 (45%)
- [ ] Infrastructure chosen
- [ ] Infrastructure setup
- [ ] Infrastructure documented
- [ ] Attack planning complete
- [ ] Attack 1 executed
- [ ] Attack 1 detection analyzed
- [ ] Attack 2 executed
- [ ] Attack 2 detection analyzed
- [ ] Attack 3 executed (if doing 3+)
- [ ] Attack 3 detection analyzed
- [ ] All screenshots captured and organized
- [ ] Report outline created
- [ ] Report sections A-H written
- [ ] References completed
- [ ] Final review & PDF export
**Status:** __% complete

## Submission Preparation
- [ ] All files renamed correctly
- [ ] Pre-submission validation passed
- [ ] Submission package created
- [ ] Backup created
- [ ] Uploaded to Blackboard
- [ ] Submission verified
**Status:** __% complete

**Overall Completion:** __% / 100%
**Estimated Hours Remaining:** __
**Days Until Deadline:** __
```

---

# ⚡ QUICK START: What to Do RIGHT NOW

## Immediate Actions (Next 2 Hours)

### Custom Prompt for Claude Code:
```
I'm ready to start immediately. Help me prioritize what to do RIGHT NOW.

Based on today's date and the December 11, 2025 deadline, create:

1. **Today's Action Plan:**
   - What should I accomplish today?
   - Which prompts should I run first?
   - What's the minimum viable progress for today?

2. **This Week's Goals:**
   - Major milestones to hit this week
   - Which activity to focus on first
   - Daily time commitment needed

3. **Weekly Breakdown:**
   - Week-by-week plan until deadline
   - Hours per week required
   - Key deliverables each week

4. **Risk Assessment:**
   - What are the biggest risks to completion?
   - Where am I most likely to get stuck?
   - What contingency plans should I have?

5. **First Three Prompts:**
   Give me the FIRST THREE prompts from this implementation plan I should run right now to start making progress.

Be specific and realistic about time commitment.
Help me understand if I can realistically complete this by the deadline.
Create a personalized action plan for my situation.
```

---

# 🆘 TROUBLESHOOTING GUIDE

## If You Get Stuck

### General Stuck Prompt:
```
I'm stuck on [specific task]. Help me troubleshoot.

What I'm trying to do: [describe]
What's happening: [describe problem]
Error messages: [paste any errors]
What I've tried: [list attempts]

Provide:
1. Diagnosis of the problem
2. 3 potential solutions
3. Step-by-step fix for most likely solution
4. Alternative approaches if that doesn't work
5. When to skip and move on (don't let perfect be enemy of done)
```

### Time Crisis Prompt:
```
I'm running out of time. Help me prioritize for maximum grade with minimum time.

Time remaining: [X days/hours]
Current completion: [X%]
Activities status:
- Activity 1: [status]
- Activity 2: [status]
- Activity 3: [status]

Create a crisis completion plan:
1. What to finish fully (highest grade impact)
2. What to complete minimally (pass marks)
3. What to potentially skip (if absolutely necessary)
4. Fastest path to 50% (pass)
5. Realistic target grade with time remaining

Be honest about what's achievable.
Prioritize getting SOMETHING submitted over perfection.
```

---

# ✅ SUCCESS CRITERIA

## How to Know You're Done

### Final Success Check Prompt:
```
Am I truly submission-ready? Perform final success check.

For submission to be successful, verify:

**Activity 1:**
- [ ] Notebook executes without errors
- [ ] Q10 identifies 3+ suspicious IPs with detailed reasoning
- [ ] Demonstrates analytical thinking beyond basic analysis
- [ ] Grade estimate: __% / 20%

**Activity 2:**
- [ ] All models trained successfully
- [ ] Achieved >90% accuracy (requirement met)
- [ ] SHAP analysis complete
- [ ] Conclusions demonstrate understanding
- [ ] Grade estimate: __% / 35%

**Activity 3:**
- [ ] 2+ attacks executed and documented
- [ ] All attacks have SIEM detection evidence
- [ ] 15+ screenshots captured
- [ ] Report is 1400-1500 words
- [ ] Professional quality throughout
- [ ] Grade estimate: __% / 45%

**Overall:**
- [ ] Total estimated grade: __% / 100%
- [ ] Pass threshold (50%) achieved
- [ ] All files ready for submission
- [ ] Submission verified on Blackboard

Provide honest assessment of:
- Readiness level (Ready / Nearly Ready / Not Ready)
- Estimated grade range
- Critical gaps remaining
- Final recommendations

Be brutally honest. Better to know now than after submission.
```

---

# 📝 FINAL NOTES

## Important Reminders

1. **Start with Activity 2** - It's the most straightforward and builds confidence
2. **Don't neglect Activity 3** - It's 45% and requires the most time
3. **Question 10 (Activity 1) is crucial** - 8 marks, requires critical thinking
4. **>90% accuracy is required** for Activity 2 - Don't submit if not achieved
5. **Word count matters** - Activity 3 must be ≤1500 words
6. **Screenshots are evidence** - Activity 3 needs 15-25 quality screenshots
7. **Student ID everywhere** - Replace all placeholders
8. **All cells must be executed** - Staff won't re-run notebooks
9. **Backup everything** - Create backups before submission
10. **Verify submission** - Download and check after uploading

## Quality Over Quantity

- Better to do 2 attacks thoroughly than 5 attacks poorly
- Better to have deep analysis in Q10 than surface-level observations
- Better to have clear screenshots with good captions than many unclear ones
- Better to submit complete work than perfect incomplete work

## When in Doubt

Use this prompt:
```
I'm unsure about [decision]. Help me decide based on:
- Grade impact (which choice affects grade more?)
- Time efficiency (which is faster?)
- Submission requirements (which meets criteria?)
- Risk assessment (which is safer?)

Provide clear recommendation with rationale.
```

---

# 🎯 YOU'VE GOT THIS!

This plan transforms your templates into a complete, submission-ready portfolio.

**Your advantages:**
- Excellent templates already created
- Clear structure to follow
- Detailed prompts for every step
- Helper utilities already written

**The work ahead:**
- Execute the notebooks (straightforward)
- Analyze the data (guided by prompts)
- Set up SIEM and run attacks (time-intensive but manageable)
- Write the report (structured with clear guidance)

**Success strategy:**
1. Follow the prompts sequentially
2. Don't skip the documentation steps
3. Ask for help when stuck (use the troubleshooting prompts)
4. Track progress (use the tracker)
5. Submit something rather than nothing

**Remember:** You have 92% of the work ahead, but you also have 100% of the tools needed to complete it.

Start with Phase 1, Task 1.1 RIGHT NOW.

Good luck! 🚀
```
