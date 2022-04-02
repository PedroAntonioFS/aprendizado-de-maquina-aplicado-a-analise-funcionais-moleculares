import numpy as np
from math import ceil
from sklearn.model_selection import KFold
import tensorflow as tf
import gc

def train_test_split_per_class(x, y, test_size=0.3):
    test_indexes = []

    for label in np.unique(y):
        indexes = np.where(y == label)[0]

        test_indexes.extend(np.random.choice(indexes, ceil(test_size*indexes.size), False))

    x_train = x[[i for i in range(len(x)) if i not in test_indexes]]
    y_train = y[[i for i in range(len(y)) if i not in test_indexes]]
    x_test  = x[test_indexes]
    y_test  = y[test_indexes]
    

    return x_train, x_test, y_train, y_test

def cross_validation(x, y, model, k_folds, optimizer, loss, metrics, epochs, batch_size):
    kf = KFold(n_splits=k_folds, shuffle=True)
    
    iteration = 1
    results = []
    for train_index, test_index in kf.split(x,y):
        tf.keras.backend.clear_session()
        gc.collect()
        try:
            del model_clone
        except NameError:
            pass

        print('Fold {}'.format(iteration))
        model_clone = tf.keras.models.clone_model(model)
        model_clone.compile(optimizer = optimizer, loss=loss, metrics=metrics)

        x_train, X_test = x[train_index], x[test_index]
        y_train, y_test = tf.one_hot(y[train_index], 5), tf.one_hot(y[test_index], 5)

        model_clone.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

        results.append(model_clone.evaluate(X_test, y_test))
        
        iteration+=1

    return results

def cross_validation_per_class(x, y, model, k_folds, optimizer, loss, metrics, epochs, batch_size):
    unique_labels = np.unique(y)
    for label in unique_labels:
        k_folds = min(k_folds, len(np.where(y == label)[0]))
    
    folds = []
    for label in unique_labels:
        label_index = (np.where(y == label)[0])
        np.random.shuffle(label_index)
        label_folds = np.array_split(label_index, k_folds)
        folds.append(label_folds)

    results = []
    for i in range(k_folds):
        test_folds = []
        train_folds = []
        for label_folds in folds:
            test_folds.append(label_folds[i])
            train_folds.extend(label_folds[:i])
            train_folds.extend(label_folds[i+1:])
        
        test_index = np.concatenate(test_folds)
        train_index = np.concatenate(train_folds)

        tf.keras.backend.clear_session()
        gc.collect()
        try:
            del model_clone
        except NameError:
            pass

        print('Fold {}/{}'.format(i, k_folds))
        model_clone = tf.keras.models.clone_model(model)
        model_clone.compile(optimizer = optimizer, loss=loss, metrics=metrics)

        x_train, X_test = x[train_index], x[test_index]
        y_train, y_test = tf.one_hot(y[train_index], 5), tf.one_hot(y[test_index], 5)

        model_clone.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

        results.append(model_clone.evaluate(X_test, y_test))

    return results

def over_sampling(x, y, labels, size=0):
    if size <= 0:
        for label in list(set(np.unique(y)) - set(labels)):
            index = np.where(y==label)[0]
            size = len(index) if size==0 else min(size, len(index))

    if size <= 0:
        return x,y

    samples = []
    for label in labels:
        index = np.where(y==label)[0]
        
        if len(index) < size:
            diff = size - len(index)
            new_samples1 = diff // len(index)
            new_samples2 = diff % len(index)

            index = np.concatenate((np.repeat(index, new_samples1), np.random.choice(index, new_samples2, False)))
            
        samples.extend(index)
        
    x_samples = x[samples]
    y_samples = y[samples]
    
    return np.concatenate((x,x_samples)), np.concatenate((y,y_samples))

def over_sampling_cv(x, y, model, k_folds, optimizer, loss, metrics, epochs, batch_size, sampling_labels, size=0):
    unique_labels = np.unique(y)
    for label in unique_labels:
        k_folds = min(k_folds, len(np.where(y == label)[0]))
    
    folds = []
    for label in unique_labels:
        label_index = (np.where(y == label)[0])
        np.random.shuffle(label_index)
        label_folds = np.array_split(label_index, k_folds)
        folds.append(label_folds)

    results = []
    for i in range(k_folds):
        test_folds = []
        train_folds = []
        for label_folds in folds:
            test_folds.append(label_folds[i])
            train_folds.extend(label_folds[:i])
            train_folds.extend(label_folds[i+1:])
        
        test_index = np.concatenate(test_folds)
        train_index = np.concatenate(train_folds)

        tf.keras.backend.clear_session()
        gc.collect()
        try:
            del model_clone
        except NameError:
            pass

        print('Fold {}/{}'.format(i, k_folds))
        model_clone = tf.keras.models.clone_model(model)
        model_clone.compile(optimizer = optimizer, loss=loss, metrics=metrics)

        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], tf.one_hot(y[test_index], 5)
        
        x_sampled, y_sampled = over_sampling(x_train, y_train, sampling_labels)
        y_sampled = tf.one_hot(y_sampled, 5)

        model_clone.fit(x_sampled, y_sampled, epochs=epochs, batch_size=batch_size, verbose=0)

        results.append(model_clone.evaluate(x_test, y_test))

    return results
