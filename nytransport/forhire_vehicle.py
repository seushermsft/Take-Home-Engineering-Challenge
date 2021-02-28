import pandas as pd


def run( start_zone, end_zone, ):
    """

    :param start_zone:
    :param end_zone:
    :param start_datetime: start time you search for
    :param end_datetime: end time your search for
    :return: fare
    """

    forhire_vehicle_data = pd.read_csv('tripdata/fhv_tripdata_2018-01.csv')
    taxi_zone_data = pd.read_csv('tripdata/taxi+_zone_lookup.csv')

    if forhire_vehicle_data is None or taxi_zone_data is None:
        print("data loading failure")

    taxi_zone_data.set_index('Zone', inplace=True)
    start_zone_location_id = taxi_zone_data.loc[[start_zone], 'LocationID'][0]
    end_zone_location_id = taxi_zone_data.loc[[end_zone], 'LocationID'][0]

    test1 = forhire_vehicle_data.loc[(forhire_vehicle_data['PUlocationID'] == start_zone_location_id) &
                                 (forhire_vehicle_data['DOlocationID'] == end_zone_location_id),]
    print(test1)

    # yellow_taxi_data.hist(bins=50, figsize=(20,25), layout=(5,3))
    # plt.show()

