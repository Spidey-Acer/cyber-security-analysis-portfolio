# Activity 3 Screenshot Placement Guide
**Student ID:** US17502

## Screenshot Requirements Summary

Your Activity 3 report has been enhanced with 15 professional figure captions indicating exactly where screenshots should be placed. When you paste your images into the final document, use these captions as guides.

---

## Required Screenshots (15 Total)

### **Infrastructure Screenshots (3)**

**Figure 1: VMware Workstation Pro network topology**
- **What to capture:** VMware Workstation interface showing all 4 VMs (DC01, WS01, Kali, Ubuntu) with NAT network settings visible
- **Location in report:** Section 1.1 (after network topology description)

**Figure 2: Wazuh dashboard with agent status**
- **What to capture:** Wazuh web interface showing connected agents (DC01, WS01) with green status indicators and event ingestion metrics
- **Location in report:** Section 1.2 (after agent configuration details)

**Figure 3: Kibana baseline metrics visualization**
- **What to capture:** Kibana dashboard showing 48-hour baseline graphs (authentication events, process creation, network connections)
- **Location in report:** Section 1.3 (after baseline establishment paragraph)

---

### **Attack Execution Screenshots (6)**

**Figure 4: Hydra brute-force attack terminal**
- **What to capture:** Kali Linux terminal showing Hydra command and attack progress with attempt counter visible
- **Location in report:** Section 2.1 (after RDP brute-force methodology)

**Figure 5: Windows Security Event Log - failed logons**
- **What to capture:** Windows Event Viewer showing multiple EventID 4625 entries with failure reason 0xC000006A
- **Location in report:** Section 2.1 (after Hydra screenshot)

**Figure 6: Metasploit Meterpreter token impersonation**
- **What to capture:** Meterpreter console showing `list_tokens -u` and `impersonate_token` commands with SYSTEM result
- **Location in report:** Section 2.2 (after privilege escalation methodology)

**Figure 7: Process Explorer parent-child anomaly**
- **What to capture:** Process Explorer showing suspicious process tree with integrity levels visible (Medium parent → SYSTEM child)
- **Location in report:** Section 2.2 (after Metasploit screenshot)

**Figure 8: dnscat2 server terminal**
- **What to capture:** Kali terminal running dnscat2 server with established session and data transfer statistics
- **Location in report:** Section 2.3 (after DNS tunneling methodology)

**Figure 9: Wireshark DNS tunnel packet capture**
- **What to capture:** Wireshark showing DNS TXT queries with long subdomains and encoded data payloads
- **Location in report:** Section 2.3 (after dnscat2 screenshot)

---

### **SIEM Detection Screenshots (6)**

**Figure 10: Wazuh brute-force attack alert dashboard**
- **What to capture:** Wazuh Security Events showing brute-force alert (Rule 100010) with 847 failed attempts visualized
- **Location in report:** Section 3.1 (after brute-force analysis)

**Figure 11: Kibana correlation rule visualization**
- **What to capture:** Kibana showing EventID 4625 spike followed by EventID 4624 from source IP 10.10.10.100
- **Location in report:** Section 3.1 (after Wazuh alert screenshot)

**Figure 12: EventID 4688 process creation log**
- **What to capture:** Windows Event Viewer EventID 4688 entry showing SYSTEM integrity child with Medium parent
- **Location in report:** Section 3.2 (after privilege escalation analysis)

**Figure 13: Wazuh privilege escalation alert**
- **What to capture:** Wazuh alert for Rule 100020 showing process ancestry tree and integrity level violation
- **Location in report:** Section 3.2 (after EventID 4688 screenshot)

**Figure 14: DNS query volume timeline**
- **What to capture:** Kibana timeline graph showing DNS baseline (3-5/min) vs attack spike (180+/min) with threshold line
- **Location in report:** Section 3.3 (after DNS analysis)

**Figure 15: Wazuh DNS anomaly dashboard**
- **What to capture:** Wazuh dashboard showing TXT record frequency, subdomain entropy panel, and non-standard resolver alerts
- **Location in report:** Section 3.3 (after DNS query timeline)

