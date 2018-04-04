import sys
import numpy as np
import tifffile
import gi
import ufo.numpy
gi.require_version('Ufo', '0.0')
from gi.repository import Ufo


def write_image(path, image):
    try:
        image[0]
    except:
        image = [image]
    tifffile.imsave(path, np.array([image]).astype(np.float32))


def make_input(width, height):
    # Mean is not zero, so skew and kurtosis will work
    return np.linspace(0, 1, num=width * height).reshape(height, width).astype(np.float32) ** 2


def measure_numpy(path, metric, axis, width, height):
    image = make_input(width, height).astype(np.float)

    if metric == 'skew':
        from scipy.stats import skew
        func = skew
    elif metric == 'kurtosis':
        from scipy.stats import kurtosis
        func = kurtosis
    else:
        func = getattr(np, metric)

    result = func(image, axis=1 - axis if axis != -1 else None)
    write_image(path, result)


def measure_ufo(out_path, metric, axis, width, height):
    pm = Ufo.PluginManager()
    sched = Ufo.Scheduler()
    graph = Ufo.TaskGraph()
    input_path = 'data/measure.tif'

    image = make_input(width, height)
    tifffile.imsave(input_path, image)

    reader = pm.get_task('read')
    measure = pm.get_task('measure')
    output = Ufo.OutputTask()

    reader.props.path = input_path
    measure.props.axis = axis
    measure.props.metric = metric

    graph.connect_nodes(reader, measure)
    graph.connect_nodes(measure, output)

    sched.run(graph)

    buf = output.get_output_buffer()
    gpu_result = ufo.numpy.asarray(buf)
    write_image(out_path, gpu_result)


def main():
    reference_path, out_path, metric, axis, width, height = sys.argv[1:]
    axis = int(axis)
    width = int(width)
    height = int(height)

    try:
        measure_numpy(reference_path, metric, axis, width, height)
        measure_ufo(out_path, metric, axis, width, height)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
