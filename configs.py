# inital importing of pickled model and variables list
import pickle
from numpy.core.fromnumeric import var
import statsmodels.api as sm

final_fit = sm.load("final_fit.pkl")
variables = pickle.load(open("variables.pickle", "rb"))
# sort variables by alpha
variables = sorted(variables)
