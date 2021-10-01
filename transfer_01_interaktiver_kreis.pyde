def setup():
    size(700, 700)
    

def draw():
    helligkeit = mouseY / 2.35
    print(helligkeit)
    background(helligkeit, helligkeit, helligkeit)
    ellipse(350, 350, mouseX, mouseX)
