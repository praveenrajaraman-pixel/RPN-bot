import os
from simple_salesforce import Salesforce

class SalesforceIntegration:
    def __init__(self):
        self.username = os.getenv('SALESFORCE_USERNAME')
        self.password = os.getenv('SALESFORCE_PASSWORD')
        self.security_token = os.getenv('SALESFORCE_SECURITY_TOKEN')
        self.sf = None
        self.connect()

    def connect(self):
        try:
            self.sf = Salesforce(username=self.username, password=self.password, security_token=self.security_token)
            print("Connected to Salesforce")
        except Exception as e:
            print(f"Connection error: {e}")

    def sync_meeting_to_salesforce(self, meeting_data):
        try:
            activity_data = {'Subject': meeting_data.get('title'), 'Description': meeting_data.get('notes'), 'ActivityDate': meeting_data.get('date')}
            result = self.sf.Task.create(activity_data)
            return result
        except Exception as e:
            return {'error': str(e)}