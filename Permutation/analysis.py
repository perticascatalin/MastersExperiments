import numpy as np
import matplotlib.pyplot as plt
import setup as stp

N_CLASSES = stp.num_classes()

def debugger(correct_pred, logits, y_exp, x):
	print (str(int(correct_pred[0])) + " out of " + str(N_CLASSES))
	# to check first and second choice
	# out = list()
	# for j in range(N_CLASSES):
	# 	f_max = np.argmin(logits[0][j])
	# 	f_max_2 = np.argmin(logits[0][j])
	# 	for k in range(N_CLASSES):
	# 		if logits[j][0][k] > logits[j][0][f_max]:
	# 			f_max_2 = f_max
	# 			f_max = k
	# 		elif logits[j][0][k] > logits[j][0][f_max_2]:
	# 			f_max_2 = k
	# 	out.append((f_max, f_max_2))
	# print out

def print_1by1(arr, title):
	line = ""
	for i in range(N_CLASSES):
		line += (str(arr[i]) + " ")
	print (title + line)

def print_barchart(arr, expect, actual, figname):
	n_groups = len(arr[:N_CLASSES])
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	xticks = map(str, np.arange(1, n_groups + 1))
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, tuple(expect), bar_width, alpha=opacity, color='g', label='Expected')
	rects2 = plt.bar(index + bar_width, tuple(actual), bar_width, alpha=opacity, color='r', label='Actual')
	 
	plt.xlabel('Element')
	plt.ylabel('Value')
	plt.title('Expected vs. actual labels')
	plt.xticks(index + bar_width, tuple(xticks))
	plt.legend()
	plt.savefig('./data/' + figname)
	plt.clef()

# asm plot
def print_acc_scale_models():
	ns = [6, 8, 9, 10, 11, 12, 16, 20, 24]
	nn = [1.00, 1.00, 1.00, 0.95, 0.66, 0.44, 0.23, 0.07, 0.04]
	dt = [1.00, 0.99, 0.92, 0.75, 0.68, 0.60, 0.34, 0.23, 0.15]
	rd = [0.17, 0.12, 0.11, 0.10, 0.09, 0.08, 0.06, 0.05, 0.04]
	plt.title('Predict Sorted Order', fontsize = 18)
	plt.xlabel('# Elements', fontsize = 16)
	plt.ylabel('% Correctly Guessed', fontsize = 16)
	plt.plot(ns, nn, 'b', linewidth = 2.8, label = 'Neural Net')
	plt.plot(ns, dt, 'g', linewidth = 2.8, label = 'Decision Trees')
	plt.plot(ns, rd, 'y', linewidth = 2.8, label = 'Random')
	plt.legend()
	plt.savefig('./results/' + 'asm.png')
	plt.clf()

def pretty_printing(correct_pred, logits, y_exp, x, epoch):
	out = list()
	y_pred = list()
	for j in range(N_CLASSES):
		y_pred.append(np.argmax(logits[j][0]))
	print_1by1(x[0], 'input: ')
	print_1by1(y_exp[0], 'expect:')
	print_1by1(y_pred, 'pred:  ')
	print_barchart(x[0], list(y_exp[0]), y_pred, ('labels_' + str(epoch) + '.png'))

#print_barchart(list([10, 30, 20, 40, 50]), list([1, 3, 2, 4, 5]), list([1, 2, 3, 4, 5]), 'labels_0.png')
#print_acc_scale_models()
