# FashionFindr online shopping assistant bot

FashionFindr is an AI-powered online shopping assistant built with Streamlit that helps users discover relevant products from a curated dress catalog. The assistant is strictly constrained to the provided catalog, ensuring accurate, reliable, and hallucination-free responses.

This project showcases prompt engineering, catalog-based retrieval, and the development of an interactive LLM-powered web application.

Features:

 - Conversational shopping assistant (FashionFindr )
 - Retrieves relevant products from a dress catalog based on Amazon.com listings
 - Strictly constrained to catalog data (no hallucinations)
 - Prompt-engineered system role for controlled responses 
 - Streamlit-based chat UI 
 - Uses OpenRouter-compatible OpenAI client
 - Powered by Solar Pro 3 model via OpenRouter

Model Details
- Provider: OpenRouter
- Model: Solar Pro 3
- Usage: LLM response generation for catalog-based conversational shopping
- Reason for Selection: Fast, cost-free inference suitable for lightweight conversational applications


Project Structure:
- data/
  - product_1.txt
  - product_2.txt
- bot.py
- main.py
- requirements.txt
- README.md

For data/

Each file represents one product:

First line: Product title

Remaining lines: Product description


How It Works
1. Catalog Loading

- bot.py reads all product files from the data/ directory.

- Builds a catalog dictionary mapping product titles to their descriptions.

2. Prompt Construction

- A system prompt defines Alex as an online shopping assistant.

- The entire product catalog is injected into the prompt.

- The assistant is explicitly instructed not to respond outside the provided catalog.

3. LLM Response Generation

- User messages are combined with the system prompt.

 - Responses are generated using the xiaomi/mimo-v2-flash:free model via OpenRouter.

4. Streamlit Interface

- main.py provides a chat-based user interface.

- Streamlit session state maintains conversation history.

- Messages are rendered using streamlit-chat.


Tech Stack

- Python

- Streamlit

- OpenAI / OpenRouter API
- OpenAI-compatible client
- LLM Prompt Engineering

- streamlit-chat


Installation Steps

Clone the repository:

- git clone https://github.com/your-username/alex-shopping-assistant.git
cd alex-shopping-assistant
- Install dependencies
- Set your API key
- Running the App
streamlit run main.py



Examples:

“I’m looking for a new year's party dress.”  
“Do you have a suitable dress that I can wear to my friend's birthday party?”  
FashionFindr will only respond with products that exist in the catalog.


Design Constraints

The assistant cannot:
- Recommend products not in the catalog
- Answer non-shopping-related questions
- Provide external fashion advice  
   -- This ensures safe, reliable, and controlled responses.

Future Improvements:

- Integrate vector embeddings for semantic product search
- Expand support to additional product categories beyond dresses
- Add category and price-based filtering
-Incorporate product images for richer browsing
-Enable multi-catalog support
-Introduce user personalization and preference tracking

References

- Dress and sweater product data based on listings from Amazon.com
- Xiaomi: MiMo-V2-Flash model via OpenRouter: https://openrouter.ai/xiaomi/mimo-v2-flash:free
