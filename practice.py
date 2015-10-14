__author__ = 'bastanib'


def make_stream(start=0, f_next=lambda x: x+1):
  def stream():
    nonlocal start
    return_val = start
    start = f_next(start)
    return return_val
  return stream


# These are based on exercises from the book Cracking the Coding Interview, 5th Edition

# Page 52: Approach II: Pattern Matching
def find_split(split_sorted_list):

  # first gracefully handle bad inputs, i.e. lists of length <= 1
  length = len(split_sorted_list)
  if length <= 1:
    return 'list is too short'

  # recurse based on length

  # get the ends
  first = split_sorted_list[0]
  last = split_sorted_list[length-1]

  # base case: length == 2.  last should be less than first, else list was not split to begin with
  if length == 2:
    if last < first:
      return last
    else:
      return 'list was not split'

  # recursion: length > 2.  divide the list at the midpoint and recurse on the half that has last <
  else:
    midpoint = length//2
    mid = split_sorted_list[midpoint]
    if mid < first:
      return find_split(split_sorted_list[0:midpoint+1])
    else:
      return find_split(split_sorted_list[midpoint:length])
