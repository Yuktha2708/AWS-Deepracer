def reward_function(params):
    # Example of penalize steering, which helps mitigate zig-zag behaviors

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    is_left_of_center = params['is_left_of_center']

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if is_left_of_center == True:
        if distance_from_center <= marker_1:
            reward = 0.5
        elif distance_from_center <= marker_2:
            reward = 1.0
        elif distance_from_center <= marker_3:
            reward = 0.1
        else:
            reward = 1e-3  # likely crashed/ close to off track
   
    else:
        reward = 1e-3

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 30 
    
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
        
    return float(reward)
