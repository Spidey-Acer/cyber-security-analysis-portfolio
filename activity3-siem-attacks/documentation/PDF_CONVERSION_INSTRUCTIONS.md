# Quick PDF Conversion Guide - Activity 3
**Student ID:** US17502

---

## ✅ STATUS: HTML File Created Successfully!

The file `US17502-TASK3-TEMP.html` has been created and should be open in your browser.

---

## 🚀 FASTEST METHOD: Browser Print to PDF (2 minutes)

The HTML file is now open in your browser. Follow these steps:

### Step-by-Step Instructions:

1. **Press `Ctrl + P`** (or click the three-dot menu → Print)

2. **In the Print Dialog:**
   - **Destination:** Select "Save as PDF" or "Microsoft Print to PDF"
   - **Layout:** Portrait
   - **Pages:** All
   - **Margins:** Default
   - **Scale:** 100%
   - ✓ Check "Background graphics" (if available)

3. **Click "Save" or "Print"**

4. **Save the file as:**
   - File name: `US17502-TASK3.pdf`
   - Location: `C:\Users\HP\University\cyber-security-analysis-portfolio\activity3-siem-attacks\documentation\`

5. **Done!** You now have your PDF submission file.

---

## 🎯 ALTERNATIVE: Microsoft Word Method (3 minutes)

If browser method doesn't work well:

1. **Right-click** `US17502-TASK3-TEMP.html`
2. **Open With** → Microsoft Word
3. Word will import the HTML
4. **File** → **Save As**
5. Choose **PDF** format
6. Save as `US17502-TASK3.pdf`

---

## ✓ VERIFY YOUR PDF

After creating the PDF, check that it contains:

- [ ] Student ID "US17502" visible at the top
- [ ] All 5 main sections (Executive Summary → Conclusion)
- [ ] 15 figure captions present (even if images are placeholders)
- [ ] Code blocks formatted correctly
- [ ] References section at the end
- [ ] File size: 200KB - 5MB (reasonable range)
- [ ] Total pages: Approximately 10-15 pages

---

## 🧹 CLEANUP AFTER PDF CREATION

Once you have `US17502-TASK3.pdf`, delete the temporary HTML file:

```powershell
cd "C:\Users\HP\University\cyber-security-analysis-portfolio\activity3-siem-attacks\documentation"
Remove-Item US17502-TASK3-TEMP.html
Remove-Item convert_to_html.py
```

---

## 📊 FINAL SUBMISSION CHECKLIST

After PDF creation:

### Required Files:
- ✅ `activity1-log-analysis/notebooks/US17502-TASK1.ipynb`
- ✅ `activity2-dga-classification/notebooks/US17502-TASK2.ipynb`
- ⚠️ `activity3-siem-attacks/documentation/US17502-TASK3.pdf` ← **CREATE THIS NOW**

### Optional Enhancement:
- Add screenshots to PDF (15 figure locations marked)
- Use stock images from Wazuh documentation if lab not available

---

## 🎓 SUBMISSION READY!

Once you have the PDF:

```powershell
# Verify all three submission files exist
dir activity1-log-analysis\notebooks\US17502-TASK1.ipynb
dir activity2-dga-classification\notebooks\US17502-TASK2.ipynb
dir activity3-siem-attacks\documentation\US17502-TASK3.pdf

# Commit to git
git add activity3-siem-attacks/documentation/US17502-TASK3.pdf
git commit -m "Add Activity 3 final PDF submission"
git push origin main
```

---

## ⏱️ TIME ESTIMATE

- PDF conversion: **2 minutes**
- Verification: **1 minute**
- Git commit: **1 minute**

**Total: 4 minutes to submission-ready!**

---

**Questions?**
- PDF looks wrong? Try the Word method instead
- Need screenshots? See `SCREENSHOT_PLACEMENT_GUIDE.md`
- File too large? Use lower quality settings in Print dialog

---

**Your portfolio is 95% complete. This is the final step!**
