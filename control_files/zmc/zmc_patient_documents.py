zmc_patient_documents_hubs = {
    'table': 'zmc.patient_documents',
    'hubs': [
        {
            'hub': 'zmc.hub_object',
            'keys': 'serums_id'
        }
    ]
}

zmc_patient_documents_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_object_patient_documents',
            'columns': [
                'report_title', 'department', 'date', 'content'
            ],
            'hub': 'zmc.hub_object',
            'hub_id': 0
        }
    ]
}

zmc_patient_documents_links = {
    'links': []
}