from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import scale_vector, add_vectors, Point
from compas_slicer.geometry import Path

def create_overhang_texture(slicer, overhang_distance = 10):
    for i, layer in enumerate(slicer.layers):
        if i%5==0 and i >0:
            for j, path in enumerate(layer.paths):
                new_path = []
                for k, point in enumerate(path.points):
                    if k%2==0:
                        #get normal of print point
                        normal =  get_normal_of_path_on_xy_plane(k, point ,path, mesh=None)
                        scaled_vector = scale_vector(normal, -overhang_distance)
                        new_pt = add_vectors(point, scaled_vector)
                        #create a compas point
                        point = Point(new_pt[0],new_pt[1],new_pt[2])
                    new_path.append(point)
                layer.paths[j] = Path(points=new_path, is_closed=path.is_closed)

