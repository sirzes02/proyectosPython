# Addition of vectors

height_weight_age = [70, 170, 40, 0]
grades = [95, 80, 75, 62]


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


print(vector_add(height_weight_age, grades))


# Dot product

def dot(v, w):
    return [v_i * w_i for v_i, w_i in zip(v, w)]


print(dot(height_weight_age, grades))
