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

#

