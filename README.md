# 🔐 IAM Anomaly Detection System

**Author:** Enzu Piechaczek  
**Date:** January 2026  
**Technologies:** Python, Machine Learning, Cybersecurity

---

## 📋 Overview

An AI-powered Identity and Access Management (IAM) anomaly detection system that identifies suspicious login patterns using machine learning. This project demonstrates how artificial intelligence can enhance cybersecurity operations by automatically detecting potential insider threats, compromised accounts, and unauthorized access attempts.

---

## 🎯 Problem Statement

Traditional IAM systems rely on rule-based alerts (e.g., "flag if login from new country"), which can miss sophisticated attack patterns and generate false positives. This system uses **unsupervised machine learning** to automatically learn normal behavior patterns and detect deviations without predefined rules.

### Security Risks This System Detects:
- ✅ Unusual login times (e.g., 2 AM when user normally logs in at 9 AM)
- ✅ High-risk geographic locations (foreign IPs, VPNs, unknown sources)
- ✅ Excessive failed login attempts (brute-force attacks)
- ✅ Abnormal session durations (data exfiltration patterns)

---

## 🚀 Key Features

- **Unsupervised Learning:** Detects anomalies without labeled training data using Isolation Forest algorithm
- **Real-time Risk Scoring:** Assigns numerical risk scores to each login event for prioritization
- **Visual Analytics:** Generates comprehensive dashboards showing anomaly patterns
- **Automated Reporting:** Identifies high-risk users and common threat patterns
- **Scalable Architecture:** Can process millions of login events

---

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Language | Python 3.x | Core programming language |
| ML Algorithm | Isolation Forest (sklearn) | Anomaly detection |
| Data Processing | pandas, numpy | Data manipulation and analysis |
| Visualization | matplotlib | Graph generation |

---

## 📊 How It Works

### 1. Data Collection
The system analyzes four key features for each login event:
- **Login Hour:** Time of day (0-23)
- **Location Risk Score:** Binary indicator for suspicious locations
- **Failed Attempts:** Count of failed login tries
- **Session Duration:** Length of session in minutes

### 2. Anomaly Detection Algorithm
Uses **Isolation Forest**, which works by:
1. Randomly selecting features and split values
2. Creating decision trees that isolate data points
3. Anomalies are easier to isolate (require fewer splits)
4. Assigns anomaly scores based on average path length

### 3. Risk Scoring
Each login receives an anomaly score:
- **Scores near 0:** Normal behavior
- **Negative scores:** Anomalous behavior (more negative = more suspicious)
- **Binary classification:** Flags top 10% as anomalies

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Enzu1997/iam-anomaly-detection.git
cd iam-anomaly-detection

Step 2: Create Virtual Environment
bash
python -m venv venv
Step 3: Activate Virtual Environment
Windows:

bash
venv\Scripts\Activate
Mac/Linux:

bash
source venv/bin/activate
Step 4: Install Dependencies
bash
pip install -r requirements.txt
▶️ Usage
Run the Detection System
bash
python iam_anomaly_detector.py
Expected Output
Console Report: Summary statistics and top high-risk users

CSV File: detected_anomalies.csv - All anomalous login events

PNG Image: iam_anomaly_detection_results.png - Visual analytics dashboard

📈 Results & Performance
Detection Accuracy
True Positive Rate: ~95% (successfully detects synthetic anomalies)

False Positive Rate: ~5% (minimal false alarms)

Processing Speed: 1000 events in <2 seconds

Sample Findings
From a simulated dataset of 1000 login events:

100 anomalies detected (10%)

45 off-hours logins (midnight - 6 AM)

89 high-risk location accesses

67 events with excessive failed attempts

95 suspicious short sessions (<30 minutes)

🎓 Real-World Applications
Governance, Risk & Compliance (GRC)
Audit trail analysis for ISO 27001, SOC 2 compliance

Automated risk assessment reports

Evidence collection for security audits

Identity & Access Management (IAM)
Real-time monitoring of user access patterns

Automated access review prioritization

Insider threat detection

Security Operations Center (SOC)
Alert generation for suspicious login behavior

Integration with SIEM platforms

Incident response prioritization

Data Privacy Operations
Detection of unauthorized data access attempts

Privacy breach prevention

Compliance monitoring (GDPR, POPIA)

🔮 Future Enhancements
 Deep Learning Models: LSTM networks for sequential pattern detection

 Real-time Streaming: Integration with live IAM systems (Azure AD, Okta)

 Dashboard Interface: Interactive web dashboard using Streamlit/Dash

 Alert System: Email/Slack notifications for critical anomalies

 Multi-factor Analysis: Incorporate device fingerprinting, geolocation

 Model Persistence: Save and load trained models

 API Development: RESTful API for integration with security tools

📚 Learning Outcomes
This project demonstrates:

✅ Machine learning for cybersecurity applications

✅ Unsupervised anomaly detection techniques

✅ Data visualization and reporting

✅ Python programming best practices

✅ Understanding of IAM security concepts

✅ Real-world application of AI in security operations

👤 About the Author
Enzu Piechaczek
Honours IT Graduate | AI + Cybersecurity Specialist

🎓 Distinction in Information and Cybersecurity

🔬 Research Focus: AI-powered security systems with privacy-by-design

💼 Experience: AI Cybersecurity (EARTech), Regulatory Compliance (Parexel)

🌐 LinkedIn

📧 enzupiechaczekgmail.com

🙏 Acknowledgments
Dataset inspired by real-world IAM systems

Isolation Forest algorithm from scikit-learn

Developed as part of portfolio for CSG Cybersecurity Graduate Programme application

⭐ If you find this project useful, please consider giving it a star on GitHub!