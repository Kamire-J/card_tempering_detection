# Important libraries and modules
from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image 


# Define Config Paths
app.config['INITIAL_FILE_UPLOADS'] = '../static/uploads' 
app.config['EXISTNG_FILE'] = '../static/original'
app.config['GENERATED_FILE'] = '../static/generated'