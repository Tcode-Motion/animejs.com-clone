import cv2
import os

# Path to the video file
video_path = r"C:\Users\tanmoy\Documents\animejs.com\assets\videos\learn-animejs-course-teaser.mp4"
output_dir = r"C:\Users\tanmoy\Documents\animejs.com\extracted_frames"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Video Properties:")
print(f"  Duration: {duration:.2f} seconds")
print(f"  FPS: {fps:.2f}")
print(f"  Total Frames: {total_frames}")
print(f"  Resolution: {width}x{height}")
print()

# Extract 20 frames evenly distributed throughout the video
num_frames_to_extract = 20
frame_interval = total_frames // (num_frames_to_extract + 1)

extracted_count = 0
for i in range(1, num_frames_to_extract + 1):
    frame_number = i * frame_interval
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    ret, frame = cap.read()
    if ret:
        timestamp = frame_number / fps
        output_path = os.path.join(output_dir, f"frame_{i:03d}_t{timestamp:.2f}s.png")
        cv2.imwrite(output_path, frame)
        extracted_count += 1
        print(f"Extracted frame {i}/{num_frames_to_extract} at {timestamp:.2f}s -> {output_path}")
    else:
        print(f"Failed to extract frame {i}")

cap.release()
print(f"\nSuccessfully extracted {extracted_count} frames to {output_dir}")
