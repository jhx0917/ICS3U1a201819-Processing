
x = 0
value = 0
z = 0

text_size = 30
rotation = 0
rotation_speed = 0
text_size_speed = 1
animate = False

def setup():
    global sat_img
    global back_img
    global s
    size(640, 480)
    back_img = loadImage("IMG_0597.jpg")
    sat_img = loadImage("IMG_1547.jpg")
    s =  loadImage("1531220956636c15d6061ad.jpeg")
def draw():
    global x
    global text_size
    global rotation
    global rotation_speed
    global text_size_speed

    if x >= 640:
        x = 0
    x += 3
    
    background(back_img)  # sky blue
    image(sat_img, 0, 25, 100, 100)
    image(s, z+20, 50, 30 ,30)
    # cloud
    noStroke()
    fill(255 , 102 , 178)
    ellipse(x, height/2, 50, 50)
    ellipse(x+30, height/2, 50, 50)
    ellipse(x+10, height/2-20, 50, 50)
      
    fill(176 ,202 ,48)
    rect(0 , 400 ,250 ,20)
    fill(255, 204 ,229)
    ellipse(600, 70 ,80, 80)

    fill(255, 153,255)
    rect(500, 400, 500 ,500)
    
    


    if animate:
        rotation_speed += 0.01
        text_size_speed += 0.3
        text_size += text_size_speed
        rotation += rotation_speed
    

    translate(width/2, height/2)
    rotate(rotation)
    textSize(text_size)
    fill(200, 50, 255, 255-text_size/2)
    text("Kisses", 0, 0)



    if keyPressed:
        if key == 'b' or key == 'B':
            fill(255, 102, 225)

    else:
        fill(204, 153,255)

    rect(25, 25, 50, 50)





def mouseClicked(): 
    global z
    z +=20
    if z > 640:
        z = 0
        
        
        
        
def mousePressed():
    global animate
    animate = not animate
