#Task 2 sentiment tally
def tally_glowing_words(scribble, happy_vocab):
    sparkle_points = 0
    for doodle in scribble.split():
        if doodle.lower() in happy_vocab:
            sparkle_points += 1
    return sparkle_points

def tally_grumpy_words(scribble, grumpy_vocab):
    gloom_points = 0
    for doodle in scribble.split():
        if doodle.lower() in grumpy_vocab:
            gloom_points += 1
    return gloom_points

scribbles = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

happy_vocab = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
grumpy_vocab = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for scribble in scribbles:
    sparkle_count = tally_glowing_words(scribble, happy_vocab)
    gloom_count = tally_grumpy_words(scribble, grumpy_vocab)

    print(f"Scribble: '{scribble}'")
    print(f"Sparkle Words Count: {sparkle_count}")
    print(f"Gloom Words Count: {gloom_count}")
    print()