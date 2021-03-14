 # Feed forward neural network with back propagation code

 ## Variables used :

 1. X_train     : shape (784, 54000)
 2. X_test      : shape (784, 10000)
 3. X_val       : shape (784, 6000)
 4. y_train_org : original y train with shape (54000, 1)
 5. y_val_org   : original y val with shape (6000, 1)
 6. y_train_one : one hot y train with shape (10, 54000)
 7. y_val_one   : one hot y val with shape (10, 6000) 
 8. y_test      : shape (10000, 1)
 9. nn          : number of neurons
 10. prev_n     : number of neurons in previous layer
 11. W          : a list containing weight matrices of all layers
 12. b          : a list containing bias matrices of all layers
 13. a          : a list containing pre activation vectors of all layers
 14. h          : a list containing activation vectors of all layers

 ## Note :  

 W_gd, W_m ====>  weight matrices of gradient descent and momentum gradient descent optimizers. And the name of these variables change accordingly depending upon the name of optimizer.

 Similarly for b, a and h.

 ## hyperparameters used in the optimizers:

 1. epochs: number of epochs

 2. learning_rate

 3. activate : if activate=None, then the activation function used will be sigmoid. if activate='tanh', then the activation function used will be tanh. if activate='relu', then the activation function used will be relu.

 4. initialization : if initialization=None, then the initialization will be random. if initialization='Xavier', then the initialization will be xavier

 5. regularise : alpha value which tells the amount of regularization to be used.

 6. batch : if batch=False then all the instances will the given to the network at each epoch.

 7. batch_size : if batch=True then a number should given here which will denote the number of batch of instances to be fed. i.e. if batch_size=1 then its stochastic.

 8. gamma_m : acceleration parameter for momentum.

 9. gamma_n : acceleration paramenter for nestrov.

 10. beta   : update parameter for rms prop.

 11. epsilon : update parameter for rms prop and adam.

 12. beta1,beta2 : update parameter for adam.

 ## Functions created :

 1. add_hidden_layer()  : used to add a hidden layer to the network.
 2. add_output_layer()  : used to add a output layer to the network.
 3. sigmoid()
 4. matrix_sigmoid()
 5. softmax()
 6. matrix_softmax()
 7. relu()
 8. matrix_relu()
 9. tanh()
 10. matrix_tanh()
 11. forward_prop()    : Performs forward propagation
 12. backward_prop()   : Performs backward propagation
 13. cross_entropy()   : calculates cross_entropy using the one hot vectors of the output
 14. gradient_descent() 
 15. momentum()
 16. nestrov()
 17. rmsprop()
 18. adam()
 19. accuracy(): Takes y_pred,y_true and calculates accuracy of the prediction.
 20. train() 




 # Self declaration:

 AM19M016 :

 1. created the add_hidden_layer and add_output_layer functions
 2. created all the functions for activations i.e. sigmoid, softmax, relu and tanh
 3. created the forward_prop function
 4. created the backward_prop function
 5. created the gradient_descent function

 AM19M029 :

 1. created the momentum function
 2. created the nestrov function
 3. created the rmsprop function
 4. created the adam function
 5. setting up the sweep in wandb and logging in wandb and generating the plots.

 We shaik azharuddin and shivam singh, swear on our honour that the above declaration is correct.
 


