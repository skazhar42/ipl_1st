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
 13. a          : a list containing activation vectors of all layers
 14. h          : a list containing pre activation vectors of all layers

 ##Note :  

 W_gd, W_m ====>  weight matrices of gradient descent and momentum gradient descent optimizers. And the name of these variables change accordingly depending upon the name of optimizer.

 Similarly for b, a and h.

