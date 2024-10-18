import os
import pickle
import mediapipe as mp
import cv2

# Initialize mediapipe solutions
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Hands solution instance
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.1)  # Lower confidence

# Data directory
DATA_DIR = './data'

data = []
labels = []

# Supported image extensions
valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')

for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    
    if os.path.isdir(dir_path):  # Ensure it's a valid directory
        for img_path in os.listdir(dir_path):
            if img_path.endswith(valid_extensions):  # Process only valid image files
                data_aux = []
                x_ = []
                y_ = []

                # Load and process image
                img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
                
                if img is not None:  # Check if the image was loaded correctly
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    # Resize the image (optional, depending on your image size)
                    img_rgb = cv2.resize(img_rgb, (480, 480))

                    # Process image to find hand landmarks
                    results = hands.process(img_rgb)
                    
                    if results.multi_hand_landmarks:  # If hand landmarks were detected
                        for hand_landmarks in results.multi_hand_landmarks:
                            mp_drawing.draw_landmarks(img_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Visualize landmarks
                            
                            for i in range(len(hand_landmarks.landmark)):
                                x = hand_landmarks.landmark[i].x
                                y = hand_landmarks.landmark[i].y

                                x_.append(x)
                                y_.append(y)

                            # Normalize landmark coordinates relative to the minimum x and y
                            for i in range(len(hand_landmarks.landmark)):
                                x = hand_landmarks.landmark[i].x
                                y = hand_landmarks.landmark[i].y
                                data_aux.append(x - min(x_))
                                data_aux.append(y - min(y_))

                        # Store processed data and labels
                        data.append(data_aux)
                        labels.append(dir_)

                        # Display the image with landmarks
                        cv2.imshow("Hand Landmarks", img_rgb)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                    else:
                        print(f"No hand landmarks detected in image: {img_path}")
                else:
                    print(f"Failed to load image: {img_path}")
            else:
                print(f"Skipping non-image file: {img_path}")

# Save data to a pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("Data processing complete. Saved to 'data.pickle'.")
