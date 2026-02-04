# AWS-Cost-Optimizaion
# AWS Cost Optimizer & Monitoring System

## 📌 Project Overview
The AWS Cost Optimizer & Monitoring System is a cloud-based solution designed to identify underutilized and unused AWS resources and provide cost-saving recommendations. The project leverages AWS native services to monitor resource usage, optimize cloud spending, and improve operational efficiency.

This project is suitable for **freshers**, **cloud engineers**, and **service desk / monitoring roles**.

---

## 🎯 Objectives
- Monitor AWS resource utilization
- Identify idle or underutilized EC2 instances
- Detect unattached EBS volumes
- Provide cost optimization recommendations
- Send automated alerts to administrators
- Reduce unnecessary AWS billing

---

## 🏗 Architecture Overview
EventBridge triggers the Lambda function on a scheduled basis.  
Lambda fetches metrics from CloudWatch and resource details from EC2.  
Identified cost issues are sent as alerts via SNS email notifications.

**Flow:**
EventBridge → Lambda → CloudWatch & EC2 → SNS → Email Alerts


---

## 🛠 AWS Services Used
- **AWS Lambda** – Core automation logic
- **Amazon EC2** – Compute resource monitoring
- **Amazon EBS** – Storage usage analysis
- **Amazon CloudWatch** – Metrics and logs
- **Amazon SNS** – Email notifications
- **Amazon EventBridge** – Scheduled execution
- **AWS IAM** – Secure role-based access
- **AWS Budgets** – Cost threshold alerts
- **Amazon S3** – Lifecycle policy optimization (optional)

---

## ⚙️ Features
- Detects EC2 instances with low CPU utilization
- Identifies unattached EBS volumes
- Sends cost optimization recommendations via email
- Fully automated daily execution
- Follows AWS security best practices (IAM least privilege)
- Safe implementation (no automatic deletion of resources)

---

## 🚀 Implementation Steps (High Level)
1. Enabled AWS Billing and Cost Explorer
2. Created IAM role with required permissions
3. Configured SNS for email notifications
4. Launched test EC2 and EBS resources
5. Developed AWS Lambda function using Python
6. Integrated CloudWatch metrics
7. Automated execution using EventBridge
8. Tested alerts and verified results

---

## 🧪 Test Cases
| Scenario | Expected Result |
|-------|----------------|
| EC2 with low CPU usage | Detected and reported |
| Unattached EBS volume | Listed in alert |
| Lambda execution | Successful |
| SNS notification | Email received |

---

## 📊 Results
- Identified unused compute and storage resources
- Improved visibility into cloud spending
- Prevented unnecessary monthly AWS costs
- Estimated cost optimization of **30–40%**

---

## 🔐 Security & Best Practices
- IAM roles used instead of hardcoded credentials
- Least privilege access model
- Read-only permissions for monitoring
- No destructive automation (recommendation-based)

---

## 📈 Future Enhancements
- Snapshot cost detection and alerts
- Automatic shutdown of non-production EC2 instances
- Cost forecasting using ML models
- Dashboard visualization using Amazon QuickSight
- Multi-account cost optimization

---

## 👨‍💻 Author
**Margam Saicharan**  
B.Tech – AI & Data Science  
AWS & Cloud Enthusiast  

---

## 📄 License
This project is for educational and learning purposes.
