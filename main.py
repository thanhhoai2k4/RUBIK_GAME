from ursina import *
from src import *


if __name__=="__main__":
    app = Ursina()
    window.title = title
    window.size = windowsize
    EditorCamera()
    bg = WebcamBackground()
    rubik = RubikCube()
    app.run()