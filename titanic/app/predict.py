import numpy as np
import pandas as pd
import joblib

model = joblib.load('titanic/models/titanic_model_v3.joblib')


def preprocess(data):


    feature_values = {
        'PassengerId': 1,
        'Pclass': 3,
        'Age': 1,
        'SibSp': 0,
        'Sex': 0,
        'Embarked': 2,
        'Title': 3,
        'Fare': 14.45,
        'Parch': 0,
    }


    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values



####### 
## Now we can predict with the trained model:
#######


def predict(data):
    """
    If debug, print various useful info to the terminal.
    """
 
    # Store the data in an array in the correct order:

    column_order = ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked','Title']

    data = np.array([data[feature] for feature in column_order], dtype=object)
    print(data.shape)


    # NB: In this case we didn't do any preprocessing of the data before 
    # training our random forest model (see the notebool `nbs/1.0-asl-train_model.ipynb`). 
    # If you plan to feed the training data through a preprocessing pipeline in your 
    # own work, make sure you do the same to the data entered by the user before 
    # predicting with the trained model. This can be achieved by saving an entire 
    # sckikit-learn pipeline, for example using joblib as in the notebook.
    
    pred = model.predict(data.reshape(1,-1))

    uncertainty = model.predict_proba(data.reshape(1,-1))

    return pred, uncertainty


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred, uncertainty = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])
    uncertainty = str(uncertainty[0])


    # Return
    return_dict = {'pred': pred, 'uncertainty': uncertainty}

    return return_dict