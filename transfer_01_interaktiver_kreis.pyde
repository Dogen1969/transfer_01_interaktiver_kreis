def setup():
    size(700, 700)
    

def draw():
    translate(width/2, height/2)
    helligkeit = mouseY / 2.35
    print(helligkeit)
    background(helligkeit, helligkeit, helligkeit)
    ellipse(0, 0, mouseX, mouseX)
