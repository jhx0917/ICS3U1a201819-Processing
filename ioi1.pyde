
x = 0
value = 0
z = 0

def setup():
    global sat_img
    global back_img
    size(640, 480)
    sat_img = loadImage("IMG_0350.jpg")
    back_img = loadImage("IMG_0597.jpg")


def draw():
    global x
    
    if x >= 640:
        x = 0
    x += 3
    
    background(back_img)  # sky blue
    image(sat_img, 80, 80, 80, 80)
    # cloud
    noStroke()
    fill(255 , 102 , 178)
    ellipse(x, height/2, 50, 50)
    ellipse(x+30, height/2, 50, 50)
    ellipse(x+10, height/2-20, 50, 50)
    
    
    
    fill("#C17C74")
    rect(z, 50, 30, 30)
    




def mouseClicked(): 
    global z
    z +=20
    if z > 640:
        z = 0
