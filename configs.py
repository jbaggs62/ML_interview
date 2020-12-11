# inital importing of pickled model and variables list
import pickle

Final_Model = pickle.load(open("final_model.pickle", "rb"))
variables = pickle.load(open("variables.pickle", "rb"))

# sort variables by alpha
variables = sorted(variables)