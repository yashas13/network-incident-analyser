# Network Incident Analyser
# Author: Yashas Vishwakarma
# Built with: Azure AI Language Service

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your Azure credentials
ENDPOINT = "your-endpoint-here"
KEY = "your-key-here"

client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY)
)

def analyse(text):
    phrases = client.extract_key_phrases([text])[0].key_phrases
    sentiment = client.analyze_sentiment([text])[0].sentiment

    print("Key Issues Found:", phrases)
    print("Severity Sentiment:", sentiment.upper())

# Example incidents
if __name__ == "__main__":
    analyse("DNS resolution failing for all users on VLAN 10. Internal applications unreachable. Started after maintenance window at 2AM. Affecting 200+ users.")
