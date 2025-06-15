import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Tic Tac Toe - Ishan vs Computer", layout="centered")

# Title
st.title("🎮 Tic Tac Toe - Ishan (X) vs Computer (O)")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Function to check winner
def check_winner():
    b = st.session_state.board
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "":
            return True
        if b[0][i] == b[1][i] == b[2][i] != "":
            return True
    if b[0][0] == b[1][1] == b[2][2] != "":
        return True
    if b[0][2] == b[1][1] == b[2][0] != "":
        return True
    return False

# Function to check draw
def is_draw():
    for row in st.session_state.board:
        if "" in row:
            return False
    return True

# Computer move logic (random available cell)
def computer_move():
    available = [(i, j) for i in range(3) for j in range(3) if st.session_state.board[i][j] == ""]
    if available:
        i, j = random.choice(available)
        st.session_state.board[i][j] = "O"
        if check_winner():
            st.success("💻 Computer (O) wins!")
            st.session_state.game_over = True
        elif is_draw():
            st.info("😐 It's a draw!")
            st.session_state.game_over = True
        else:
            st.session_state.current_player = "X"

# Player move logic
def make_move(i, j):
    if not st.session_state.game_over and st.session_state.board[i][j] == "":
        st.session_state.board[i][j] = "X"
        if check_winner():
            st.success("🎉 You (X) win!")
            st.session_state.game_over = True
        elif is_draw():
            st.info("😐 It's a draw!")
            st.session_state.game_over = True
        else:
            st.session_state.current_player = "O"
            computer_move()

# Draw the game board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        button_label = st.session_state.board[i][j] or " "
        if cols[j].button(button_label, key=f"{i}-{j}", use_container_width=True):
            if st.session_state.current_player == "X":
                make_move(i, j)

# Show current player
if not st.session_state.game_over:
    st.markdown(f"**Current Player:** `{st.session_state.current_player}`")

# Reset button
if st.button("🔁 Reset Game"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
