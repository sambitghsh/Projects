
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import matplotlib.pyplot as plt 


class Ridge_linear():
      def _init_(self, alpha=0.20, solver='closed'):
          self.alpha = alpha
          self.solver = solver

      def fit(self, X, y):
          X_with_intercept = np.c_[np.ones((X.shape[0], 1)), X]
          #print("intercept:",X_with_intercept)
          self.X_intercept = X_with_intercept
          if self.solver == 'closed':
              dimension = X_with_intercept.shape[1]
              print("Dimention:",dimension)
              A = np.identity(dimension)
              A[0, 0] = 0
              A_biased = self.alpha * A
              thetas = np.linalg.inv(X_with_intercept.T.dot(
                  X_with_intercept) + A_biased).dot(X_with_intercept.T).dot(y)
              self._coef_hat  = thetas
          self.thetas = thetas
          return self

      def predict(self, X):
          thetas = self.thetas
          X_predictor = np.c_[np.ones((X.shape[0], 1)), X]
          self.predictions = X_predictor.dot(thetas)
          return self.predictions
      
     
def main() : 
      
        # Importing dataset     
        df = pd.read_csv( 'C:/Users/Lenovo/Downloads/trdata.txt', usecols=range(1,15) , delimiter=",") 
        X = df.iloc[:, :-1].values 
        Y = df.iloc[:, -1].values     
      
        # Splitting dataset into train and test set 
        X_train, X_test, Y_train, Y_test = train_test_split( X, Y,  
                                                
                                              test_size = 0.25, random_state = 10) 
          
        # Model training     
        model = Ridge_linear() 
        model.fit( X_train, Y_train ) 
          
        # Prediction on test set 
        
        Y_pred = model.predict( X )
        Y_pred_test = model.predict( X_test )
                
        a = list(range(len(model._coef_hat)))
        print("a:",a)
        plt.plot(a, model._coef_hat)

        print(Y_pred)
        print("R2 score",r2_score(Y,Y_pred))
        print("RMSE",np.sqrt(mean_squared_error(Y,Y_pred)))
        print("R2 score",r2_score(Y_test,Y_pred_test))
        print("RMSE",np.sqrt(mean_squared_error(Y_test,Y_pred_test)))
        
        df = pd.read_csv('C:/Users/Lenovo/Downloads/Testdata.txt', usecols=range(1,14) , delimiter=",")
        X_test_input= df.iloc[:, :].values
        Y_pred_input = model.predict( X_test_input)
        for i in range(0,Y_pred_input.shape[0]):
            print(Y_pred_input[i])
        
        
      
if __name__ == '__main__' :
    main()