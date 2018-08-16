from read_csv import load_data_from_csv
import os
import numpy as np


def create_data_set(csv_files_dir):
    full_data_set = []
    for file in os.listdir(csv_files_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(csv_files_dir, file)
            full_data_set.extend(load_data_from_csv(file_path))
    return full_data_set

def shuffle_data_set(data_set):
    np_data_set = np.array(data_set)
    np.random.shuffle(np_data_set)
    return np_data_set

def create_training_data(shuffled_data_set):
    idx = int(len(shuffled_data_set) * (4/5))
    train_data = shuffled_data_set[:idx]
    return train_data

def create_dev_data(shuffled_data_set):
    idx = int(len(shuffled_data_set) * (4/5))
    dev_data = shuffled_data_set[idx:]
    return dev_data

full_data_set = create_data_set('csv_files')
shuffled_data_set = shuffle_data_set(full_data_set)
train_data = create_training_data(shuffled_data_set)
dev_data = create_dev_data(shuffled_data_set)

print(len(train_data))
print(len(dev_data))

print(train_data)
print(dev_data)