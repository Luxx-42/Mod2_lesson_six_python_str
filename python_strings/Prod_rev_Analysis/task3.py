#Task 3 review summary
def trim_the_tale(long_story, max_babble=30):
    if len(long_story) <= max_babble:
        return long_story

    dramatic_pause = long_story[:max_babble].rfind(" ")

    if dramatic_pause == -1:
        return long_story[:max_babble] + "..."

    return long_story[:dramatic_pause] + "..."

customer_tales = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

cliffhangers = [trim_the_tale(tale) for tale in customer_tales]

for cliffhanger in cliffhangers:
    print(f"Summary Review: {cliffhanger}")
