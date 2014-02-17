
def make_new_row(old_row):
    """Requires:
       -- list old_row that begins and ends with a 1 and has zero or more
          integers in between (has to have at least [1,1])
       Returns:
       -- list beginning and ending with a 1 and each interior (non 1)
          integer is the sum of the corresponding old_row elements
          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """

    
