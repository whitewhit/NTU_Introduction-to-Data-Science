import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def simple_linear_regression_fit(x_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    """
    Inputs:
    x_train: a (num observations by 1) array holding the values of the predictor variable
    y_train: a (num observations by 1) array holding the values of the response variable

    Returns:
    beta_vals:  a (num_features by 1) array holding the intercept and slope coeficients
    """
    
    x_mean = np.mean(x_train)
    y_mean = np.mean(y_train)

    numerator = 0.
    denominator = 0.
    
    for i in range(x_train.size):
        numerator += (x_train[i] - x_mean)*(y_train[i] - y_mean)
        denominator += (x_train[i] - x_mean)*(x_train[i] - x_mean)

    beta_1 = numerator/denominator
    beta_0 = y_mean -beta_1 * x_mean

    return np.array([beta_0, beta_1])


def main():
    # 1.
    x_train = np.array([[1], [2], [3]])
    y_train = np.array([2, 2, 4])
    print('X_train shape = ' , x_train.shape)
    print('y_train shape = ' , y_train.shape)

    # 2.
    a = simple_linear_regression_fit(x_train, y_train)
    x = np.linspace(0, 4, 40)
    y = a[1]*x + a[0]

    # 3.
    linear_model = LinearRegression(fit_intercept=True)

    linear_model.fit(x_train, y_train)
    linear_model.coef_, linear_model.intercept_
    a = [linear_model.coef_[0],linear_model.intercept_]

    Xfit = np.expand_dims(np.linspace(0, 4, 11), axis=1)
    yfit = linear_model.predict(Xfit)

    linear_r2 = linear_model.score(x_train, y_train)

    # 畫圖
    fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex=True, figsize=(8, 8))
    # 圖一顯示1.與2.
    ax0 = ax[0]
    ax0.set_title('simple_linear_regression_fit ')
    ax0.scatter(x_train, y_train, c='lightgray')
    ax0.plot(x, y, c='orange', lw=2, label= f'Linear (d=1), $y={a[0]:.2f}x + {a[1]}$')
    ax0.legend()

    # 圖一顯示1.與3.
    ax1 = ax[1]
    ax1.set_title('sklearn.linear_model ')
    ax1.scatter(x_train, y_train, c='lightgray')
    ax1.plot(Xfit, yfit, c='green', lw=2, label= f'Linear (d=1), $y={linear_model.coef_[0]:.2f}x + {linear_model.intercept_}$')
    ax1.legend()

    plt.subplots_adjust(hspace=0.4)
    plt.show()

    
if __name__ == "__main__":
    main()