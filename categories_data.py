# Predefined startup categories with 2 idea examples each
categories = {
    "EdTech": [
        "AI tutor for exam preparation",
        "Interactive platform for coding lessons"
    ],
    "Gig Economy": [
        "App for freelance pet sitters",
        "Uber for personal chefs"
    ],
    "FinTech": [
        "App for managing student loan repayments",
        "Real-time crypto tax calculator"
    ],
    "HealthTech": [
        "Wearable for monitoring sleep disorders",
        "AI diagnosis from skin images"
    ],
    "SaaS": [
        "Subscription-based dashboard for HR analytics",
        "CRM for small-scale legal firms"
    ],
    "ClimateTech": [
        "Solar energy prediction platform",
        "Marketplace for carbon credits"
    ],
    "Marketplaces": [
        "Platform to rent DIY tools locally",
        "Auction site for handmade art"
    ]
}

# Helper to flatten category examples and generate labels
def get_all_examples_and_labels():
    examples = []
    labels = []
    for category, ideas in categories.items():
        for idea in ideas:
            examples.append(idea)
            labels.append(category)
    return examples, labels
