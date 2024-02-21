import keyboard
from PIL import Image
import pyautogui
import numpy as np
import cv2
import time
from threading import Thread

COLOR_FULL= "color_full.png"
COLOR_CROPPED = "color_cropped.png"
GRAYSCALE_CROPPED = "grayscale_cropped.png"
BW_CROPPED = "bw_cropped.png"

def get_bw_region(bw_threshold): #returns a black/white PIL Image object
    global fishing_bounds
    left, top, right, bottom = fishing_bounds
    width = right - left
    height = bottom - top
    crop_area = (left, top, width, height)
    color_cropped = pyautogui.screenshot(region=crop_area)
    color_cropped.save(COLOR_CROPPED)
    color_full = pyautogui.screenshot()
    color_full.save(COLOR_FULL)
    bw_cropped = color_cropped.convert('L').point(lambda x: 0 if x > bw_threshold else 255) #
    bw_cropped.save(BW_CROPPED)
    return bw_cropped

def find_biggest_shadow(bw_image):
    global fishing_bounds
    bw_cropped_np = np.array(bw_image)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(bw_cropped_np, connectivity=8, ltype=cv2.CV_32S)
    if num_labels <= 1: #just in case we only had one area
        print("no areas found!")
        return 500, 500
    largest_label_index = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1  # +1 to correct for skipping the first component
    center_of_largest_component = centroids[largest_label_index]
    #print(f"The center of the biggest white region is at {center_of_largest_component}")
    shadow_x = center_of_largest_component[0] + fishing_bounds[0]
    shadow_y = center_of_largest_component[1] + fishing_bounds[1]
    return shadow_x, shadow_y

def calculate_cast(fish_x,fish_y):
    cast_x = ((fish_x * -.34) + 1291) #-.34x+1291.15
    cast_y = ((fish_y * -.378) + 1100) #-.378x+1099.65
    print(f"castx: {cast_x} casty: {cast_y}")
    return cast_x, cast_y

def cast_rod(cast_x, cast_y):
    screen_width, screen_height = pyautogui.size()
    cast_button_x = screen_width // 2
    cast_button_y = screen_height * .75
    pyautogui.moveTo(cast_button_x, cast_button_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(cast_x, cast_y, duration=.005)
    pyautogui.mouseUp()
    return

def wait_for_fish():
    time.sleep(1.75)
    return

def fish():
    while not stop_thread:
        bw_region = get_bw_region(123) #higher threshold = easier regions
        shadow_x, shadow_y = find_biggest_shadow(bw_region)
        cast_x, cast_y = calculate_cast(shadow_x, shadow_y)
        cast_rod(cast_x, cast_y)
        wait_for_fish()

def start_fishing():
    global stop_thread, thread
    if stop_thread:
        stop_thread = False
        fish_thread = Thread(target=fish)
        fish_thread.start()

def stop_fishing():
    global stop_thread
    stop_thread = True

def calibrate():
    global fishing_bounds
    mouse_x, mouse_y = pyautogui.position()
    color_full = pyautogui.screenshot()
    color_full.save(f"X{mouse_x:.0f}_Y{mouse_y:.0f}.png")
    return

#left, top, right, down
#fishing_bounds = [385, 220, 875, 750] #boatyard street
#fishing_bounds = [440, 40, 985, 510] #Acorn Acres
fishing_bounds = [632, 152, 1300, 590] #Brrgh (closest dock to Polar Place)

stop_thread = True
keyboard.add_hotkey('F12', start_fishing)
keyboard.add_hotkey('F11', stop_fishing)
keyboard.add_hotkey('F10', calibrate)

keyboard.wait('esc')