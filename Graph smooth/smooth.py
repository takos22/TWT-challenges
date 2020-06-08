import matplotlib.pyplot as plt
import json
import random


def smooth(points: list, max_width: int = 501) -> list:
    """Makes a graph line smoother "to capture important patterns in the data, while leaving out noise or other fine-scale structures/rapid phenomena" - Wikipedia.
    
    Arguments:
        points (list of int): list of the y points to smooth.
    Keyword arguments:
        max_width (int): width of the average for each point. The higher it is, the smoother the curve gets. (default: 501)
    
    Returns:
        list: list of the smoothed y points.
    """

    smooth_points = points.copy()
    for i in range(len(points)):
        # start of the average of points (i-250 | 0 if i < 250 | i - distance to len if i > len-250)
        min_i = max((i-(max_width-1)//2, 0)) if i+(max_width-1)//2 <= len(points) else -len(points) + 2*i

        # end of the average of points (i+250 | len if i > len-250 | i + distance to 0 if i < 250)
        max_i = min((i+(max_width-1)//2, len(points))) if i-(max_width-1)//2 >= 0 else 2*i + 1

        # average of his value the 500 neighbouring points' value
        smooth_points[i] = sum(points[min_i: max_i]) / (max_i - min_i)
    return smooth_points

def multi_smooth(points: list, iterations: int, max_width: int = 501) -> list:
    for i in range(iterations):
        points = smooth(points, max_width=max_width)
    return points

def noise(length, variation = 1, noise = 10):
    points = [0]
    points.append(random.uniform(points[-1]-variation, points[-1]+variation))
    for i in range(length-2):
        points.append(random.uniform(sum(points[-2:])/2-variation, sum(points[-2:])/2+variation))
    for i,p in enumerate(points):
        points[i] = p + random.uniform(-noise, noise)
    return points

def noise2(amount = 2000, oscilation = 1, noise = 10, randomNoise = False, save = False, name = "data"):
    data = []

    previous = 0
    noiseDir = -1
    for i in range(amount):
        deviation = random.randint(-oscilation, oscilation)
        data.append(previous+deviation+(noise*noiseDir))
        if randomNoise:
            noiseDir = random.randint(-1, 1)
        else:
            if noiseDir == -1:
                noiseDir = 1
            else:
                noiseDir = -1
        previous = previous+deviation
    
    if save:
        with open(f"{name}.json", 'w') as f:
            json.dump(data, f)

    return data

# lambda of smooth() bcs i hate myself
smooth_lambda = lambda points:[sum(points[(max((i-250,0))if i+250<=len(points)else-len(points)+2*i):(min((i+250,len(points)))if i>=250 else 2*i+1)])/((min((i+250,len(points)))if i>=250 else 2*i+1)-(max((i-250,0))if i+250<=len(points)else-len(points)+2*i))for i in range(len(points))]


# with open("Graph smooth/data.json") as f:
#     data = json.load(f)

data = noise2(5000)

plt.plot(data)
plt.plot(smooth(data), color="red")
plt.plot(multi_smooth(data, 20, 75), color="yellow")
# plt.plot(smooth_lambda(data), color="green")
plt.show()
