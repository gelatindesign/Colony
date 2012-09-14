# ------------------------ Panda3D Configuration File ------------------------
# User editable configuration settings for Panda3D
# ----------------------------------------------------------------------------



# ------------------------ Rendering ------------------------

# Set rendering engine to DirectX or OpenGL
load-display pandagl
#load-display pandadx9
#load-display pandadx8
#load-display tinydisplay



# ------------------------ Window / Screen ------------------------

#window-type none
window-title Colony

win-size 1280 960

# Enables full-screen mode (true or false)
fullscreen #f

# Removes border from window (true or false)
undecorated #f

# Limits the frame rate to monitor's capabilities (vsync)
sync-video #t



# ------------------------ Profiling ------------------------

# Shows the frame rate (in frames per second) at the upper right corner of the screen (true or false)
show-frame-rate-meter #t



# ------------------------ Models ------------------------

model-path $MAIN_DIR/data/models