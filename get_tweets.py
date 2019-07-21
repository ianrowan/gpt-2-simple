import twint
import os
import csv
import numpy as np

continuous = False
base_path = os.path.dirname(os.path.realpath(__file__))
name = input("Twitter User: @")
c = twint.Config()

c.Username = name
c.Store_csv = True
# CSV Fieldnames
c.Custom["tweet"] = ["tweet"]
# Name of the directory
save_dir = base_path + "/data/{}.csv".format(name)
open(save_dir, "w")
c.Output = save_dir

twint.run.Search(c)

with open(save_dir, "r") as csvfile:
    data = np.asarray([i for i in csv.reader(csvfile)])


data_final = np.asarray([[i[0]] for i in data if "/" not in i[0] and "0" not in i[0]])
text = ""
if not continuous:
    np.savetxt(save_dir, data_final, fmt='%s')

    with open(save_dir, "r") as csvfile:
        for i in csvfile:
            text = text + str(i)

else:
    for i in data_final:
        text += str(i[0])

np.savetxt(base_path + "/data/{}.txt".format(name), np.asarray([text]), fmt='%s')