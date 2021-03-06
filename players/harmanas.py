def bet(bets, wealth, round):
  total_true, total_false = bets['total']
  players = len(wealth)
  ps[0] = float(total_true / (total_true + total_false))
  total = float((total_true + total_false)) / players

  # We can also see how much wealth a player has by querying wealth
  w_list = list(d.items())
  w_sorted = w_list.sort(key = lambda tup: tup[1])

  # This is wrong, it 's supposed to take an average.
  for i, w in enumerate(w_sorted[0: 3]):
      t, f = bets[w[0]]
  ps[i + 1] = t / (t + f)

  p = mean(ps)

  if round > 0:
      return (p * total, (1 - p) * total)
  else :
      return 0.0, 0.0

def mean(ps):
  return sum(ps) / len(ps)