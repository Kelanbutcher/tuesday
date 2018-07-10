xCoordinate = 50
speed = 2
ellipsesize = 20

def setup():
    size(400,400)
    
def draw():
    background(0)
    global xCoordinate, speed, ellipseSize
    leftBoundary = ellipsesize / 2
    rightBoundry = 400 - ellipsesize / 2
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
    speed = -speed
    xCoordinate += speed
    fill(255,255,0)
    ellipse(xCoordinate,50, ellipsesize,ellipsesize)
    
    
    
    
    
    
    
    
    
    
