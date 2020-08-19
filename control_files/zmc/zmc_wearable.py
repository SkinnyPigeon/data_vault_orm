zmc_wearable_hubs = {
    'table': 'zmc.wearable',
    'hubs': [
        {
            'hub': 'zmc.hub_object',
            'keys': 'serums_id'
        },
        {
            'hub': 'zmc.hub_time',
            'keys': 'serums_id'
        }
    ]
}

zmc_wearable_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_object_exercise_measurements',
            'columns': [
                'nr_sst', 'steps_total', 'cadence', 'cyc_rot', 'cyc_rpm'
            ],
            'hub': 'zmc.hub_object',
            'hub_id': 0
        },
        {
            'satellite': 'zmc.sat_time_exercise_measurements',
            'columns': [
                'day_nr', 'time_total', 'time_passive', 'time_active', 'time_sit', 'time_stand', 'time_walk', 'time_cycle', 'time_hi'
            ],
            'hub': 'zmc.hub_time',
            'hub_id': 0
        }
    ]
}

zmc_wearable_links = {
    'links': [
        {
            'link': 'zmc.object_time_link'
        }
    ]
}