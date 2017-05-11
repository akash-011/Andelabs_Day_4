class BinarySearch(list):

  def __init__(self, a, b): #Creates list of length a with steps of b between elements
    self.a = a
    self.b = b
         
    for i in range(self.a):
      list.append(self, self.b)
      self.b +=b
      i +=1
  
    self.length = i

  def search(self,value):
    first = 0
    last = self.length-1
    found = False
    count = 0
    in_list = False
    try:
      index = self.index(value)
      in_list = True
    except ValueError:
      index = -1
      in_list = False

    while first<=last and not found and in_list and value != self[last]:
        mid_point = (first+last)//2
        if self[mid_point] == value:
            found = True
            count +=1
            index = mid_point
        else:
            if value < self[mid_point]:
                last = mid_point - 1
                count +=1
            else:
                first = mid_point + 1
                count +=1
    
    
    return {"count": count, "index": index}
