import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
import time
from PIL import Image
from io import BytesIO
import cv2
import time

def printProbabilities(probs,moves):
    white_probs = [p[0] for p in probs]
    draw_probs = [p[1] for p in probs]
    black_probs = [p[2] for p in probs]
    labels = moves[:len(probs)]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, white_probs, width, color='indianred', label='Whites')
    rects2 = ax.bar(x + width/2, black_probs, width, color='lightsalmon',label='Blacks')
    rects3 = ax.bar(x + width, draw_probs, width, color='green',label='Draw')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Rating')
    ax.set_title('Probabilities of winning')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    autolabel(ax,rects1)
    autolabel(ax,rects2)
    autolabel(ax,rects3)

    fig.tight_layout()
    plt.show()


def autolabel(ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def cropImage(png,e):
    im = Image.open(BytesIO(png))

    left = e.location['x'] - 5
    top = e.location['y'] - 110
    right = e.location['x'] + e.size['width']
    bottom = e.location['y'] + e.size['height'] - 75
    
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('testing.png') # saves new cropped image
    img = Image.open('testing.png')
    img.show() 


def webDriver(query):
    url = "https://www.dcode.fr/fen-chess-notation"
    driver = webdriver.Chrome()
    driver.get(url)
    webform = driver.find_element_by_xpath("//input[@id='fen_reader_fen']").clear()
    webform = driver.find_element_by_xpath("//input[@id='fen_reader_fen']")
    webform.send_keys(query)
    button = driver.find_elements_by_xpath("//button")[2]
    button.click()
    time.sleep(3)
    element = driver.find_element_by_class_name('result')
    png = driver.get_screenshot_as_png()
    cropImage(png,element)
    driver.close()

def printChessTable(fen):
    fen = fen.replace('%20',' ')
    image = webDriver(fen)
    

