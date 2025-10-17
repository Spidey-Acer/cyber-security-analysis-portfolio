# Activity 3: SIEM-Based Attack Simulation and Detection

**Student ID:** [YOUR_STUDENT_ID]  
**Module:** UFCFFY-15-M Cyber Security Analytics  
**Word Count:** [XXX/1500]

---

## Executive Summary

[Brief 2-3 sentence overview of what you accomplished: infrastructure used, attacks performed, detection methods]

---

## 1. Introduction (150-200 words)

### 1.1 Objectives
- [State the purpose of this investigation]
- [List specific attack scenarios you plan to simulate]
- [Explain what you aim to demonstrate]

### 1.2 Scope
- [Define the boundaries of your investigation]
- [List the tools and platforms used]

---

## 2. Infrastructure Setup (250-300 words)

### 2.1 Environment Architecture
**Platform Used:** [GoibhniUWE / DetectionLab / Custom Setup]

[INSERT SCREENSHOT: Architecture diagram showing VMs and network topology]

**Figure 1:** Virtual infrastructure architecture

### 2.2 Components
| Component | Purpose | Specifications |
|-----------|---------|---------------|
| SIEM Platform | [Splunk/Wazuh/Elastic] | [Version, config] |
| Target System | [Windows Server/Linux] | [OS, services] |
| Attack System | [Kali Linux/Custom] | [Tools installed] |

### 2.3 Setup Process
1. [Step-by-step description of how you configured the environment]
2. [Challenges encountered and solutions]
3. [Configuration of logging and monitoring]

[INSERT SCREENSHOT: SIEM dashboard]

**Figure 2:** SIEM platform initial configuration

---

## 3. Attack Execution (400-500 words)

### 3.1 Attack Scenario 1: [Attack Name]

**Attack Type:** [e.g., Brute Force, SQL Injection, Privilege Escalation]

**Objective:** [What you're trying to achieve]

**Methodology:**
1. [Step-by-step description of the attack]
2. [Commands/tools used]
3. [Expected outcomes]

[INSERT SCREENSHOT: Attack execution]

**Figure 3:** [Description of attack in progress]

**Technical Details:**
```bash
# Example command used
[paste your commands here]
```

### 3.2 Attack Scenario 2: [Attack Name]

**Attack Type:** [e.g., Lateral Movement, Data Exfiltration]

[Follow same structure as 3.1]

[INSERT SCREENSHOT]

**Figure 4:** [Description]

### 3.3 Attack Scenario 3: [Attack Name]

[Optional - include if you performed multiple sophisticated attacks]

---

## 4. Attack Detection and Analysis (400-500 words)

### 4.1 Detection Methodology

**Approach:**
- [Describe how you configured the SIEM to detect attacks]
- [Explain what log sources were used]
- [Detail any custom rules or alerts created]

### 4.2 Detection Results - Attack 1

[INSERT SCREENSHOT: SIEM showing detected activity]

**Figure 5:** Detection of [Attack 1] in SIEM

**Analysis:**
- **Indicators Observed:** [List specific indicators: IPs, processes, file changes, etc.]
- **Log Evidence:** [Quote relevant log entries]
- **Timeline:** [When did detection occur relative to attack]

**Example Log Entry:**
```
[Paste relevant log entry showing detection]
```

### 4.3 Detection Results - Attack 2

[Follow same structure as 4.2]

[INSERT SCREENSHOT]

**Figure 6:** [Description]

### 4.4 Detection Results - Attack 3

[If applicable]

---

## 5. Critical Analysis (200-250 words)

### 5.1 Effectiveness of Detection

**Successful Detections:**
- [Which attacks were detected successfully?]
- [How quickly were they detected?]
- [What made detection possible?]

**Challenges and Limitations:**
- [Were any attacks missed initially?]
- [What adjustments were needed?]
- [Limitations of the SIEM configuration]

### 5.2 False Positives/Negatives
- [Discuss any false alarms]
- [Explain how you tuned detection rules]

---

## 6. Mitigation Recommendations (150-200 words)

Based on the attacks performed and detected:

1. **Preventive Controls:**
   - [Recommendations to prevent attacks]
   
2. **Detective Controls:**
   - [Improvements to detection capabilities]
   
3. **Response Procedures:**
   - [Recommended response actions]

---

## 7. Reflection and Lessons Learned (100-150 words)

- [What did you learn about SIEM platforms?]
- [Insights about attack patterns]
- [Challenges overcome]
- [What would you do differently?]

---

## 8. Conclusion (100-150 words)

[Summarize your findings, emphasizing:]
- Successfully demonstrated attacks
- Effectiveness of SIEM detection
- Key insights gained

---

## References

[List all sources cited using UWE Harvard format]

1. [Source 1]
2. [Source 2]
3. ...

---

## Appendix (if needed - not counted in word count)

### Appendix A: Configuration Files
[Relevant SIEM rules, configurations]

### Appendix B: Additional Screenshots
[Extra evidence not included in main body]

---

**Declaration:** I confirm that this is my own work and I have acknowledged all sources used.

**Word Count:** [XXX/1500]