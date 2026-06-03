def get_clean_input():
    raw_input = input("You:")
    clean_input = raw_input.strip().lower()
    return clean_input
    #returns sanitized and normalised string
def process_intent(user_input):
    
    information = {
        "hello": "Welcome to DecodeLabs Support. How can I assist you today?",
        "hours": "Our digital systems are operational 24/7. Human engineering support is active Monday-Friday, 9 AM - 6 PM IST.",
        "location": "Our primary digital development hub is located in Greater Lucknow, India.",
        "services": "We offer elite AI Engineering training, Full-Stack AI Development pipelines, and custom automation deployment.",
        "status": "All core routing engines and LLM gateways are operating at 100% efficiency."
    }
    response = information.get(user_input, "ROUTE_TO_LLM" )

    return response
if __name__ == "__main__" :

    print("--- Sanitization Engine Active ---")

    processed_text = get_clean_input()

    system_reply = process_intent(processed_text)

    print(f"System response:{system_reply}")