import comp_prob_inference

# 1st approach
# Go with the mathematical definition of a random variable. 
# First, specify what the underlying probability space is:
prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

# Then provide a way to map from the sample space to the alphabet:
W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}

# Then we can generate a random sample/draw for random variables W and I:
random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = W_mapping[random_outcome]
I = I_mapping[random_outcome]

print(W, I)

# 2nd approach
# Remember how we wrote out probability tables for random variables W and I? 
# Let's directly store these probability tables:
W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
I_table = {0: 1/2, 1: 1/2}

# Treating the tables as probability spaces, draw samples for W and I:
W = comp_prob_inference.sample_from_finite_probability_space(W_table)
I = comp_prob_inference.sample_from_finite_probability_space(I_table)

print(W, I)
#Treating the tables as probability spaces, draw samples for W and I:

W = comp_prob_inference.sample_from_finite_probability_space(W_table)
I = comp_prob_inference.sample_from_finite_probability_space(I_table)
