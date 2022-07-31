def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    track_length = params['track_length']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    
    radius = track_length*0.16
    
    # Give a very low reward by default
    reward = 1e-3
    
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track == True:
        if is_left_of_center == True:
            if distance_from_center == 0.25 * track_width:
                reward= 3.0
    
    else:
        reward = 1e-3
    
    ABS_STEERING_THRESHOLD = 15 
    
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8


    SPEED_THRESHOLD = 1.0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 0.5
    else:
        # High reward if the car stays on track and goes fast
        reward = 2.0

    # Always return a float value
    return float(reward)
