# inital importing of pickled model and variables list
import pickle
import statsmodels.api as sm

Final_Model = pickle.load(open("final_model.pickle", "rb"))
final_fit = sm.load("final_fit.pkl")
variables = pickle.load(open("variables.pickle", "rb"))
print(type(Final_Model))
# sort variables by alpha
variables = sorted(variables)