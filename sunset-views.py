"""
    Given an array of buildings and a direction that all of the buildings face,
    return an array of the indices of the buildings that can see the sunset.

    A building can see the sunset if it's strictly taller than all of the
    buildings that come after it in the direction that it faces.

    The input array named buildings contains positive, non-zero
    integers representing the heights of the buildings. A building at index
    i thus has a height denoted by buildings[i]. All of the buildings face the 
    same direction, and this direction is either east or west, denoted by the 
    input string named direction, which will always be equal to either "EAST" 
    or "WEST". In relation to the input array, you can interpret these directions as 
    right for east and left for west.
  
    Note: The indices in the output array should be sorted in ascending order. 

    Example:
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"

        Output:
            [1, 3, 6, 7]
"""
def sunsetViews(buildings, direction):
    views = []
    tallest = None
    is_east = direction.upper() == "EAST"
    st = [i for i in range(len(buildings))]  

    if is_east:
        buildings = reversed(buildings)

    for building in buildings:
        idx = st.pop() if is_east else st.pop(0)

        if tallest is None or tallest < building:
            if is_east:
                views.insert(0, idx)
            else:
                views.append(idx)

            tallest = building
    
    return views

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "east"))