import cv2
import mediapipe as mp
import random

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to classify hand gesture
def classify_gesture(landmarks):
    thumb_is_open = landmarks[4].x < landmarks[3].x
    index_is_open = landmarks[8].y < landmarks[6].y
    middle_is_open = landmarks[12].y < landmarks[10].y
    ring_is_open = landmarks[16].y < landmarks[14].y
    pinky_is_open = landmarks[20].y < landmarks[18].y

    if all([thumb_is_open, index_is_open, middle_is_open, ring_is_open, pinky_is_open]):
        return "paper"
    elif all([index_is_open, middle_is_open]) and not any([ring_is_open, pinky_is_open]):
        return "scissors"
    elif not any([thumb_is_open, index_is_open, middle_is_open, ring_is_open, pinky_is_open]):
        return "rock"
    else:
        return None

# Function to get computer move
def get_computer_move():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'scissors' and computer_move == 'paper') or \
         (player_move == 'paper' and computer_move == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    results = hands.process(rgb_frame)
    
    player_move = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            player_move = classify_gesture(hand_landmarks.landmark)
    
    # Display player move
    if player_move:
        computer_move = get_computer_move()
        result = determine_winner(player_move, computer_move)
        
        cv2.putText(frame, f"Your Move: {player_move}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Computer Move: {computer_move}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, result, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if result == "You win!" else (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Make a move: Rock, Paper, or Scissors", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Display the frame
    cv2.imshow('Rock-Paper-Scissors Game', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
