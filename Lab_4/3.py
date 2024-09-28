from argparse import ArgumentParser
from pathlib import Path
import cv2

parser = ArgumentParser()
parser.add_argument("--input", required=True, type = str)

args = parser.parse_args()

cap = cv2.VideoCapture(args.input)
if not cap.isOpened():
    print(f"Failed to open videofile {args.input}")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

filename = Path(args.input).name


font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 0.5
font_color = (255, 255, 255)
thickness = 1

i = 0
while True:
    ret, frame = cap.read()
    if (not ret): break
    
    cv2.putText(frame, f"Filename: {filename}", (0,20), font, font_scale, font_color, thickness)
    cv2.putText(frame, f"Fps: {fps}", (0, 40), font, font_scale, font_color, thickness)
    cv2.putText(frame, f"Size: {frame_width}x{frame_height}", (0, 60), font, font_scale, font_color, thickness)
    cv2.putText(frame, f"Duration: {frame_count/fps} sec", (0,80), font, font_scale, font_color, thickness)
    cv2.putText(frame, f"Frame at {round(i/fps, 2)} sec.", (0, 100), font, font_scale, font_color, thickness)
    
    cv2.imshow("Video", frame)
    i += 1

    k = cv2.waitKey(int(fps))
    if (k == ord("q")): break



cap.release()
cv2.destroyAllWindows()
