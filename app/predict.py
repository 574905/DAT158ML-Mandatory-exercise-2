import numpy as np
import pandas as pd
import joblib

####### 
## Get the model trained in the notebook 
# `../nbs/1.0-asl-train_model.ipynb`
#######

model = joblib.load('models/tmdbboxoffice.joblib')
pipeline = joblib.load('models/pipeline.joblib')


def preprocess(data):
    """
    Returns the features entered by the user in the web form. 

    To simplify, we set a bunch of default values. 
            For bools and ints, use the most frequent value
            For floats, use the median value

    Note that this represent some major assumptions that you'd 
    not want to make in real life. If you want to use default 
    values for some features then you'll have to think more 
    carefully about what they should be. 

    F.ex. if the user doesn't provide a value for BMI, 
    then one could use a value that makes more sense than 
    below. For example, the mean for the given gender would 
    at least be a bit more correct. 
    
    Having _dynamic defaults_ is important. And of course, if 
    relevant, getting some of the features without asking the user. 
    E.g. if the user is logged in and you can pull information 
    form a user profile. Or if you can compute or obtain the information 
    thorugh other means (e.g. user location if shared etc).
    """


    feature_values = {
        'belongs_to_collection': 0,
        'budget': 8000000,
        'genres': 'Drama',
        'original_language': 'En',
        'popularity': 7.3748615,
        'production_companies': 'Universal Pictures',
        'production_countries': "United States of America",
        'release_year': 2004,
        'runtime': 104,
        'spoken_languages': 'English',
        'Keywords': None,
        'cast': None
       
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

    column_order = ['belongs_to_collection', 'budget', 'genres', 'original_language', 'popularity', 'production_companies', 'production_countries', 'release_year', 'runtime', 'spoken_languages',
       'Keywords', 'cast']

    data = np.array([data[feature] for feature in column_order], dtype=object)
    data = pd.DataFrame(data.reshape(1, -1), columns = column_order)

    
    data = pipeline.transform(data)
    pred = model.predict(data)


   
    return pred


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])
   


    # Return
    return_dict = {'pred': pred}

    return return_dict