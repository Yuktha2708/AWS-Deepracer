def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 2.0
        
    if is_left_of_center == True:
        reward = 1.5
        
    SPEED_THRESHOLD = 2.0
    if speed >= SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 0.5
    elif speed < SPEED_THRESHOLD:
        reward = 1e-3

    # Always return a float value
    return float(reward)
