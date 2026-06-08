# ──────────────────────────────────────────────
#  Movie Recommendation System — Python
#  Technique: Cosine Similarity on user preferences
# ──────────────────────────────────────────────

# ── 1. Movie Catalog ───────────────────────────
MOVIES = [
    {"title": "Inception",               "year": 2010, "rating": 8.8, "genres": ["Sci-Fi","Thriller"],        "moods": ["Mind-bending","Exciting"]},
    {"title": "The Dark Knight",         "year": 2008, "rating": 9.0, "genres": ["Action","Thriller"],         "moods": ["Exciting","Mind-bending"]},
    {"title": "Interstellar",            "year": 2014, "rating": 8.6, "genres": ["Sci-Fi","Drama"],            "moods": ["Emotional","Mind-bending","Inspiring"]},
    {"title": "The Shawshank Redemption","year": 1994, "rating": 9.3, "genres": ["Drama"],                     "moods": ["Inspiring","Emotional"]},
    {"title": "Parasite",                "year": 2019, "rating": 8.5, "genres": ["Thriller","Drama"],          "moods": ["Mind-bending","Scary"]},
    {"title": "The Shining",             "year": 1980, "rating": 8.4, "genres": ["Horror","Thriller"],         "moods": ["Scary","Mind-bending"]},
    {"title": "Spirited Away",           "year": 2001, "rating": 8.6, "genres": ["Animation","Drama"],         "moods": ["Inspiring","Emotional"]},
    {"title": "Superbad",                "year": 2007, "rating": 7.6, "genres": ["Comedy"],                    "moods": ["Funny","Relaxing"]},
    {"title": "La La Land",              "year": 2016, "rating": 8.0, "genres": ["Romance","Drama"],           "moods": ["Emotional","Inspiring"]},
    {"title": "Mad Max: Fury Road",      "year": 2015, "rating": 8.1, "genres": ["Action"],                    "moods": ["Exciting"]},
    {"title": "Get Out",                 "year": 2017, "rating": 7.7, "genres": ["Horror","Thriller"],         "moods": ["Scary","Mind-bending"]},
    {"title": "Amélie",                  "year": 2001, "rating": 8.3, "genres": ["Romance","Comedy"],          "moods": ["Funny","Emotional","Relaxing"]},
    {"title": "The Grand Budapest Hotel","year": 2014, "rating": 8.1, "genres": ["Comedy","Drama"],            "moods": ["Funny","Exciting"]},
    {"title": "Planet Earth II",         "year": 2016, "rating": 9.5, "genres": ["Documentary"],               "moods": ["Inspiring","Relaxing"]},
    {"title": "Toy Story",               "year": 1995, "rating": 8.3, "genres": ["Animation","Comedy"],        "moods": ["Funny","Inspiring","Emotional"]},
    {"title": "Whiplash",                "year": 2014, "rating": 8.5, "genres": ["Drama","Thriller"],          "moods": ["Inspiring","Exciting"]},
    {"title": "Knives Out",              "year": 2019, "rating": 7.9, "genres": ["Thriller","Comedy"],         "moods": ["Funny","Mind-bending","Exciting"]},
    {"title": "Her",                     "year": 2013, "rating": 8.0, "genres": ["Sci-Fi","Romance","Drama"],  "moods": ["Emotional","Mind-bending"]},
    {"title": "The Notebook",            "year": 2004, "rating": 7.8, "genres": ["Romance","Drama"],           "moods": ["Emotional","Relaxing"]},
]

ALL_GENRES = ["Action","Comedy","Drama","Horror","Sci-Fi","Romance","Thriller","Animation","Documentary"]
ALL_MOODS  = ["Exciting","Relaxing","Emotional","Funny","Scary","Inspiring","Mind-bending"]


# ── 2. Similarity Function ─────────────────────
def cosine_similarity(user_genres, user_moods, movie):
    """
    Score calculate karo user preferences aur movie ke beech.
    Genre match = 2 points, Mood match = 1.5 points
    Score = actual_matches / max_possible  → [0, 1]
    """
    score = 0
    for g in user_genres:
        if g in movie["genres"]:
            score += 2
    for m in user_moods:
        if m in movie["moods"]:
            score += 1.5

    max_possible = len(user_genres) * 2 + len(user_moods) * 1.5
    return round(score / max_possible, 4) if max_possible > 0 else 0


