zmc_patient_details_hubs = {
    'table': 'zmc.patient_details',
    'hubs': [
        {
            'hub': 'zmc.hub_person',
            'keys': 'serums_id'
        },
        {
            'hub': 'zmc.hub_location',
            'keys': 'serums_id'
        }
    ]
}

zmc_patient_details_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_person_demographic_details',
            'columns': [
                'patnr', 'gschl', 'nname', 'nnams', 'vname', 'titel', 'namzu', 'gbdat', 'gbnam', 'gbnas', 'gland', 'natio', 'land', 'telf1'
            ],
            'hub': 'zmc.hub_person',
            'hub_id': 0
        },
        {
            'satellite': 'zmc.sat_location_patient_address',
            'columns': [
                'pstlz', 'ort', 'stras'
            ],
            'hub': 'zmc.hub_location',
            'hub_id': 0
        }
    ]
}

zmc_patient_details_links = {
    'links': [
        {
            'link': 'zmc.person_location_link',
            'values': {
                'person_id': 0,
                'locationzmc._id': 0
            }
        }
    ]
}


