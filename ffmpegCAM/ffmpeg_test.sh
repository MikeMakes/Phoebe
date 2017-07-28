#!/bin/bash

ffmpeg -f v4l2 -framerate 16 -video_size 640x480 -i /dev/video0 output2.h264