# ── 3. Recommendation Engine ──────────────────
def recommend(user_genres, user_moods, min_rating=7.0, top_n=5):
    """
    User ki preferences le, similar movies dhundo.

    Args:
        user_genres : list  e.g. ["Sci-Fi", "Thriller"]
        user_moods  : list  e.g. ["Exciting", "Mind-bending"]
        min_rating  : float minimum IMDb rating
        top_n       : int   kitni recommendations chahiye

    Returns:
        list of dicts sorted by similarity score
    """
    results = []

    for movie in MOVIES:
        if movie["rating"] < min_rating:
            continue
        sim = cosine_similarity(user_genres, user_moods, movie)
        if sim > 0:
            results.append({**movie, "score": sim})

    # Sort by score, then rating as tiebreaker
    results.sort(key=lambda x: (x["score"], x["rating"]), reverse=True)
    return results[:top_n]


# ── 4. Display Helper ─────────────────────────
def display_recommendations(recs):
    if not recs:
        print("  Koi match nahi mila. Rating kam karo ya genres badlo.\n")
        return

    for i, m in enumerate(recs, 1):
        bar_len = int(m["score"] * 20)
        bar     = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {i}. {m['title']} ({m['year']})  ★ {m['rating']}")
        print(f"     Match: [{bar}] {int(m['score']*100)}%")
        print(f"     Genres: {', '.join(m['genres'])}  |  Moods: {', '.join(m['moods'])}")
        print()


# ── 5. User Input Loop ────────────────────────
def get_user_preferences():
    print("\n" + "=" * 55)
    print("  Movie Recommendation System")
    print("=" * 55)

    print("\nAvailable Genres:")
    for i, g in enumerate(ALL_GENRES, 1):
        print(f"  {i:>2}. {g}")

    genre_input = input("\nGenre numbers daalo (e.g. 1 3 5): ").strip()
    selected_genres = []
    for idx in genre_input.split():
        if idx.isdigit() and 1 <= int(idx) <= len(ALL_GENRES):
            selected_genres.append(ALL_GENRES[int(idx) - 1])

    print("\nAvailable Moods:")
    for i, m in enumerate(ALL_MOODS, 1):
        print(f"  {i:>2}. {m}")

    mood_input = input("\nMood numbers daalo (e.g. 1 3): ").strip()
    selected_moods = []
    for idx in mood_input.split():
        if idx.isdigit() and 1 <= int(idx) <= len(ALL_MOODS):
            selected_moods.append(ALL_MOODS[int(idx) - 1])

    rating_input = input("\nMinimum rating (default 7.0): ").strip()
    min_rating = float(rating_input) if rating_input else 7.0

    return selected_genres, selected_moods, min_rating


# ── 6. Main ───────────────────────────────────
def main():
    # --- Interactive mode ---
    try:
        genres, moods, min_rating = get_user_preferences()

        print(f"\nTumhari choices:")
        print(f"  Genres : {genres if genres else 'koi nahi'}")
        print(f"  Moods  : {moods  if moods  else 'koi nahi'}")
        print(f"  Rating : {min_rating}+")

        if not genres and not moods:
            print("\n  Kuch to select karo bhai!")
            return

        recs = recommend(genres, moods, min_rating=min_rating, top_n=5)

        print(f"\nTop recommendations ({len(recs)} milein):\n")
        display_recommendations(recs)

    except (EOFError, KeyboardInterrupt):
        # --- Demo mode (non-interactive) ---
        print("\n[Demo Mode] Running preset example...\n")

        examples = [
            (["Sci-Fi","Thriller"], ["Mind-bending","Exciting"], 8.0),
            (["Comedy","Romance"],  ["Funny","Relaxing"],        7.5),
            (["Drama"],             ["Inspiring","Emotional"],   8.0),
        ]

        for genres, moods, rating in examples:
            print("=" * 55)
            print(f"  Genres : {genres}")
            print(f"  Moods  : {moods}")
            print(f"  Rating : {rating}+")
            print("=" * 55)
            recs = recommend(genres, moods, min_rating=rating, top_n=3)
            print(f"\nTop {len(recs)} recommendations:\n")
            display_recommendations(recs)


if __name__ == "__main__":
    main()
