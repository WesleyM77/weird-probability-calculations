import random
import matplotlib.pyplot as plt

loops = 10000
buttonRange = 5001
start = 71
end = 69
successes = 0

oddsX = []
oddsY = []

print(str(loops) + ' iterations allowed per cycle.')
for buttonLimit in range(buttonRange):
    for x in range(loops):
        temp = start
        for y in range(buttonLimit):
            direction = random.choice([-1, 1])
            temp += direction

            if temp == end:
                successes += 1
                break

    prob = (successes/loops) * 100
    print('For button limit=' + str(buttonLimit))
    print(str(round(prob, 2)) + '% chance when allowed ' +
          str(buttonLimit) + ' button presses before stopping.')
    print('=======================================================================')
    oddsX.append(buttonLimit)
    oddsY.append(prob/100)
    successes = 0

print(oddsX)
print(oddsY)
plt.plot(oddsX, oddsY)

# naming the x axis
plt.xlabel('Button Presses Allowed')
# naming the y axis
plt.ylabel('Probability of reducing temp by 2 degrees')

# giving a title to my graph
plt.title('Temp Probability!')

# function to show the plot
plt.show()