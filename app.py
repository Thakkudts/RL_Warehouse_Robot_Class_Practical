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

next_state = {
    0:  {"LEFT": 0,  "RIGHT": 1,  "UP": 0,  "DOWN": 4},
    1:  {"LEFT": 0,  "RIGHT": 2,  "UP": 1,  "DOWN": 5},
    2:  {"LEFT": 1,  "RIGHT": 3,  "UP": 2,  "DOWN": 6},
    3:  {"LEFT": 2,  "RIGHT": 3,  "UP": 3,  "DOWN": 7},

    4:  {"LEFT": 4,  "RIGHT": 5,  "UP": 0,  "DOWN": 8},
    5:  {"LEFT": 4,  "RIGHT": 6,  "UP": 1,  "DOWN": 9},
    6:  {"LEFT": 5,  "RIGHT": 7,  "UP": 2,  "DOWN": 10},
    7:  {"LEFT": 6,  "RIGHT": 7,  "UP": 3,  "DOWN": 11},

    8:  {"LEFT": 8,  "RIGHT": 9,  "UP": 4,  "DOWN": 12},
    9:  {"LEFT": 8,  "RIGHT": 10, "UP": 5,  "DOWN": 13},
    10: {"LEFT": 9,  "RIGHT": 11, "UP": 6,  "DOWN": 14},
    11: {"LEFT": 10, "RIGHT": 11, "UP": 7, "DOWN": 15},

    12: {"LEFT": 12, "RIGHT": 13, "UP": 8,  "DOWN": 12},
    13: {"LEFT": 12, "RIGHT": 14, "UP": 9, "DOWN": 13},
    14: {"LEFT": 13, "RIGHT": 15, "UP": 10, "DOWN": 14},
    15: {"LEFT": 15, "RIGHT": 15, "UP": 15, "DOWN": 15}
}

state = st.number_input(
    "Enter starting state:",
    min_value=0,
    max_value=15,
    value=0,
    step=1
)

if st.button("Find Full Path to Goal"):

    state = int(state)

    if state == 15:
        st.success("🎯 The robot is already at the GOAL!")

    else:
        current_state = state
        path = [current_state]
        action_path = []

        visited = set()

        while current_state != 15 and current_state not in visited:

            visited.add(current_state)

            best_action_number = int(Q[current_state].argmax())
            best_action = actions[best_action_number]

            action_path.append(best_action)

            current_state = next_state[current_state][best_action]

            path.append(current_state)

        st.subheader("🚀 Complete Path")

        path_text = " → ".join(
            [f"S{s}" for s in path]
        )

        st.success(path_text)

        st.subheader("🧭 Actions")

        action_text = " → ".join(action_path)

        st.info(action_text)

        st.subheader("📍 Step-by-Step Route")

        for i in range(len(action_path)):
            st.write(
                f"Step {i + 1}: S{path[i]} "
                f"→ **{action_path[i]}** "
                f"→ S{path[i + 1]}"
            )

        st.subheader("🎯 Goal")

        st.success("Robot reached GOAL (S15)!")
