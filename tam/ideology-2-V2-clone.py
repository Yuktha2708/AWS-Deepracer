def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    track_length = params['track_length']
    is_left_of_center = params['is_left_of_center']
    steps = params['steps']
    progress = params['progress']

    
    radius = track_length*0.16
    
    
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 3.0

    
    # Give a very low reward by default
    reward = 1e-3
    
    if is_left_of_center == True:
        if radius<(radius - distance_from_center):
            reward= 2.0
        else:
            reward = 1e-3
    else:
            reward = 1e-3
    
    TOTAL_NUM_STEPS = 250
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    # Always return a float value
    return float(reward)
