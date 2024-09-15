# A simple dictionary of predefined questions and answers
faq_responses = {
    "return policy": "Our return policy allows you to return items within 30 days of purchase.",
    "shipping time": "Shipping usually takes 5-7 business days depending on your location.",
    "payment methods": "We accept Visa, Mastercard, PayPal, and Apple Pay.",
    "track my order": "You can track your order by logging into your account and checking the 'Orders' section.",
    "contact support": "You can contact our customer support via email at support@company.com."
}

def get_response(user_input):
    """
    A simple function that takes a user input, looks for keywords,
    and returns a predefined response.
    """
    user_input = user_input.lower()
    
    # Search for keywords in the input and return an appropriate response
    for keyword, response in faq_responses.items():
        if user_input in keyword :
            return response
    
    return "I'm sorry, I don't understand your question. Please try asking something else."
