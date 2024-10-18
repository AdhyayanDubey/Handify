
# Handify: Sign Language Recognition System

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Data Collection](#data-collection)
- [Data Processing](#data-processing)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

## Introduction
**Handify** is a Sign Language Recognition System that utilizes computer vision and machine learning to recognize and translate sign language gestures into text. The project aims to bridge communication gaps for individuals who are deaf or hard of hearing.

## Problem Statement
Sign language is often misunderstood or misinterpreted by those unfamiliar with it. Handify seeks to improve communication and accessibility for individuals using sign language by providing an intuitive recognition system.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - OpenCV
  - MediaPipe
  - Scikit-learn
  - Pickle
- **Development Environment**: Local machine with Python installed

## Installation
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Handify
   ```
2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe scikit-learn
   ```

## Usage
1. **Data Collection**: Use the provided script to collect hand gesture images through your webcam.
2. **Data Processing**: Run the script to process the collected images and extract hand landmarks.
3. **Model Training**: Train a machine learning model to classify the gestures based on the processed data.
4. **Recognition**: Implement real-time gesture recognition using the trained model.

## Code Structure
```
Handify/
│
├── data/                     # Directory for storing collected images
│   ├── 0/                    # Class 0 images
│   ├── 1/                    # Class 1 images
│   └── 2/                    # Class 2 images
│
├── data_collection.py        # Script for collecting data
├── data_processing.py         # Script for processing collected data
└── model.py                  # Script for training and recognition
```

## Data Collection
The `data_collection.py` script captures images of hand gestures using the webcam. It saves the images in separate folders based on the gesture class.

## Data Processing
The `data_processing.py` script processes the captured images using MediaPipe to extract hand landmarks. The landmarks are normalized and saved in a pickle file for training.

## Future Enhancements
- Improve model accuracy by increasing the dataset size and incorporating more gestures.
- Implement real-time gesture recognition using a trained model for instant feedback.
- Expand to support multiple sign languages.

## Contributors
- [AdhyayanDubey] - https://github.com/AdhyayanDubey
- [Vinamra Srivastava] - https://github.com/VinamraSrivastava-0
- [vansh jain] - https://github.com/vanshjain07

