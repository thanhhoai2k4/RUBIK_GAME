from ursina import *
import cv2
from PIL import Image

class RubikCube(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cubes = []
        self.cube_colors = [
            color.pink, color.orange,
            color.white, color.yellow,
            color.azure, color.green
        ]
        self.scale = (0.75, 0.75)
        template_model = self._create_template_model()
        self._spawn_cubes(template_model)

    def _create_template_model(self):
        """Tạo ra model 6 mặt màu, combine lại và trả về model data"""
        temp_parent = Entity(enabled=False)
        for i, direction in enumerate((Vec3.right, Vec3.up, Vec3.forward)):
            e = Entity(parent=temp_parent, model='plane', origin_y=-.5,
                       color=self.cube_colors[i * 2])
            e.look_at(direction, 'up')
            e_flipped = Entity(parent=temp_parent, model='plane', origin_y=-.5,
                               color=self.cube_colors[i * 2 + 1])
            e_flipped.look_at(-direction, 'up')
        temp_parent.combine()
        model = temp_parent.model
        destroy(temp_parent)
        return model

    def _spawn_cubes(self, model_template):
        """Sinh ra 27 viên, sắp xếp và gán làm con của self"""
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    # Tạo entity con, gán parent=self để nó dính vào khối cha
                    e = Entity(
                        parent=self,
                        model=copy(model_template),
                        texture='white_cube',
                        position=Vec3(x, y, z) - Vec3(1, 1, 1)  # Căn giữa về (0,0,0)
                    )
                    self.cubes.append(e)
    def input(self, key):
        if key == 'l':
            print("xxxx")

    def update(self):
        pass

