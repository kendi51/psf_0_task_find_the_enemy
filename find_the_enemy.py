def find_the_enemy(arr):
    # create a var to contain the list of tuples for the 2's pos(x, y)
    two_pos = []
    # create a var to store the distance
    total_dis = []
    # create variables to store column len and row len
    num_cols = len(arr[0])
    num_rows = len(arr)
    for i in range(num_rows):
        # find the position of 1 (x, y)
        if "1" in arr[i]:
            for j in range(num_cols):
                if arr[i][j] == "1":
                    one_row = i
                    one_col = j

        # find the position of the enemy 2 => (x, y)
        if "2" in arr[i]:
            for j in range(num_cols):
                if arr[i][j] == "2":
                    two_pos.append((i, j))
    if not two_pos:
        return 0
    # find the horizontal distance
    for pos in two_pos:
        h_direct_dis = abs(one_col - pos[1])
        h_wrapped_dis = num_cols - h_direct_dis
        h_min = min(h_direct_dis, h_wrapped_dis)

        # find the vertical distance
        v_direct_dis = abs(one_row - pos[0])
        v_wrapped_dis = num_rows - v_direct_dis
        v_min = min(v_direct_dis, v_wrapped_dis)

        total_dis.append(v_min + h_min)

    return min(total_dis)
