import pandas as pd
from matplotlib import *
from matplotlib.pyplot import *

test_log = pd.read_csv("./log/model.log.test")
_, ax1 = subplots(figsize=(15, 10))
ax1.plot(test_log["NumIters"], test_log["loss"], 'g')
ax1.set_xlabel('iteration')
ax1.set_ylabel('test loss')
savefig("./test_loss.png") #save image as png


train_log = pd.read_csv("./log/model.log.train")
_, ax1 = subplots(figsize=(15, 10))
ax1.plot(train_log["NumIters"][1:], train_log["loss"][1:], 'g')
ax1.set_xlabel('iteration')
ax1.set_ylabel('train loss')
savefig("./train_loss.png") #save image as png
