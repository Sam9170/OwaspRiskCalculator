# Defined the factors and their associated options and ratings

threat_agent_factors = {
    "Skill Level": {"No technical skills": 1, 
                    "Some technical skills": 3, 
                    "Advanced computer user": 5, 
                    "Network and programming skills": 6, 
                    "Security penetration skills": 9},

    "Motive": {"Low or no reward": 1, 
               "Possible reward": 4, 
               "High reward": 9},

    "Opportunity": {"Full access or expensive resources required": 0, 
                    "Special access or resources required": 4, 
                    "Some access or resources required": 7, 
                    "No access or resources required": 9},

    "Size": {"Developers": 2, 
             "System administrators": 2, 
             "Intranet users": 4, 
             "Partners": 5, 
             "Authenticated users": 6, 
             "Anonymous Internet users": 9}
}

vulnerability_factors = {
    "Ease of Discovery": {"Practically impossible": 1, 
                          "Difficult": 3, 
                          "Easy": 7, 
                          "Automated tools available": 9},
    "Ease of Exploit": {"Theoretical": 1, 
                        "Difficult": 3, 
                        "Easy": 5, 
                        "Automated tools available": 9},

    "Awareness": {"Unknown": 1, 
                  "Hidden": 4, 
                  "Obvious": 6, 
                  "Public knowledge": 9},

    "Intrusion Detection": {"Active detection in application": 1, 
                            "Logged and reviewed": 3, 
                            "Logged without review": 8, 
                            "Not logged": 9}
}

technical_impact_factors = {
    "Loss of Confidentiality": {"Minimal non-sensitive data disclosed": 2, 
                                "Minimal critical data disclosed": 6, 
                                "Extensive non-sensitive data disclosed": 6, 
                                "Extensive critical data disclosed": 7, 
                                "All data disclosed": 9},

    "Loss of Integrity": {"Minimal slightly corrupt data": 1, 
                          "Minimal seriously corrupt data": 3, 
                          "Extensive slightly corrupt data": 5, 
                          "Extensive seriously corrupt data": 7, 
                          "All data totally corrupt": 9},

    "Loss of Availability": {"Minimal secondary services interrupted": 1, 
                             "Minimal primary services interrupted": 5, 
                             "Extensive secondary services interrupted": 5, 
                             "Extensive primary services interrupted": 7, 
                             "All services completely lost": 9},

    "Loss of Accountability": {"Fully traceable": 1, 
                               "Possibly traceable": 7, 
                               "Completely anonymous": 9}
}

business_impact_factors = {
    "Financial damage": {"Less than the cost to fix the vulnerability": 1, 
                         "Minor effect on annual profit": 3, 
                         "Significant effect on annual profit": 7, 
                         "Bankruptcy": 9},

    "Reputation damage": {"Minimal damage": 1, 
                          "Loss of major accounts": 4, 
                          "Loss of goodwill": 5, 
                          "Brand damage": 9},

    "Non-compliance": {"Minor violation": 2, 
                       "Clear violation": 5, 
                       "High profile violation": 7},

    "Privacy violation": {"One individual": 3, 
                          "Hundreds of people": 5, 
                          "Thousands of people": 7, 
                          "Millions of people": 9}
}

# Function to collect user input for a factor and validate it
def collect_user_input(factor_name, factor_options):
    while True:
        print(f"Select an option for '{factor_name}':")
        for option, rating in factor_options.items():
            print(f"{option}: {rating}")
        
        selected_option = input()
        
        if selected_option.isdigit() and int(selected_option) in factor_options.values():
            return int(selected_option)
        else:
            print("Invalid option. Please select a valid numeric option.")

# Collect user inputs for threat agent factors
threat_agent_selections = {}
for factor, options in threat_agent_factors.items():
    selected_option = collect_user_input(factor, options)
    threat_agent_selections[factor] = selected_option 

# Collect user inputs for vulnerability factors
vulnerability_selections = {}
for factor, options in vulnerability_factors.items():
    selected_option = collect_user_input(factor, options)
    vulnerability_selections[factor] = selected_option

# Collect user inputs for technical impact factors
technical_impact_selections = {}
for factor, options in technical_impact_factors.items():
    selected_option = collect_user_input(factor, options)
    technical_impact_selections[factor] = selected_option

# Collect user inputs for business impact factors
business_impact_selections = {}
for factor, options in business_impact_factors.items():
    selected_option = collect_user_input(factor, options)
    business_impact_selections[factor] = selected_option

# Function to calculate likelihood and impact scores
def calculate_likelihood_and_impact_score(factors):
    likelihood_score = 1
    impact_score = 1
    for factor, selected_option in factors.items():
        likelihood_score *= selected_option
        impact_score *= selected_option
    return likelihood_score, impact_score

# Calculate likelihood and impact scores separately
likelihood_score = calculate_likelihood_and_impact_score(threat_agent_selections)
impact_score = calculate_likelihood_and_impact_score(vulnerability_selections)


# Determine risk severity
def determine_risk_severity(likelihood_score, impact_score):
    if likelihood_score < 3 or impact_score < 3:
        return "LOW"
    elif likelihood_score <= 3 and impact_score <= 3:
        return "LOW"
    elif (3 < likelihood_score <= 6) or (3 < impact_score <= 6):
        return "MEDIUM"
    else:
        return "HIGH"

# Determine risk severity
risk_severity = determine_risk_severity(likelihood_score[0], impact_score[1])

# Print the results
print("\nRisk Assessment Results:")
print(f"Likelihood Score: {likelihood_score[0]}")
print(f"Impact Score: {impact_score[1]}")
print(f"Risk Severity: {risk_severity}")
