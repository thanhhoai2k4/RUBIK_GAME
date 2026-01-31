from ursina import *
from src import *


if __name__=="__main__":
    app = Ursina()
    window.title = title
    window.size = windowsize
    EditorCamera()
    # element
    bg = WebcamBackground(windowsize[0])
    rubik = RubikCube()
    app.run()