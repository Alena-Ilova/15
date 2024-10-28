def cut_rod(n, prices):

  dp = [0] * (n + 1) 

  cut_points = [0] * (n + 1)

  dp[0] = 0

  for i in range(1, n + 1):

    max_value = 0
    cut_point = 0

    for j in range(1, i + 1):
      current_value = prices[j - 1] + dp[i - j]

      if current_value > max_value:
        max_value = current_value
        cut_point = j

    dp[i] = max_value
    cut_points[i] = cut_point

  recommended_lengths = []
  current_length = n

  while current_length > 0:
    recommended_lengths.append(cut_points[current_length])

    current_length -= cut_points[current_length]

  return recommended_lengths[::-1]

rod_length = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]

recommended_lengths = cut_rod(rod_length, prices)

print("Recommended lengths:", recommended_lengths)