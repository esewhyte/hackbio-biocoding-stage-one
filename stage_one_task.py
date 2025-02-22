# Define the codon-to-amino acid dictionary
codon_db = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu"
}


def translator(input_codon):
    """
    Translates an RNA sequence into a list of amino acids using the codon dictionary.
    
    :param input_codon: A string representing the RNA sequence.
    :return: A list of translated amino acids.
    """
    ribosome_output = []


    # Split the sequence into codons (every 3 nucleotides)
    for i in range(0, len(input_codon), 3):
        codon = input_codon[i:i+3]  # Extract codon (3 bases)
        amino_acid = codon_db.get(codon, "Unknown")  # Translate using dictionary
        ribosome_output.append(amino_acid)


    return ribosome_output


# Test the function
test_cd = "UUAUUAUUAUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCUUCUUCUUCUUC"
print(translator(test_cd))


#Writing a function that simulates and generates a logistic population growth curve


def population_maker(k=2, x_mid=5, x=None):
    """
    Generates logistic growth values based on the given parameters.
    
    :param k: Growth rate constant
    :param x_mid: Midpoint where growth slows down
    :param x: Input value or array of time points
    :return: Logistic function values
    """
    return 1 / (1 + np.exp(-k * (x - x_mid)))


# Generate OD600 values for x ranging from 0 to 24
x_values = np.arange(0, 25)  # Equivalent to 0:24 in R
od_600 = [population_maker(k=0.25, x_mid=10, x=i) for i in x_values]


# Plot the logistic growth curve
plt.plot(x_values, od_600, marker='o', linestyle='-')
plt.xlabel("Time")
plt.ylabel("OD600")
plt.title("Logistic Growth Curve")
plt.show()


import math
def population(x , k = 2, x_mid = 5):
    solution = 1/(1 + math.exp(-k*(x-x_mid)))
    return solution
print(population(k = 2, x_mid = 5, x = 10))
od_600 = []
for i in range(0,24):
    od_600.append(population(x = i, k = 0.5, x_mid = 10))
print(od_600)


#the function to generate 100 different growth curves.
def generate_growth_curves(num_curves, time_points):
    curves = {}
    for i in range(num_curves):
        curve = simulate_logistic_curve(time_points)
        curves["Curve_" + str(i + 1)] = curve
    return curves


#the function to determine the time when the growth curve reaches 80% of the carrying capacity.
def time_to_reach_80_percent(time_points, growth_curve, K=1):
    threshold = 0.8 * K
    for i in range(len(time_points)):
        if growth_curve[i] >= threshold:
            return time_points[i]
    return None




# the function for calculating the hamming distance between my Slack username and twitter/X handle


def hamming_distance(slack, twitter):
  #the shorter string will be padded with spaces so both have the same length
  if len(slack) < len(twitter):
    slack = slack + " " * (len(twitter) - len(slack))
  elif len(twitter) < len(slack):
    twitter = twitter + " " * (len(slack) - len(twitter))


  # the counter for hamming distance is initialized as zero
  distance = 0
  #next, the function is looped for each character
  for i in range(len(slack)):
    if slack[i] != twitter[i]:
      distance += 1
  return distance


# slack and twitter usernames
slack_username = "ese"
twitter_username = "esecynth"


# calculating and printing the final Hamming distance
result = hamming_distance(slack_username, twitter_username)
print("Hamming distance:", result)




# Repository link: https://github.com/esewhyte/hackbio-biocoding-stage-one
