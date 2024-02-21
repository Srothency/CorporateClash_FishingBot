import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def perform_linear_regression(X_list, Y_list):
    # Convert lists to numpy arrays and reshape X to fit the model requirements
    X = np.array(X_list).reshape(-1, 1)
    Y = np.array(Y_list)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    return model, score

    from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def perform_linear_regression(from_list, to_list):
    X = np.array(from_list).reshape(-1, 1)
    Y = np.array(to_list)
    from_train, from_test, to_train, to_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(from_train, to_train)
    score = model.score(from_test, to_test)
    return model, score

mouse_x = [983, 1022, 1040, 1045, 1049, 1052, 1063, 1070, 1090, 1108, 1115]
fish_x = [909, 758, 724, 680, 748, 702, 723, 584, 644, 428, 556]
mouse_y = [939, 932, 993, 861, 1041, 938, 988, 855, 1031, 894, 959]
fish_y = [394, 391, 274, 658, 189, 395, 336, 638, 199, 551, 410]

x_model, x_score = perform_linear_regression(fish_x, mouse_x)
print(f"slope for x is {x_model.coef_} and intercept is {x_model.intercept_}")
y_model, y_score = perform_linear_regression(fish_y, mouse_y)
print(f"slope for y is {y_model.coef_} and intercept is {y_model.intercept_}")