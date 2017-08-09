import theano
from theano import tensor as T
import numpy as np
import lasagne
import setup

output_size, x_train, y_train = setup.loadData('train', 'head')
print('Data loading completed')

#batch size x image channels x height x width
data_size = (None, 1, 100, 100)


input_var = T.tensor4('input')
target_var = T.ivector('targets')


net = {}

net['data'] = lasagne.layers.InputLayer(data_size, input_var=input_var)

net['conv1'] = lasagne.layers.Conv2DLayer(net['data'], num_filters=5, filter_size=5)
net['pool1'] = lasagne.layers.Pool2DLayer(net['conv1'], pool_size=2)

net['conv2'] = lasagne.layers.Conv2DLayer(net['pool1'], num_filters=5, filter_size=5)
net['pool2'] = lasagne.layers.Pool2DLayer(net['conv2'], pool_size=2)

net['fc1'] = lasagne.layers.DenseLayer(net['pool2'], num_units=100)
net['drop1'] = lasagne.layers.DropoutLayer(net['fc1'],  p=0.3)

net['out'] = lasagne.layers.DenseLayer(net['drop1'], num_units=output_size, nonlinearity=lasagne.nonlinearities.softmax)

print('Network configuration completed')




#hyperparameters
lr = 1e-2
weight_decay = 1e-5

#mean cross entropy loss function
prediction = lasagne.layers.get_output(net['out'])
loss = lasagne.objectives.categorical_crossentropy(prediction, target_var)
loss = loss.mean()

#Also add weight decay to the cost function
weightsl2 = lasagne.regularization.regularize_network_params(net['out'], lasagne.regularization.l2)
loss += weight_decay * weightsl2

#get the update rule for sgd with nesterov momentum
params = lasagne.layers.get_all_params(net['out'], trainable=True)
updates = lasagne.updates.sgd(loss, params, learning_rate=lr)


train_fn = theano.function([input_var, target_var], loss, updates=updates)

test_prediction = lasagne.layers.get_output(net['out'], deterministic=True)
test_loss = lasagne.objectives.categorical_crossentropy(test_prediction,
                                                        target_var)
test_loss = test_loss.mean()
test_acc = T.mean(T.eq(T.argmax(test_prediction, axis=1), target_var),
                  dtype=theano.config.floatX)

val_fn = theano.function([input_var, target_var], [test_loss, test_acc])
get_preds = theano.function([input_var], test_prediction)

print('Function configuration completed')


print('Training started')

import time
epochs = 50
batch_size = 100

#run training function for each mini-batches
n_examples = x_train.shape[0]
n_batches = int(n_examples / batch_size)

start_time = time.time()

cost_history = []
for epoch in range(epochs):
    st = time.time()
    batch_cost_history = []
    for batch in range(n_batches):
        x_batch = x_train[batch*batch_size: (batch+1) * batch_size]
        y_batch = y_train[batch*batch_size: (batch+1) * batch_size]
        
        this_cost = train_fn(x_batch, y_batch) #update
        
        batch_cost_history.append(this_cost)
        
    epoch_cost = np.mean(batch_cost_history)
    cost_history.append(epoch_cost)
    en = time.time()
    print('Epoch %d/%d, training error %f, time %.2fs' % (epoch+1, epochs, epoch_cost, en-st))
    
end_time = time.time()
print('Training completed in %.2fs.' % (end_time - start_time))

