import time
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver

def autolabel(ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def printProbabilities(probs,player,moves):
    #probs = [white, draw, black]
    win_probs = [p[0] if player == 'w' else p[2] for p in probs]
    draw_probs = [p[1] for p in probs]
    lose_probs = [p[2] if player == 'w' else p[0] for p in probs]
    labels = moves[:len(probs)]

    x = np.arange(len(labels))  # the label locations
    width = 0.13  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, win_probs, width, color='indianred', label='Winning')
    rects2 = ax.bar(x, lose_probs, width, color='lightsalmon',label='Losing')
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
    plt.savefig('Output/probabilities.png')
    plt.show()


def cropImage(png,e):
    im = Image.open(BytesIO(png))

    left = e.location['x'] - 5
    top = e.location['y'] - 110
    right = e.location['x'] + e.size['width']
    bottom = e.location['y'] + e.size['height'] - 75
    
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('Output/chesstable.png') # saves new cropped image
    img = Image.open('Output/chesstable.png')
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
    time.sleep(2)
    element = driver.find_element_by_class_name('result')
    png = driver.get_screenshot_as_png()
    cropImage(png,element)
    driver.close()

def printChessTable(fen):
    fen = fen.replace('%20',' ')
    image = webDriver(fen)
    

