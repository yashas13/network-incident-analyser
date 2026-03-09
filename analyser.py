# 🔍 Network Incident Analyser

An AI-powered tool that analyses network incident descriptions and automatically 
extracts key issues and severity — built using Azure AI Language Service.

## 🏗️ Architecture
```
Incident Text Input
        ↓
Azure AI Language Service
        ↓
Key Phrase Extraction + Sentiment Analysis
        ↓
Structured Incident Summary
```

## ✨ Features

- 🔍 Automatic key issue extraction from incident logs
- 📊 Severity sentiment classification (Positive / Neutral / Negative)
- ⚡ Instant analysis — no manual triage needed
- 🌐 Supports multiple languages
- ☁️ Fully hosted on Azure

## 🛠️ Azure Services Used

| Service | Purpose |
|---|---|
| Azure AI Language Service | Key phrase extraction and sentiment analysis |
| Azure Cognitive Services | Underlying AI/NLP engine |

## 💬 Example Input
```
DNS resolution failing for all users on VLAN 10. Internal applications 
unreachable. Started after maintenance window at 2AM. Affecting 200+ users.
```

## 📤 Example Output
```
Key Issues Found: ['DNS resolution', 'VLAN 10', 'maintenance window', '200+ users']
Severity Sentiment: NEGATIVE
```

## 🚀 How to Run
```bash
pip install azure-ai-textanalytics
```
```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint="your-endpoint",
    credential=AzureKeyCredential("your-key")
)
```

## 👨‍💻 Author

**Yashas Vishwakarma**
Network Engineer → AI Engineer
3.5 years enterprise networking experience (Cisco, Computacenter/Daimler)
