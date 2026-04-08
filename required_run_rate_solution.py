# Write your solution here
def run_rate(runs_to_win,overs_remaining):
    required_run_rate = runs_to_win/overs_remaining
    return required_run_rate
runs_to_win = int(input())
overs_remaining = float(input())
a=run_rate(runs_to_win,overs_remaining)
print(round(a,2))