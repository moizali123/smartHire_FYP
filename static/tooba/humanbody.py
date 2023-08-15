import cv2
import time

# Defining a function bodyMovementDetection
def bodyMovementDetection():
    # capturing video in real time
    cap = cv2.VideoCapture(0)

    # reading frames sequentially
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    # Initialize the Background Subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=25, detectShadows=False)

    score = 25  # Initialize score

    # Start time for the 2-minute timer
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Apply background subtraction to get the foreground mask
        fg_mask = bg_subtractor.apply(frame)

        # Clean up the mask (remove noise and shadows)
        fg_mask = cv2.erode(fg_mask, None, iterations=2)
        fg_mask = cv2.dilate(fg_mask, None, iterations=2)

        # Find contours in the mask
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        labels = []  # List to store labels for each motion region

        for contour in contours:
            if cv2.contourArea(contour) < 900:
                continue
            
            # Draw a bounding box around the movement area
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "BODY MOVEMENT DETECTED", (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)
            
            label = "Motion Region {}".format(len(labels) + 1)  # Generate label
            labels.append(label)  # Add label to the list
            cv2.putText(frame, "STATUS: {}".format(label), (10, 90), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        num_regions = len(labels)  # Number of motion regions detected

        if num_regions > 8:
            score -= 2  # Subtract 2 from score if more than 10 motion regions
        
        cv2.putText(frame, "SCORE: {}".format(score), (10, 120), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        cv2.imshow("Video", frame)

        # Check for key press
        key = cv2.waitKey(50)
        if key == 27 or key == ord('q'):  # 'Esc' key or 'q' key to quit
            break

        # Check if 2 minutes have passed without any motion detection
        elapsed_time = time.time() - start_time
        if elapsed_time >= 120:  # 120 seconds = 2 minutes
            score = 0
            print("No motion regions detected for 2 minutes. Stopping the process.")
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Final Score:", score)  # Print the final score after the while loop


if __name__ == "__main__":
    bodyMovementDetection()
