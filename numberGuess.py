import streamlit as st
import random
from streamlit_extras.let_it_rain import rain


st.set_page_config(page_title="Number Guessing Game", layout="centered")

# Styling
st.markdown(""" 
    <style>
        .stButton>button {
            font-size:18px;
            padding:10px 25px;
            border-radius:12px;
        }
        .stNumberInput input{
            font-size:20px;
            text-align:center;
        }
    </style>        
""", unsafe_allow_html=True)

# Title and instructions
st.title("🎯 Number Guessing Game")
st.subheader("Guess the secret number between 1 and 50")

# Difficulty select
difficulty = st.selectbox("Select Difficulty Level:", ['😌 Easy (10 tries)', '🔥 Hard (5 tries)'])
max_attempts = 10 if "Easy" in difficulty else 5

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.result = ""

# Remaining attempts & progress
remaining = max_attempts - st.session_state.attempts
progress = st.progress(st.session_state.attempts / max_attempts)

# Game logic
if not st.session_state.game_over:
    st.markdown(f"🕒 Attempts left: **{remaining}** / {max_attempts}")
    guess = st.number_input("👇 Enter your guess:", min_value=1, max_value=50, step=1, key='guess')

    if st.button("✔ Submit Guess"):
        st.session_state.attempts += 1
        progress.progress(st.session_state.attempts / max_attempts)

        if guess == st.session_state.secret_number:
            st.success(f"🎉 You guessed it in {st.session_state.attempts} tries! The number was {st.session_state.secret_number}.")
            st.session_state.game_over = True
            st.session_state.result = "win"
            rain(emoji="🎊", font_size=54, falling_speed=5, animation_length="infinite")
        elif guess < st.session_state.secret_number:
            st.session_state.message = "🔼 Too low! Try a higher number."
        else:
            st.session_state.message = "🔽 Too high! Try a lower number."

        if st.session_state.attempts >= max_attempts and not st.session_state.game_over:
            st.error(f"💀 Game Over! The correct number was {st.session_state.secret_number}.")
            st.session_state.game_over = True
            st.session_state.result = "lose"

    st.write(st.session_state.message)

# Play again button
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        st.session_state.secret_number = random.randint(1, 50)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.result = ""
        progress.progress(0)
