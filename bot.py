import os
files = os.listdir("./data")

catalog= {}
for file in files:
    file=os.path.join("./data", file)
    data=open(file).readlines()
    title=data[0]
    description="\n".join(d for d in data[1:])
    catalog[title]=description
    
few_shot_examples = """

Example 1:
User: Can you recommend some V neck dress from the catalog?
Assistant: Of course! Here are some V-neck dresses from our catalog:
- product title: Bebonnie Womens Sexy V Neck Batwing Sleeve Sparkly Cocktail Party Sweater Dresses Holiday Bodycon Midi Dress
  details: Features a V-neckline and comes in sizes XS to XL. It is a sparkly, bodycon midi dress perfect for parties and special events.
- product title: oten Womens Deep V Neck Ruffle Sleeve Sheath Casual Cocktail Party Work Faux Wrap Dress
  details: This dress has a deep V-neck with ruffle decor and is designed for various occasions, including work, parties, and casual outings. It is made from a stretchy polyester and spandex blend.

Example 2:
User: I want a sleeveless dress I can wear to Cocktail party
Assistant: Of course! Based on our catalog, here is a sleeveless dress that would be perfect for a cocktail party:
- product title: BABEYOND 1920s Flapper Dress Gatsby Fringed Dress Roaring 20s
  details:  This is a sleeveless, bodycon fitted midi dress with a dazzling embellished art deco design featuring fringe, beads, and sequins. It is specifically recommended for cocktail parties, proms, and evening events.

Example 3:
User: What sizes do you have for the sparkly dress?
Assistant: Of course! Here are the size details for the sparkly dresses we have in the catalog:
- product title: Sparkly Outfits for Women, One Shoulder Ruched Bodycon Short Prom Dress
  details: XS=US 00, S=US 0-2, M=US 4-6, L=US 8-10, XL=US 12
There is also another sparkly dress in our catalog:
- product title: 
Bebonnie Womens Sexy V Neck Batwing Sleeve Sparkly Cocktail Party Sweater Dresses Holiday Bodycon Midi Dress
For the "Sparkly Outfits for Women" short one-shoulder dress:
  details: Bust Size: XS 31.9", S 33.9", M 35.8", L 38.6", XL 42.1"
"""
few_shot_examples2 = """

Here are a few examples.
Example 1:
User: I am looking for a sparkly dress
Assistant: Do you have any color or fit preference?
User: Show me all the sparkly dresses you have.
Assistant: I found three sparkly dresses for you. 
- Jessica women dress
- Berry long sweater dress
- Boho maxi dress
Let me know which dress you want more details about. I can get it for you.
User: I have a budget of $20.
Assistant: You can buy the Boho maxi dress since it is $16 which meets your budget. Would you like to view more details about this dress?
User: No. Thank you so much for helping. That's all I needed.
Assistant: No problem! Feel free to come back if you need any help.

Example 2:
User: I am looking for a dress
Assistant: Do you prefer a particular style or is it for any occassion?
User: Cocktail party
Assistant: What's your budget?
User: Below $40
Assistant: Got it. Here are my top picks.
- Hollypick lace dress 
- Pretty Garden shoulder bodycon dress
User: Thank you. You have been a great help
Assistant: No problem! Feel free to come back if you need any help.

Example 3:
User: I am looking for a sweater
Assistant: Do you have a budget in mind?
User: Below $10
Assistant: Sorry, there are no sweaters within the $10 budget. Would you increase it?
User: What is the cheapest one you have?
Assistant: We have trendy queen oversized crewneck sweater that is $40. Are you interested in that one?
User: No
Assistant: Alright. Let me know if there is anything I can help you with. 
User: No, I'm good. Thanks
Assistant: No problem! Feel free to come back if you need any help.
"""


prompt="You are a online shopping assistant FashionFindr. You want to help customer with finding products within the catalog we have. Be concise with your responses, don't reveal all the product details at once. Always ask follow up questions to gain enough clarity before providing suggestions."
prompt+="Here is a catalog: "
for title,description in catalog.items():
    prompt+= f"product title: {title}\n details: {description}\n\n"
prompt += few_shot_examples2
prompt+="DO NOT ANSWER ANYTHING BEYOND SHOPPING. DO NOT GIVE ANY INFORMATION APART FROM CATALOG THAT IS PROVIDED TO YOU"
model="upstage/solar-pro-3:free"

def respond(client, messages):
    messages = [{"role": "system", "content": prompt}] + messages
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in messages
        ],
        stream=False,
    )
    return stream
