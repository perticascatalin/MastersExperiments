## Relational reasoning in deep learning: a parallel between solving visual and programming tasks

### 1. A simple Neural Network Model for Relational Reasoning

Sample code for Sort-of-CLEVR, open source: https://github.com/clvrai/Relation-Network-Tensorflow

#### Code Running Logs

This repository is deprecated since Tensorflow2 (attempted to migrate to TF2, but got stuck at `contrib.layers.optimize_loss`, no equivalent in TF2).

Revert to TF1. This implies reverting to Python 3.6, was using Python 3.8. Got stuck with pyenv, cannot revert to 3.6.

Finally tried using:

- `sudo python -m pip install package` (for python 2.7)
- `sudo python3 -m pip install package` (for python 3.8)

Should use Python 2.7, with Tensorflow 1.15, got a working version this way. Plots visualized via Tensorflow-Plot.

- `python generator.py`
- `python trainer.py`
- `tensorboard --logdir ./train_dir`

Tensorboard then provides us with a localhost link and we can look at training statistics in the browser:

![Tensorboard](https://raw.githubusercontent.com/perticascatalin/Research/master/RelationalPROG/images/tensorboard.png)

After 15.000 training steps, we take a look at the currently tested images and we can see that 3 of 4 questions were answered correctly:

![Sample images](https://github.com/perticascatalin/Research/blob/master/RelationalPROG/images/samples.png)

After another 15.000 training steps the accuracy on the testing data reaches an average of 95%, while the loss drops to around 0.1:

![Accuracy and Loss](https://raw.githubusercontent.com/perticascatalin/Research/master/RelationalPROG/images/loss_acc.png)

### 2. Deep Coder: Learning to Write Programs