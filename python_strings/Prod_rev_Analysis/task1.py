# Task 1 keyword highlighter
def zap_keywords_in_reviews(review_list, magic_words):
    zapped_reviews = []
    for thought_bubble in review_list:
        for magic_word in magic_words:
            thought_bubble = thought_bubble.replace(magic_word, magic_word.upper())
            thought_bubble = thought_bubble.replace(magic_word.capitalize(), magic_word.upper())
        zapped_reviews.append(thought_bubble)
    return zapped_reviews

def shout_highlights(zapped_reviews, magic_words):
    print("Supercharged Reviews")
    for thought_bubble in zapped_reviews:
        if any(word.upper() in thought_bubble for word in magic_words[:2]):
            print(f"*** {thought_bubble} ***")
        else:
            print(thought_bubble)

magic_words = ["good", "excellent", "bad", "poor", "average"]

thought_bubbles = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

supercharged_reviews = zap_keywords_in_reviews(thought_bubbles, magic_words)

shout_highlights(supercharged_reviews, magic_words)