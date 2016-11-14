# Basic calculation the Prob of the Event in terms of Probability theory

def prob_of_event(event, prob_space, total_prob=0):

    if sum(prob_space.values()) > 1:
        return "The Total Prob in Prob Space greater than 1, it's strange, bro... . Fix it."

    for outcome in event:
        total_prob += prob_space[outcome]
    return total_prob

weather_prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
rainy_or_snowy_event = {'rainy', 'snowy'}
print("The probabilty of rainy or snowy for Tomorrow is {}"\
    .format(prob_of_event(rainy_or_snowy_event, weather_prob_space)))
