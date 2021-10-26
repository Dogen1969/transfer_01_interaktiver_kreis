def setup():
    size(700, 700)
    

def draw():
    translate(width/2, height/2)
    helligkeit = map(mouseY, 0, height, 0, 350)
    print(helligkeit)
    background(helligkeit, helligkeit, helligkeit)
    ellipse(0, 0, mouseX, mouseX)
