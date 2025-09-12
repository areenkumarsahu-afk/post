import streamlit as st 
import requests

st.set_page_config(page_title="AI Chatbot Demo",page_icon="🤖",layout="wide")

st.image("brand-1.jpg",width=150)
st.title("Demo: AI Assistant for Your Business")
st.markdown("Demo Version - Token usage is limited by your demo token.")
st.markdown("This is a demo showcase. Contact us to unlock unlimited chats, training on your data, and full customization!")

BASE_URL="https://backend-svlu.onrender.com"

query_params=st.query_params
token=query_params.get("token")

if not token:
    st.error("No token provided. Use the demo link with a token.")
else:
    user_input=st.chat_input("Ask me something...")
    if user_input:
        try:
            resp=requests.post(f"{BASE_URL}/ask",json={"token":token,"question":user_input})
            if resp.status_code==200:
                try:
                    data=resp.json()
                    answer=data["answer"]
                    tokens_remaining=data.get("tokens_remaining")
                    st.chat_message("assistant").write(answer)
                    if tokens_remaining is not None:
                        st.info(f"Remaining tokens:{tokens_remaining}")
                except Exception:
                    st.error("Backend returned invalid JSON.")
                    st.text(resp.text)
            else:
                try:
                    error_detail=resp.json().get('detail','Unknown error')
                except Exception:
                    error_detail=resp.text
                st.error(f"{error_detail}")
                try:
                    if resp.json().get('tokens_remaining')==0:
                        st.markdown("---")
                        st.markdown("👉[DM us on Instagram](https://instagram.com/chatalystai)")
                        st.markdown("👉 Or fill our [Email Form](https://docs.google.com/forms/d/e/1FAIpQLSdcsHT1ixLwIZhI7bJrMBWDUNhinEMouq6USDb_9ERre7sIaw/viewform?usp=dialog)")
                        st.markdown("👉 Learn more on our [Notion Page](https://www.notion.so/AI-Chatbots-That-Work-While-You-Sleep-245eb1fcbdfb80678680f57248d685c8?source=copy_link)")
                except Exception:
                    pass
        except Exception:
            st.error("Request failed.")