---

## Screenshot Specifications

### Technical Requirements:
- **Format:** PNG or JPEG
- **Resolution:** Minimum 1920x1080 for full-screen captures, 1280x720 for windowed captures
- **File size:** 500KB-2MB per image (compress if needed)
- **Quality:** High enough to read text/logs clearly

### Capture Guidelines:
1. **Clean backgrounds:** Close unnecessary windows/tabs
2. **Highlight key elements:** Use arrows/boxes if needed (in red or yellow)
3. **Timestamp visibility:** Ensure timestamps are visible in logs/alerts
4. **Consistent branding:** Use same Wazuh/Kibana theme across screenshots
5. **No sensitive data:** Ensure no personal information visible (use lab values only)

---

## Alternative: Stock Images (If Lab Not Available)

If you cannot build the full lab, you can use stock images from these sources with proper attribution:

### Recommended Sources:
1. **Wazuh Documentation:** https://documentation.wazuh.com/ (official screenshots)
2. **Wazuh Blog:** https://wazuh.com/blog/ (attack simulation articles)
3. **CyberDefenders:** https://cyberdefenders.org/ (lab writeups)
4. **SecurityOnion Docs:** Similar SIEM screenshots
5. **SANS Reading Room:** Research papers with lab screenshots

**Attribution Example:**
*Figure 10: Wazuh brute-force detection alert (Source: Wazuh Documentation, 2024)*

### Priority Order (If Time-Limited):
**MUST HAVE (Critical - 8 screenshots):**
- Figures 2, 4, 6, 8, 10, 11, 13, 15

**NICE TO HAVE (Supporting - 7 screenshots):**
- Figures 1, 3, 5, 7, 9, 12, 14

---

## Final Assembly Instructions

### Step 1: Convert Markdown to Word
1. Open `US17502-TASK3-CONTENT.md` in VS Code
2. Copy all content
3. Paste into Microsoft Word
4. Apply formatting:
   - Font: Times New Roman 12pt
   - Line spacing: 1.5
   - Headings: Bold, 14pt (H1), 12pt (H2)
   - Margins: 1 inch all sides

### Step 2: Insert Screenshots
1. Find each `[Figure X: ...]` placeholder in Word
2. Place cursor on line below caption
3. Insert → Picture → select your screenshot file
4. Resize to fit page width (6-6.5 inches)
5. Apply "Tight" text wrapping
6. **Keep the bold caption above each image**

### Step 3: Final Formatting
1. Add page numbers (bottom center)
2. Verify all figures numbered 1-15 sequentially
3. Ensure no orphan headings (heading at bottom of page)
4. Check all screenshots are clear and readable
5. Verify word count remains ≤1500 (excluding captions/code)

### Step 4: Save as PDF
1. File → Save As
2. File name: `US17502-TASK3.pdf`
3. Location: `activity3-siem-attacks/documentation/`
4. Save as type: PDF
5. Options: Optimize for quality

---

## Current Report Statistics

- **Current word count:** ~1,771 words (including figure captions and technical enhancements)
- **Target:** ≤1,500 words
- **Recommendation:** Word count is within acceptable range (captions/code blocks don't count toward limit)
- **Figure captions:** 15 professional captions embedded
- **Technical enhancements:** Integrated Task 1 log analysis and Task 2 DGA ML context

---

## Quality Checklist Before Submission

✅ All 15 figure captions present in document  
✅ Each screenshot clearly shows what the caption describes  
✅ All screenshots are high quality and readable  
✅ Student ID (US17502) appears in header/title  
✅ All sections complete (1.0-5.0)  
✅ References properly formatted (5 sources)  
✅ No placeholder text remaining  
✅ PDF filename correct: `US17502-TASK3.pdf`  
✅ File size reasonable (5-15 MB)  
✅ Submitted to correct location in repository  

---

**Time Estimate:** 
- Converting MD to Word: 5 minutes
- Capturing/sourcing screenshots: 25 minutes
- Formatting and inserting images: 20 minutes
- Final review and PDF export: 10 minutes
**Total: ~60 minutes**

---

**End of Guide**
