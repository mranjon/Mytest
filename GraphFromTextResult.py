# Heleo


path = "./output.txt"

model1_loss = []
model2_acc = []
model3_acc = []
model1_val_loss = []
model2_val_acc = []
model3_val_acc = []


# return the search string accuracy or loss(what you want) value in integer from a line
def get_search_value(line, search_string):
    value = 0
    if (line.find(search_string) != -1):
        word_list = line.split(" ")
        temp_index = word_list.index(search_string[:len(search_string)])
        value =word_list[temp_index+1]
        value = value[0:6]
    return float(value)



def filterAndAppend(list, value):
    if value!=0:
        list.append(value)



with open(path) as f:
    for line in f:
        print line

        filterAndAppend(model1_loss, get_search_value(line, search_string="model1_loss:"))
        filterAndAppend(model1_val_loss, (get_search_value(line, "val_model1_loss:")))

        filterAndAppend(model2_acc, (get_search_value(line, "model2_acc:")))
        filterAndAppend(model2_val_acc, (get_search_value(line, "val_model2_acc:")))

        filterAndAppend(model3_acc, (get_search_value(line, "model3_acc:")))
        filterAndAppend(model3_val_acc, (get_search_value(line, "val_model3_acc:")))





import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)

plt.plot(x, model1_loss)
plt.plot(x, model1_val_loss)
plt.plot(x, model2_acc)
plt.plot(x, model2_val_acc)
plt.plot(x, model3_acc)
plt.plot(x, model3_val_acc)
plt.legend(['Model 1 loss', 'Model 1 validation loss', 'Model 2 Accuracy',
            'Model 2 validation Accurays', 'Model 3 Accuracy',
            'Model 3 validation Accurays', ], loc='center left', bbox_to_anchor=(.5, 0.6))

plt.show()


print model1_loss
print model2_acc
print model3_acc
print model1_val_loss
print model2_val_acc
print model3_val_acc

