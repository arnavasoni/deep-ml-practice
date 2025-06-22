def disorder(apples: list) -> float:

    if not apples:
       return 0.0

    volume = len(apples) # total number of apples
    app_colors_count = {color: apples.count(color) for color in set(apples)} # color wise count of apples

    freq_list_sq = [(count / volume) ** 2 for count in app_colors_count.values()]
    G = 1 - sum(freq_list_sq) # Gini calculation

    # theory written in Notion.
    
    return float(G)