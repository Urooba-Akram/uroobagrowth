import streamlit as st

# App Title
st.set_page_config(page_title="Growth Mindset Project")
st.title("Growth Mindset Challenge: Web App with Streamlit")
# Sidebar
st.header("📌 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.The AI-powered app helps you buld a growth mindset with reflection, challenges and achievement!✵")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write(f"Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill")

st.header("🔧 What's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition

if user_input:
    st.success(f"💪 you re facing: {user_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header(" Reflect on Your Learing")
reflection = st.text_area("write your outcome.!")

if reflection:
    st.success(f" 🌟 Great Insight! Your reflection: {reflection}")
else:
    st.info("Refection on past experience help you grow! Share your difficulties")

#acheivemnt
st.header(" 🏆 Celebrate Your Wins!")
acheivement = st.text_input("Share something you've recently accomplished:")

if acheivement:
    st.success(" ✨ Amazing! you acheived: {acheivement}")
else:
    st.info("Big or small , every acheivement counts!Share one now 😍")

# Footer
st.write("- - -")
st.write("💡 Keep believing in yourself. Growth is a journey, not a destination! ⭐⭐⭐")
st.write(" 🎯 Created by Urooba Akram! ⭐")

# Run command: streamlit run app.py
