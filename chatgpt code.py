class Lead:
    def __init__(self, name, email, channel):
        self.name = name
        self.email = email
        self.channel = channel
        self.stage = 'Landing Page'

    def move_to_next_stage(self, opted_in):
        if opted_in:
            self.stage = 'Thank You Page'
        else:
            self.stage = 'Retargeting Ads'

    def __str__(self):
        return f"Lead: {self.name}, Email: {self.email}, Channel: {self.channel}, Stage: {self.stage}"

class SalesFunnel:
    def __init__(self):
        self.leads = []

    def add_lead(self, lead):
        self.leads.append(lead)

    def process_leads(self, opted_in):
        for lead in self.leads:
            lead.move_to_next_stage(opted_in)

    def show_leads(self):
        for lead in self.leads:
            print(lead)

# Example usage
funnel = SalesFunnel()
funnel.add_lead(Lead("John Doe", "john@example.com", "SEO"))
funnel.add_lead(Lead("Jane Smith", "jane@example.com", "Email"))

print("Before processing:")
funnel.show_leads()

# Simulate opt-in decision
funnel.process_leads(opted_in=True)

print("\nAfter processing:")
funnel.show_leads()