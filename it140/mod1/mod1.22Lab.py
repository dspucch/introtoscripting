age = float(input())
weight = float(input())
hr = float(input())
time = float(input())

calories_women = float(((age * 0.074) + (weight * 0.05741) + (hr * 0.4472) - 20.4022)) * time / 4.184
calories_men = float(((age * 0.2017) + (weight * 0.09036) + (hr * 0.6309) - 55.0969)) * time / 4.184
print('Women: {:.2f} calories'.format(calories_women))
print('Men: {:.2f} calories'.format(calories_men))
