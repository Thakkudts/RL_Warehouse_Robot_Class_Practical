import streamlit as st
import joblib

st.set_page_config(
    page_title="Smart Warehouse Robot",
    page_icon="🤖"
)

st.title("🤖 Smart Warehouse Robot")
st.write("Q-Learning based warehouse navigation")

Q = joblib.load("q_learning_model.joblib")

actions = {
    0: "LEFT",
    1: "RIGHT",
    2: "UP",
    3: "DOWN"
}

st.subheader("Warehouse")

st.write("""
**S0 | S1 | S2 | S3**

**S4 | S5 | S6 | S7**

**S8 | S9 | S10 | S11**

**S12 | S13 | S14 | 🟢 GOAL**
""")

state = st.number_input(
    "Enter the current state:",
    min_value=0,
    max_value=15,
    value=0,
    step=1
)

if st.button("Find Best Action"):

    best_action_number = Q[state].argmax()

    best_action = actions[best_action_number]

    st.success(
        f"Best action for State {state} is **{best_action}**"
    )

    st.subheader("Q-Values")

    st.write(f"LEFT  : {Q[state][0]:.2f}")
    st.write(f"RIGHT : {Q[state][1]:.2f}")
    st.write(f"UP    : {Q[state][2]:.2f}")
    st.write(f"DOWN  : {Q[state][3]:.2f}")
