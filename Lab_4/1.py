from argparse import ArgumentParser
from moviepy.editor import  VideoFileClip

parser = ArgumentParser()
parser.add_argument("--input", required=True, type = str)
parser.add_argument("--start", required=True, type = int)
parser.add_argument("--end", required= True, type = int)
parser.add_argument("--out", required=True, type = str)

args = parser.parse_args()

clip = VideoFileClip(args.input)
print("Video duration", clip.duration)

if (args.start < 0) or (args.start > args.end) or (args.end > clip.duration):
    print("Invalid argument")
    exit()


out_clip = clip.subclip(args.start, args.end)
out_clip.write_videofile(args.out)

