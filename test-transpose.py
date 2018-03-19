import sys
import numpy as np
import tifffile
import gi
gi.require_version('Ufo', '0.0')
from gi.repository import Ufo


def make_input(width, height):
    return np.arange(width * height, dtype=np.float32).reshape(height, width)


def transpose_numpy(width, height, path):
    image = make_input(width, height)
    tifffile.imsave(path, image.T)


def transpose_ufo(width, height, path):
    pm = Ufo.PluginManager()
    graph = Ufo.TaskGraph()
    sched = Ufo.Scheduler()
    input_path = 'data/transpose.tif'

    image = make_input(width, height)
    tifffile.imsave(input_path, image)

    reader = pm.get_task('read')
    transpose = pm.get_task('transpose')
    writer = pm.get_task('write')

    reader.props.path = input_path
    writer.props.filename = path

    graph.connect_nodes(reader, transpose)
    graph.connect_nodes(transpose, writer)
    sched.run(graph)


def main():
    path_numpy, path_ufo, width, height = sys.argv[1:]
    width = int(width)
    height = int(height)

    transpose_numpy(width, height, path_numpy)
    transpose_ufo(width, height, path_ufo)


if __name__ == '__main__':
    main()
