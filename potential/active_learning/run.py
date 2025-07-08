from vitrum.batch_active.learning import balace
import pickle
import os

print("Running")
try:
    ace.run()
except NameError:
    if os.path.isfile("balace.pickle"):
        file = open("balace.pickle",'rb')
        ace = pickle.load(file)
        ace.load_config()
        ace.set_defaults()
        ace.validate_config()
    else:
        ace = balace()
        print(ace.struc_gen_params)
    ace.run()
