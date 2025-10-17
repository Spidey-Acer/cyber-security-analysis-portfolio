# Attack Documentation - Activity 3
## Working Notes (Not for Submission)

**Purpose:** Use this document to track your attacks as you perform them.  
Later, you'll use these notes to write your formal report.

---

## Infrastructure Details

### Environment Setup
- **Platform:** [GoibhniUWE / DetectionLab / Custom]
- **SIEM:** [Splunk / Wazuh / Elastic] Version: [X.X]
- **Attacker Machine:** [OS and IP]
- **Target Machine:** [OS and IP]
- **Network:** [IP range and configuration]

### VMs Running
| VM Name | OS | IP Address | Role | Services Running |
|---------|----|-----------|----|-------------------|
| SIEM | | | Log collection | |
| Target1 | | | Victim | |
| Attacker | | | Attack system | |

---

## Attack 1: [Attack Name]

### Pre-Attack Planning
**Date/Time:** [YYYY-MM-DD HH:MM]  
**Attack Type:** [e.g., Brute Force, Port Scan, Privilege Escalation]  
**Objective:** [What are you trying to achieve?]  
**Tools Required:** [List tools needed]  
**Expected Indicators:** [What logs/alerts do you expect to see?]

### Execution Steps

#### Step 1: [Action]
**Command:**
```bash
[paste command here]
```

**Output:**
```
[paste output here]
```

**Screenshots:**
- [ ] Screenshot: `03_attack1_step1.png`

**Notes:**
- [Any observations, errors, or adjustments made]

#### Step 2: [Action]
**Command:**
```bash
[paste command here]
```

**Output:**
```
[paste output here]
```

**Screenshots:**
- [ ] Screenshot: `04_attack1_step2.png`

#### Step 3: [Action]
[Continue pattern...]

### Attack Results
**Success:** [Yes/No/Partial]  
**Time Taken:** [Duration]  
**Challenges:** [Issues encountered]  
**Target Impact:** [What happened on target system]

### Detection Analysis

#### SIEM Query Used
```
[paste SIEM query/search]
```

#### Logs Captured
**Source:** [Log source - Windows Event, Syslog, etc.]  
**Key Fields:**
```
[paste relevant log entries]
```

#### Detection Timeline
| Time | Event | Source | Severity |
|------|-------|--------|----------|
| 10:30:15 | [Event description] | [Source] | [Level] |
| 10:30:22 | [Event description] | [Source] | [Level] |

#### Screenshots
- [ ] `05_attack1_siem_alert.png` - SIEM alert triggered
- [ ] `06_attack1_log_evidence.png` - Raw log evidence
- [ ] `07_attack1_timeline.png` - Timeline view

