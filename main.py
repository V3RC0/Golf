from fractions import Fraction


def basic():
    event_A = int(input("Expected Outcome: ")) # expected outcome
    event_B = int(input("Sample Spaces: ")) # sample spaces
    return Fraction(event_A, event_B)



def conditional():
    # Take input as a string
    inputA = input("Enter A List separated by space: ")
    inputB = input("Enter B List separated by space: ")

    # Split the input string into a list of strings
    ListA = inputA.split()
    ListB = inputB.split()

    # Convert the list of strings to a list of integers
    nListA = list(map(int, ListA))
    nListB = list(map(int, ListB))
 
    event_AnB = list(set(nListA) & set(nListB))
    final = Fraction(len(event_AnB),len(nListB))
    print(event_AnB)
    # event B is the boundary
    return final

def bayes():
    # Calculate the probability of A given B using Bayes' theorem
    p_a = float(input("A: ")) # Probability of A
    p_b_given_a = float(input("B given A: "))  # Probability of B given A (P(B I A) probability we see B if hypothesis are True)
    p_b_given_not_a = float(input("B given not A: "))  # Probability of B given not A

    p_not_a = 1 - p_a
    p_b = (p_a * p_b_given_a) + (p_not_a * p_b_given_not_a)
    p_a_given_b = (p_a * p_b_given_a) / p_b
    return p_a_given_b



print("Probability is ", basic())

print("-" * 100)

print("Probability is ", conditional())

print("-" * 100)

print(f"The probability of A given B is {bayes():.2f}")