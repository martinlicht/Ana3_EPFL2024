#!/usr/bin/python3

import copy 

import matplotlib.pyplot as plt
import numpy as np
import time 

from PIL import Image
from PIL import Image, ImageDraw
import colorsys
import io

def square(x):
    return x * x

def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

def get_image_path_from_script_path(input_str):
    if input_str.endswith(".py"):
        # Create a modified string with ".gif" extension
        modified_str = input_str[:-2] + "gif"
        return modified_str
    else:
        raise ValueError("Input string does not end with '.py'")

def create_image( output_image_frames, name ):
    print( "Saving in: " + name )
    output_image_frames[0].save( 
        name,
        save_all=True, 
        append_images=output_image_frames[1:], 
        optimize=False, 
        duration=140, 
        loop=0,
        interlace=False
        )
