def calculate_f1_score(y_true, y_pred):
    tp,fp, tn, fn = 0, 0, 0, 0
    for s in zip(y_true, y_pred):
        if s[0] == 1 and s[1] == 1:
            tp += 1
        elif s[0] == 0 and s[1] == 1:
            fp += 1
        elif s[0] == 0 and s[0] == 0:
            tn += 1
        else:
            fn += 1
    if ((tp + fp) == 0 or (tp + fn) == 0):
        return 0.0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return round(f1, 3)