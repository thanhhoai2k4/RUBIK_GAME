from ursina import *
from src import *


if __name__=="__main__":
    app = Ursina()
    window.title = title
    window.size = windowsize
    window.forced_aspect_ratio = False
    window.center_on_screen()
    EditorCamera()
    # element
    bg = WebcamBackground(windowsize[0], Coordinates=( 10, -10, 40), scale = (5,5))
    rubik = RubikCube()
    app.run()