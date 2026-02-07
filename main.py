import streamlit as st
from openai import OpenAI
from bot import respond
from streamlit_chat import message as print_message
import uuid
import os

st.title("Online Shopping Assistant")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),base_url="https://openrouter.ai/api/v1")

#if "openai_model" not in st.session_state:
 #   st.session_state["openai_model"] = "qwen/qwen3-coder:free"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm FashionFindr, your online shopping assistant. How can I help you today?"}]

if "max_messages" not in st.session_state:
    # Counting both user and assistant messages, so 10 rounds of conversation
    st.session_state.max_messages = 50

for message in st.session_state.messages:
#   with st.chat_message(message["role"]):
#       st.markdown(message["content"])
    user=True if message["role"] == "user" else False
    if user:
        avatar="personas"
    else:
        avatar="fun-emoji"
    print_message(message["content"].replace("$", "\$"), is_user=user, key=uuid.uuid4().hex, avatar_style=avatar,allow_html=True)
else:
    if prompt := st.chat_input("How can I help you today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
#        with st.chat_message("user"):
#            st.markdown(prompt)
        print_message(prompt.replace("$", "\$"),is_user=True, key=uuid.uuid4().hex,avatar_style="personas",allow_html=True)
#        with st.chat_message("assistant"):

        try:
            stream=respond(client,st.session_state.messages)
            #response = st.write_stream(stream)
            response=stream.choices[0].message.content
            response+="<br><br>"
            print_message(response.replace("$", "\$"), key=uuid.uuid4().hex, avatar_style="fun-emoji",allow_html=True)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
        except Exception as e:
            print(e)
            st.session_state.max_messages = len(st.session_state.messages)
            rate_limit_message = """
                I'm having technical issues. Please check back again later. 
            """
            st.session_state.messages.append(
                {"role": "assistant", "content": rate_limit_message}
            )
            st.rerun()

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    if selected == 1:
        st.markdown("Thank you for your feedback. We're glad this was helpful.")
    else:
        st.markdown("Thank you for your feedback. We'll use it to improve your experience.")
