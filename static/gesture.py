import cv2
import dlib
import time
from home import views

# Load the facial landmark predictor
predictor = dlib.shape_predictor(r"D:\1_myProjects\smartHire\static\tooba\shape_predictor_68_face_landmarks.dat")
# Replace "path/to/shape_predictor_68_face_landmarks.dat" with the actual path to the file.

def draw_no_face_message(frame, face_not_detected_count):
    # Draw a message indicating no face detected
    no_face_message = "No Face Detected"
    cv2.putText(frame, no_face_message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Faces Not Detected: {face_not_detected_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def is_eyebrows_raised(landmarks):
    # Define conditions for raised eyebrows gesture
    left_eyebrow_points = [21, 22, 23, 24, 25, 26]
    right_eyebrow_points = [17, 18, 19, 20, 21]
    left_eyebrow_height = sum(landmarks[point][1] for point in left_eyebrow_points) / len(left_eyebrow_points)
    right_eyebrow_height = sum(landmarks[point][1] for point in right_eyebrow_points) / len(right_eyebrow_points)
    return left_eyebrow_height < 160 and right_eyebrow_height < 160

def is_confused(landmarks):
    # Define conditions for confusion gesture (wide-open mouth)
    mouth_points = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    mouth_open_threshold = 15  # Threshold for mouth open detection

    mouth_open_distance = landmarks[66][1] - landmarks[62][1]
    return mouth_open_distance > mouth_open_threshold


def generate_frames():
    global score
    score = views.s  # Initialize score

    # Start time for the 10-minute timer
    start_time = time.time()

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_not_detected_count = 0
    confusion_counter = 0
    eyebrows_raised_counter = 0

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        # Perform face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


        if len(faces) == 0:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 180:  # 600 seconds = 10 minutes
                score = 0

            face_not_detected_count += 1
            if face_not_detected_count >= 20:
                if score <= 0:
                    score = 0
                else:
                    score -= 0.01  # Subtract 0.5 from score if no face detected after 5 consecutive frames
            draw_no_face_message(frame, face_not_detected_count)
        else:
            face_not_detected_count = 0

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Detect facial landmarks
                shape = predictor(gray_frame, dlib.rectangle(x, y, x+w, y+h))
                landmarks = [(shape.part(i).x, shape.part(i).y) for i in range(shape.num_parts)]

                if is_eyebrows_raised(landmarks):
                    eyebrows_raised_counter += 1
                else:
                    eyebrows_raised_counter = 0

                if eyebrows_raised_counter >= 3:
                    if score <= 0:
                        score = 0
                    else:
                        score -= 0.3  # Subtract 0.5 from score if raised eyebrows gesture detected for 5 consecutive frames
                    eyebrows_raised_counter = 0

                if is_confused(landmarks):
                    confusion_counter += 1
                else:
                    confusion_counter = 0

                if confusion_counter >= 6:
                    if score <= 0:
                        score = 0
                    else:
                        score -= 0.3  # Subtract 0.5 from score if confusion gesture detected for 5 consecutive frames
                    confusion_counter = 0

                cv2.putText(frame, "FACE DETECTED" , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        
        # elapsed_time = time.time() - start_time
        # if elapsed_time >= 120:  # 600 seconds = 10 minutes
        #     score = 0



        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n\r\n')
    cap.release()