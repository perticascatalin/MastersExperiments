import os
import pickle
import tensorflow as tf
import numpy as np
import analysis as co
import generator as gen
import setup as stp
import pdb

# Setup experiment size and parameters
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
N_CLASSES = stp.num_classes
batch_size = 128
data_type = "data"
lsts_train, orders_train = gen.data()

def neural_net(x, inputs, n_classes, num_labels, dropout, reuse, is_training):
	with tf.variable_scope('SortNet', reuse = reuse):
		v = tf.Variable(tf.zeros([1]), trainable = False)

lsts_train = tf.convert_to_tensor(lsts_train, dtype = tf.float32)
orders_train = tf.convert_to_tensor(orders_train, dtype = tf.int32)
lsts_train, orders_train = tf.train.slice_input_producer([lsts_train, orders_train], shuffle = True)

X, Y = tf.train.batch([lsts_train, orders_train], batch_size = batch_size, capacity = batch_size * 8, num_threads = 4)

#logits_train, y_train = neural_net(X, Y, N_OUT_CLASSES, N_CLASSES, dropout, reuse = False, is_training = False)
ts = np.zeros((N_CLASSES, N_CLASSES, N_CLASSES, ), np.float32)
for i in range(N_CLASSES):
	for j in range(N_CLASSES):
		if i == j:
			continue

		ts[i][j][i] = 1.0
		ts[i][j][j] = -1.0

print ts[:,0,1], ts[:,1,2], ts[:,1,3]
v = tf.Variable(ts, trainable = False)
v = tf.expand_dims(v, 0)
X = tf.transpose(X)
X = tf.expand_dims(X, 0)
X = tf.expand_dims(X, 3)
print v.shape
print X.shape
res = tf.matmul(v, X)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as sess:
	# Run the initializer
	sess.run(init)
	# Start the data queue
	coord = tf.train.Coordinator()
	threads = tf.train.start_queue_runners(sess = sess, coord = coord)

	sol = sess.run([res])
	pdb.set_trace()
