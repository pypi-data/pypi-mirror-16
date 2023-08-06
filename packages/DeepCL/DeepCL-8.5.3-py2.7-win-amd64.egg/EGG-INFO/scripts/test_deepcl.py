#!c:\env-27-64\Scripts\python.exe

# train on mnist, storing data in array.arrays
# see test_deepcl_numpy.py for an example using numpy arrays

from __future__ import print_function, division
import array
import PyDeepCL
import sys
print('imports done')

if len(sys.argv) != 2:
    print(
        'usage: python ' + sys.argv[0] +
        ' [mnist data directory (containing the .mat files)]')
    sys.exit(-1)

mnistFilePath = sys.argv[1] + '/t10k-images-idx3-ubyte'

cl = PyDeepCL.DeepCL()

print('compute units:', cl.getComputeUnits())
print('local memory size, bytes:', cl.getLocalMemorySize())
print('local memory size, KB:', cl.getLocalMemorySizeKB())
print('max workgroup size:', cl.getMaxWorkgroupSize())
print('max alloc size MB:', cl.getMaxAllocSizeMB())

net = PyDeepCL.NeuralNet(cl, 1, 28)
print('created net')
print(net.asString())
print('printed net')
net.addLayer(PyDeepCL.NormalizationLayerMaker().translate(-0.5).scale(1/255.0))
print('added layer ')
PyDeepCL.NetdefToNet.createNetFromNetdef(
    net, "rt2-8c5z-relu-mp2-16c5z-relu-mp3-150n-tanh-10n")
print(net.asString())

(N, planes, size) = PyDeepCL.GenericLoader.getDimensions(mnistFilePath)
print((N, planes, size))

N = 1280
images = array.array('f', [0] * (N * planes * size * size))
labels = array.array('i', [0] * N)
PyDeepCL.GenericLoader.load(mnistFilePath, images, labels, 0, N)
print('loaded data')

sgd = PyDeepCL.SGD(cl, 0.002, 0.0)
print('created SGD')
sgd.setWeightDecay(0.0001)
netLearner = PyDeepCL.NetLearner(
    sgd, net,
    N, images, labels,
    N, images, labels,
    128)
print('created netLearner')
netLearner.setSchedule(12)
netLearner.run()
print('done, cleaning up...')
