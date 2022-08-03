def reward_function(params):
    
    center_variance = params["distance_from_center"] / params["track_width"]
    #racing line
    left_lane = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131]#Fill in the waypoints
    
    center_lane = [0,1,2,3,4,5,6,7,8,9,60,61,62,63,64,65,66,67,68,98,132,133,134]#Fill in the waypoints
    
    right_lane = [69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97]#Fill in the waypoints
    #Speed
    fast = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134]#Fill in the waypoints, 2m/s
    slow = []#Fill in the waypoints, 1m/s
    
    reward = 21.0

    if params["all_wheels_on_track"]:
        reward += 10.0
    else:
        reward -= 10.0

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10.0
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10.0
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10.0
    else:
        reward -= 10.0
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2.0 :
            reward += 10.0
        else:
            reward -= 10.0
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1.0 :
            reward += 10.0
        else:
            reward -= 10.0

    abs_steering = abs(params['steering_angle'])
    ABS_STEERING_THRESHOLD = 20 
    
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
        
    
    return float(reward)
        
    
    return float(reward)
