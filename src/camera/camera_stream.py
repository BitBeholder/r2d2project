import cv2

def get_video_capture():
    # Initialize the video capture object.
    # The argument '0' gets the default camera, but you might need to change it depending on your setup.
    cap = cv2.VideoCapture(0)

    # Set camera properties, if necessary (e.g., cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)).
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()
    
    return cap

def release_video_capture(cap):
    # Release the video capture object.
    cap.release()
    cv2.destroyAllWindows()

def main():
    cap = get_video_capture()

    try:
        while True:
            # Capture frame-by-frame.
            ret, frame = cap.read()

            # If frame is read correctly, ret is True.
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break
                
            frame_resized = cv2.resize(frame, (960, 540))

            # Here, you can process the frame if you want.
            # For example, displaying it:
            cv2.imshow('Resized Frame', frame_resized)

            # Press 'q' to exit the loop.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        release_video_capture(cap)

if __name__ == '__main__':
    main()
