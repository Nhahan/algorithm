genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, plays_array):
    genre_list = []
    genre_counts = {}
    genre_rank = []
    genre_dicts = []
    for i in range(len(genre_array)):
        genre_dicts.append({genre_array[i]: (plays[i], i)})
    for x in genre_array:
        if x not in genre_list:
            genre_list.append(x)
    for g in range(len(genre_array)):
        for genre in genre_list:
            if genre_array[g] == genre:
                if genre not in genre_counts:
                    genre_counts[genre] = plays_array[g]
                elif genre_counts[genre] < plays_array[g]:
                    genre_counts[genre] = plays_array[g]
    genre_counts_list = list(genre_counts)
    genre_counts_points = [0] * len(genre_counts_list)
    for n in range(len(genre_array)):
        for nl in range(len(genre_counts_list)):
            if genre_array[n] == genre_counts_list[nl]:
                genre_counts_points[nl] += plays_array[n]
    genre_counts = {name: value for name, value in zip(genre_counts_list, genre_counts_points)}
    for delete in range(len(genre_counts)):
        genre_rank.append(max(genre_counts, key=genre_counts.get))
        del genre_counts[max(genre_counts, key=genre_counts.get)]
    answer = list()
    for rank in genre_rank:  # pop, classic
        temp_rank_dicts = []
        for genre_dict in genre_dicts:  # [{'classic': 500}, {'pop': 600}, {'classic': 150}, {'classic': 800}, {'pop': 2500}]
            if rank in genre_dict:  # pop, classic
                temp_rank_dicts.append(genre_dict)
        temp_rank = list()
        temp_rank_list = list()
        temp_rank_checker = list()
        for t in range(
                len(temp_rank_dicts)):  # [{'pop': (600, 1)}, {'pop': (2500, 4)}]     # [{'classic': (500, 0)}, {'classic': (150, 2)}, {'classic': (800, 3)}]
            if len(temp_rank_dicts) == 2:
                temp_rank.append(temp_rank_dicts[t][rank][1])
            else:
                temp_rank_list.append(temp_rank_dicts[t][rank][0])
                if t is len(temp_rank_dicts) - 1:
                    temp_rank_list.sort(reverse=True)
                    temp_rank_list = temp_rank_list[:2]
                    for m in range(len(temp_rank_dicts)):
                        if temp_rank_dicts[m][rank][0] == temp_rank_list[0] and temp_rank_dicts[m][rank][1] not in temp_rank_checker:
                            temp_rank_checker.append((temp_rank_dicts[m][rank][0]))
                            temp_rank.append(temp_rank_dicts[m][rank][1])
                    for m in range(len(temp_rank_dicts)):
                        if temp_rank_dicts[m][rank][0] == temp_rank_list[1] and temp_rank_dicts[m][rank][1] not in temp_rank_checker:
                            temp_rank_checker.append((temp_rank_dicts[m][rank][0]))
                            temp_rank.append(temp_rank_dicts[m][rank][1])
        temp_rank.sort(reverse=True)
        answer += temp_rank
    return answer

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!

genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]
print(get_melon_best_album(genres, plays))  # 정답 = [0, 6, 5, 2, 4, 1]