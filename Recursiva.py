def inverter_string(X):
    if len(X) == 0:
        return ""
    else:
        return X[-1] + inverter_string(X[:-1])

print(inverter_string("recursao"))