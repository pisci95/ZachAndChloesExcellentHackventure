from PIL import Image as PIL_Image

orig_img_path = '/home/xilinx/jupyter_notebooks/Examples/data/webcam.jpg'
!fswebcam  --no-banner --save {orig_img_path} -d /dev/video0 2> /dev/null

img = PIL_Image.open(orig_img_path)
img
