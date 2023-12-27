import pandas as pd
def students_details():
    data = [
        {"roll_no": 1, "name": "John", "games": ["cricket", "football"],
        "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
        {"roll_no": 2, "name": "Mick", "games": ["football", "hockey"],
        "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
        {"roll_no": 3, "name": "June", "games": ["badminton", None],
        "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
        {"roll_no": 4, "name": "Adam", "games": ["soccer", "badminton"],
        "marks": {"maths": 86, "science": 91, "cs": 82}, "rank": 4},
        {"roll_no": 5, "name": "Robb", "games": ["cricket", None],
        "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
        {"roll_no": 6, "name": "Arya", "games": ["football", "hockey"],
        "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
    ]
    df = pd.DataFrame(data)
    cs_students = df[df['marks'].apply(lambda x: 'cs' in x.keys() if isinstance(x, dict) else False)]
    print(cs_students)
    df['Percentage'] = df['marks'].apply(lambda x: (3 * x.get('maths', 0) + 2 * x.get('science', 0) +
                                                    sum([v for k, v in x.items() if k not in ['maths', 'science']])))
    df['Percentage'] /= 6
    df['games'] = df['games'].apply(lambda x: [game for game in x if pd.notnull(game)])
    print(df)
    df['Previous Rank'] = df['rank']
    df['rank'] = df['Percentage'].rank(ascending=False).astype(int)
    df['Change in Rank'] = df.apply(lambda x: -(x['rank'] - x['Previous Rank']) if x['rank'] != x['Previous Rank']  else '-', axis=1)
    result_df = df[['name', 'Percentage', 'Previous Rank', 'rank', 'Change in Rank']].sort_values(by='rank')
    print(result_df)
students_details()
