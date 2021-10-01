def setup():
    size(600, 600)
    

def draw():
    helligkeit = mouseY / 2.35
    print(helligkeit)
    background(helligkeit, helligkeit, helligkeit)
    ellipse(300, 300, mouseX, mouseX)
