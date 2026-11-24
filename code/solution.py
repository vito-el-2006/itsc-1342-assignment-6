# Vittorio Enzo Lester - Assignment 6

def filter_critical_scores(score_list: list[int], min_severity=70):
	critical_scores = []
	# TODO: Filter and cap scores according to the prompt
	for score in score_list:
		add_score = score
		if score > min_severity:
			if score > 100:
				add_score = 100
			critical_scores.append(add_score)
	return critical_scores
