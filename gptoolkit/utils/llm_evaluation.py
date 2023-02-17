import math


def compute_perplexity(generated_text, desired_text):
    """Computes the perplexity of the generated text using the desired text as the probability distribution.

    Args:
        generated_text (str): The generated text to compute perplexity for.
        desired_text (str): The desired text to use as the probability distribution.

    Returns:
        float: The perplexity of the generated text.
    """
    # Split the generated and desired texts into individual tokens
    generated_tokens = generated_text.split()
    desired_tokens = desired_text.split()

    # Compute the entropy of the generated text
    entropy = 0.0
    for token in generated_tokens:
        if token not in desired_tokens:
            # Use a small probability for out-of-vocabulary tokens
            probability = 1e-10
        else:
            count = desired_tokens.count(token)
            probability = count / len(desired_tokens)
        entropy += math.log(probability, 2)

    entropy = -entropy / len(generated_tokens)

    # Compute the perplexity from the entropy
    perplexity = 2 ** entropy

    return perplexity

