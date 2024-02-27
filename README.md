# Facial-Recognition-Based-Attendance-System
An attendance management system utilizing face recognition technology. This Python script captures video from a webcam, detects faces, matches them with known faces, and records attendance with timestamps in a CSV file. The system is designed for simplicity and efficiency, providing an automated solution for tracking attendance in various settings.

## Installation

1. Clone the repository.
2. Install the required packages:pip install -r requirements.txt
3. Press 'q' to exit the application.

## Usage

1. Make sure your webcam is connected to your computer.
2. Run the script: python attendance_system.py

## Known Faces

You need to provide images of known faces in the `photos` directory. Follow the example provided in the `load_known_faces` function in `attendance_system.py` to load known faces and their encodings.

## Output

The attendance records are saved in CSV files named according to the date of attendance.

## License

This project is licensed under the MIT License.
