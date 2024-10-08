import re
import os
def extract_customer_data1(hackathon_match):
    requirements_keywords = ['looking for', 'interested in', 'require', 'want', 'need', 'searching up for', 'willing to buy', 'taking interests in buying']
    requirements = []

    for line in hackathon_match.splitlines():
        for keyword in requirements_keywords:
            if keyword in line.lower():
                requirements.append(line.strip())
                break

    return requirements

def extract_company_data1(hackathon_match):
    policy_keywords = ['policy', 'terms', 'conditions', 'warranty', 'insurance', 'financing', 'scheme', 'guidelines']
    policies = []

    for line in hackathon_match.splitlines():
        for keyword in policy_keywords:
            if keyword in line.lower():
                policies.append(line.strip())
                break

    return policies

def extract_customer_data2(hackathon_match):
    objection_keywords = ['but', 'however', 'concern', 'issue', 'problem', 'worry', 'perhaps', 'troublesome', 'awkward', 'prickly', 'complicated']
    objections = []

    for line in hackathon_match.splitlines():
        for keyword in objection_keywords:
            if keyword in line.lower():
                objections.append(line.strip())
                break

    return objections

def process_hackathon_match(hackathon_match):
    customer_data1 = extract_customer_data1(hackathon_match)
    company_data1 = extract_company_data1(hackathon_match)
    customer_data2 = extract_customer_data2(hackathon_match)

    print("\nCustomer Requirements for Car:")
    for req in customer_data1:
        print("-", req)

    print("\nCompany Policies Discussed:")
    for policy in company_data1:
        print("-", policy)

    print("\nCustomer Objections:")
    for objection in customer_data2:
        print("-", objection)

# Example conversation hackathon_match
hackathon_match = """
Salesperson: Good afternoon, sir. Have you booked the vehicle yet?

Customer: Yes, I just booked it now.

Salesperson: Great! I see you booked it for 1 PM. Have you received any confirmation message?

Customer: No, I haven't received any message yet.

Salesperson: Sometimes there's a slight delay. I've set it to notify you once it goes live. You should also download our application and log in with the same number you used for booking. That way, you'll get real-time updates.

Customer: How much does it cost?

Salesperson: The exact price isn't listed in the application, but you'll receive a message once it's confirmed. If someone else has booked it, you'll know by this evening. I've scheduled a contact for you.

Customer: Can I get a loan for this vehicle?

Salesperson: Unfortunately, it's a bit challenging since the car is over 10 years old. The interest rates are usually higher for older vehicles. Do you have any existing loans?

Customer: I was considering YoCars finance. I'll need to check their terms.

Salesperson: That's a good option. I've logged your interest, and you'll get an update soon. I've scheduled it.

Customer: What other vehicles are available within this budget?

Salesperson: In the sedan category, we have a Swift 2 City. However, it's currently booked by someone else. If you set the "notify me" option, you'll be alerted once it's available. It should be updated by this evening.

Customer: How's the power of the car?

Salesperson: It has an 1800 cc engine. Once you take it to the garage for a tune-up, it will perform excellently. We've already done some preliminary tuning.

Customer: Do you need to check my eligibility for financing?

Salesperson: The application has already checked your eligibility.

Customer: Will this affect my credit score?

Salesperson: No, it won't. Have you completed any applications recently?

Customer: Yes, I have.

Salesperson: The eligibility check is done. Your eligibility varies depending on the model and vehicle. For cars less than 10 years old, we can contact the finance team for more details.

Customer: Can I take a test drive?

Salesperson: Yes, you can. However, the test drive from Rajajinagar was canceled. Would you like to reschedule?

Customer: Yes, let's do the test drive.

Salesperson: This car is a second-owner vehicle. Do you plan to use it daily? What's your expected mileage?

Customer: Around 10 km per liter.

Salesperson: This car has an 8.8-liter engine, so you might need to spend a bit more on fuel.

Customer: That's fine. Is the car non-tampered?

Salesperson: No, it has been tampered with, but it has undergone company service.

Customer: How can I proceed with this vehicle?

Salesperson: The vehicle is already booked. If it goes live, you can book it immediately. The booking amount ranges from 10k to 25k.

Customer: No one informed me about this. Next time, please notify me when it goes live.

Salesperson: Certainly, sir. Navin will contact you once it's live.

Customer: What is FC?

Salesperson: FC stands for Fitness Certificate. For petrol cars, it's valid for 15 years. Navin will provide more details.

Customer: Is this car roadworthy?

Salesperson: Yes, but it has been modified. The bonnet has been altered.

Customer: Okay.

Salesperson: Once you receive the original RC card, you can transfer ownership. Currently, the RC card hasn't been generated. It usually takes about 90 days for the transfer process.

Customer: 90 days?

Salesperson: Yes, sir. It might take up to 50 days in some cases. Have you filed your ITR?

Customer: Yes, I have.

Salesperson: Great. Make sure to update your finishing details.

Customer: Okay, will do.

Salesperson: If the vehicle goes live, you can book it immediately. If it's not live, it might be booked for up to 3 days. If the current holder cancels, you'll be notified right away. You can book it online for Rs. 10,000. Once the payment is made, our finance team will contact you for further details. If the loan isn't approved, you can decide how to proceed.

Customer: Understood. Thank you for the information.

Salesperson: You're welcome, sir. Have a great day!
"""
# for conv9.txt in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
