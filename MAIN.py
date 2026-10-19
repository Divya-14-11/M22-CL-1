import matplotlib.pyplot as plt
weights = [2.5,3.0 ,4.5,5.0,6.5,7.0,8.0,9.5]
heights = [20,22,25,27,40,42,45,48]
lables = ["cat","cat","cat","cat","dogs","dogs","dogs","dogs"]
for w,h,l in zip(weights,heights,lables):
    print(f"{w} kg,{h} cm,{l}")
def rule_based_classifier(weights,heights):
    if weights < 5 and heights < 30:
        return "cat"
    else:
        return "dog"
print(rule_based_classifier(2.5,20))
print(rule_based_classifier(25,200))

avg_weight_dog = (6.5 + 7.0 + 8.0 + 9.5)/4
avg_weight_cat = (2.5 + 3.0 + 4.5 + 5.0)/4
avg_height_dog = (40 + 42 + 45 + 48)/4
avg_height_cat = (20 + 22 + 25 + 27)/4
print(f"avg_weight_dog = {avg_weight_dog}")
print(f"avg_weight_cat = {avg_weight_cat}")
print(f"avg_height_dog = {avg_height_dog}")
print(f"avg_height_cat = {avg_height_cat}")

