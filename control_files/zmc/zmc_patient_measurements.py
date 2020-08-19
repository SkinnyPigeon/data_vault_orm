zmc_patient_measurements_hubs = {
    'table': 'zmc.patient_measurements',
    'hubs': [
        {
            'hub': 'zmc.hub_person',
            'keys': 'serums_id'
        }
    ]
}

zmc_patient_measurements_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_person_patient_measurements',
            'columns': [
                'height', 'weight', 'date'
            ],
            'hub': 'zmc.hub_person',
            'hub_id': 0
        }
    ]
}

zmc_patient_measurements_links = {
    'links': []
}