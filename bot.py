def get_clean_input():
    #This function is for sanitising and normalising the user input
    raw_input = input("You:")
    clean_input = raw_input.strip().lower()
    return clean_input
    #returns sanitized and normalised string
def process_intent(user_input):
    # creating the database for O(1)lookup instead of unstable if-elif ladder
    information = {
        "hello": "Welcome to DecodeLabs Support. How can I assist you today?",
        "hours": "Our digital systems are operational 24/7. Human engineering support is active Monday-Friday, 9 AM - 6 PM IST.",
        "location": "Our primary digital development hub is located in Greater Lucknow, India.",
        "services": "We offer elite AI Engineering training, Full-Stack AI Development pipelines, and custom automation deployment.",
        "status": "All core routing engines and LLM gateways are operating at 100% efficiency."
    }
    response = information.get(user_input, "ROUTE_TO_LLM" )
    #.get() key checks the dictionary without loops
    return response
if __name__ == "__main__" :
    print("=============================================")
    print("--- INDUSTRIAL AI HYBRID CORE ACTIVATED ---")
    print("  Type your questions below. Type 'exit' to quit. ")
    print("=============================================")

    #While loop for continuous cycle
    while True :
        # cleaning user input
        processed_text = get_clean_input()

        # Check for the kill command
        if processed_text == "exit" :
            print("Shutting down core engine down safely. Goodbye.")
            break
            #break instantly stops the loop and exits the script cleanly if kill command is given
        
        #Checking the databse for answer or gives fallback answer if nothing matches
        system_reply = process_intent(processed_text)
        
        #OUTPUT
        print(f"Bot:{system_reply}\n")