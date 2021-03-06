def multiclass_accuracy(prediction, ground_truth):
    """
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    """

    # TODO: Implement computing accuracy
    #raise Exception("Not implemented!")
    correct = 0

    for i in range(ground_truth.shape[0]):
        if prediction[i] == ground_truth[i]:
            correct += 1

    if prediction.shape[0] != 0:
        accuracy = correct / prediction.shape[0]
    else:
        accuracy = 0

    return accuracy
