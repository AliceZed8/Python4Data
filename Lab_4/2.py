from argparse import ArgumentParser
from moviepy.editor import VideoFileClip
import math

parser = ArgumentParser()
parser.add_argument("--input", required=True, type = str)
parser.add_argument("--start", required=True, type = int)
parser.add_argument("--end", required= True, type = int)
parser.add_argument("--out_dir", required=True, type = str)
parser.add_argument("--step",   type=int, default=10)


args = parser.parse_args()

video = VideoFileClip(args.input)
video = video.resize( (16 * 250/ math.sqrt(337), 9 * 250 / math.sqrt(337)) )



diff = args.step / video.fps

pos = args.start
fileNum = 0
while pos < args.end:
    filename = args.out_dir + "/" + f"{fileNum}.png"
    video.save_frame(filename, pos)
    print(f"Frame at {pos} sec ({filename})")

    pos += diff;
    fileNum += 1;