#### Detection Effectiveness
- **Detected:** [Yes/No]
- **Time to Detect:** [How long after attack started]
- **Alert Accuracy:** [True positive/False positive]
- **Missing Elements:** [What wasn't captured]

### Lessons Learned
- [What worked well]
- [What could be improved]
- [Unexpected findings]

---

## Attack 2: [Attack Name]

[Repeat the same structure as Attack 1]

### Pre-Attack Planning
**Date/Time:**  
**Attack Type:**  
**Objective:**  
**Tools Required:**  
**Expected Indicators:**

### Execution Steps
[Document each step...]

### Attack Results
[Document results...]

### Detection Analysis
[Document detection...]

### Lessons Learned
[Document lessons...]

---

## Attack 3: [Attack Name]

[If performing additional attacks, repeat structure]

---

## SIEM Configuration Notes

### Custom Rules Created
```
[Document any custom detection rules or alerts you created]
```

### Queries Used
```
# Query 1: Detect failed login attempts
index=windows EventCode=4625
| stats count by Account_Name, src_ip

# Query 2: [Description]
[paste query]
```

### Tuning Performed
| Issue | Action Taken | Result |
|-------|-------------|--------|
| Too many false positives for X | Adjusted threshold from Y to Z | Reduced alerts by 50% |

---

## Attack Ideas & Research

### Potential Attack Vectors
1. **Brute Force Attack**
   - Tools: Hydra, Medusa
   - Target: SSH/RDP
   - Detection: Multiple failed authentication events

2. **Port Scanning**
   - Tools: Nmap
   - Target: Network services
   - Detection: Unusual network traffic patterns

3. **SQL Injection**
   - Tools: SQLmap, manual
   - Target: Web application
   - Detection: Suspicious query patterns in web logs

4. **Privilege Escalation**
   - Tools: Windows exploits, sudo misconfig
   - Target: Local system
   - Detection: Process creation, registry changes

5. **Lateral Movement**
   - Tools: PsExec, WMI
   - Target: Other network hosts
   - Detection: Remote process execution

6. **Data Exfiltration**
   - Tools: Custom scripts, DNS tunneling
   - Target: Sensitive files
   - Detection: Unusual outbound traffic

7. **Malware Execution**
   - Tools: Meterpreter, Cobalt Strike
   - Target: System compromise
   - Detection: Process injection, C2 traffic

### Research Notes

**Attack: [Name]**
- Source: [URL/Paper]
- Key Technique: [Description]
- Detection Method: [How to detect]
- Implementation Notes: [How to perform]

---

## Screenshot Inventory

### Infrastructure (Folder: screenshots/infrastructure/)
- [ ] `01_network_topology.png` - Network diagram
- [ ] `02_vm_configurations.png` - VM settings
- [ ] `03_siem_dashboard.png` - Initial SIEM view

### Attack 1 (Folder: screenshots/attacks/)
- [ ] `04_attack1_planning.png`
- [ ] `05_attack1_execution.png`
- [ ] `06_attack1_results.png`

### Detection 1 (Folder: screenshots/detection/)
- [ ] `07_attack1_siem_alert.png`
- [ ] `08_attack1_logs.png`
- [ ] `09_attack1_timeline.png`

[Continue for all attacks...]

---

## Common Commands Reference

### SIEM (Splunk)
```bash
# Search failed logins
index=windows EventCode=4625

# Search process creation
index=sysmon EventCode=1

# Search network connections
index=sysmon EventCode=3
```

### Attack Tools

#### Nmap
```bash
# Basic scan
nmap -sV target_ip

# Aggressive scan
nmap -A -T4 target_ip

# Specific ports
nmap -p 22,80,443 target_ip
```

#### Hydra (Brute Force)
```bash
# SSH brute force
hydra -l username -P /path/to/wordlist.txt ssh://target_ip

# RDP brute force
hydra -l username -P /path/to/wordlist.txt rdp://target_ip
```

#### Metasploit
```bash
# Start msfconsole
msfconsole

# Search exploits
search type:exploit platform:windows

# Use exploit
use exploit/windows/smb/ms17_010_eternalblue
```

---

## Troubleshooting Log

### Issue 1: [Problem]
**Date:** [Date]  
**Problem:** [Description]  
**Solution:** [How you fixed it]  
**Outcome:** [Result]

### Issue 2: [Problem]
[Continue...]

---

## Timeline of Work

| Date | Activity | Duration | Notes |
|------|----------|----------|-------|
| 2025-11-01 | Setup infrastructure | 3 hours | Had issues with network config |
| 2025-11-02 | Attack 1 execution | 2 hours | Successful |
| 2025-11-03 | Detection analysis | 2 hours | Created custom rule |

---

## Report Writing Checklist

When converting these notes to formal report:

- [ ] Remove informal language and working notes
- [ ] Structure using report template
- [ ] Add formal introductions and conclusions to each section
- [ ] Ensure all screenshots are referenced in text
- [ ] Add figure captions (Figure 1: Description)
- [ ] Check word count (max 1500)
- [ ] Add references for tools/techniques used
- [ ] Proofread for grammar and clarity
- [ ] Verify academic tone throughout

---

## References to Cite

Keep track of sources as you research:

1. [Tool documentation]
2. [CVE references]
3. [Attack technique papers]
4. [MITRE ATT&CK techniques]
5. [Configuration guides]

Use UWE Harvard format for all citations.

---

## Ideas for Excellence (Higher Marks)

To achieve 70%+ marks:

1. **Multiple Sophisticated Attacks:** Go beyond basic examples
2. **Custom Detection Rules:** Show you can create tailored detections
3. **Cross-correlation:** Link multiple log sources
4. **Attack Chain:** Show progression through kill chain
5. **Evasion Techniques:** Demonstrate advanced attacker behavior
6. **Incident Response:** Show response actions, not just detection
7. **Threat Intelligence:** Link to real-world threats (MITRE ATT&CK)
8. **Metrics:** Quantify detection effectiveness

---

**Remember:** This is your working document. Keep it detailed!  
You'll thank yourself when writing the formal report.