import os


def cut(start, duration, video_input, video_out):
    command = 'ffmpeg -ss ' + start + ' -i ' + video_input + ' -c copy -t ' + duration + ' ' + video_out
    os.system(command)


def histogram(video_input):
    command = 'ffplay ' + video_input + ' -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"'
    os.system(command)


def resize_scale(pixels, input, output):
    if len(pixels) == 3:
        command = 'ffmpeg -i ' + input + ' -filter:v scale=' + pixels + ':-1 -c:a copy ' + output
    elif len(pixels) > 3:
        command = 'ffmpeg -i ' + input + ' -s ' + pixels + ' -c:a copy ' + output
    os.system(command)


def stereo_to_mono(input, output):
    command = 'ffmpeg -i ' + input + ' -map_channel 0.1.0 -c:v copy ' + output
    os.system(command)

# initial seconds, duration, name of the input file, name of the output file
# cut('0','12','BBB.mp4','BBBcut.mp4')

# name of the input filename
# histogram('BBB.mp4')

# output resolution(can be type XXXxXXX or XXX), input filename, output filename
# resize_scale('160x120', 'BBB.mp4', 'BBB160x120.mp4')

# input filename, output filename
# stereo_to_mono('BBB.mp4','mono.mp4')
