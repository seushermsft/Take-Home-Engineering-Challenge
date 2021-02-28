import pandas as pd


def run( start_zone, end_zone, trip_distance=False, total_amount=False):
    """

    :param trip_distance:
    :param total_amount:
    :param start_zone:
    :param end_zone:
    :param start_datetime: start time you search for
    :param end_datetime: end time your search for
    :return: fare
    """

    yellow_taxi_data = pd.read_csv('tripdata/yellow_tripdata_2018-01.csv')
    taxi_zone_data = pd.read_csv('tripdata/taxi+_zone_lookup.csv')

    if yellow_taxi_data is None or taxi_zone_data is None:
        print("data loading failure")

    taxi_zone_data.set_index('Zone', inplace=True)
    start_zone_location_id = taxi_zone_data.loc[[start_zone], 'LocationID'][0]
    end_zone_location_id = taxi_zone_data.loc[[end_zone], 'LocationID'][0]

    if trip_distance == "True":
        trip_data = yellow_taxi_data.loc[(yellow_taxi_data['PULocationID'] == start_zone_location_id) &
                                     (yellow_taxi_data['DOLocationID'] == end_zone_location_id),
                                      ['tpep_pickup_datetime','tpep_dropoff_datetime','trip_distance','fare_amount',
                                       'total_amount']].sort_values(by='trip_distance', ascending=True)
    elif total_amount == "True":
        trip_data = yellow_taxi_data.loc[(yellow_taxi_data['PULocationID'] == start_zone_location_id) &
                                     (yellow_taxi_data['DOLocationID'] == end_zone_location_id),
                                     ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance', 'fare_amount',
                                      'total_amount']].sort_values(by='total_amount', ascending=True)
    print(trip_data)

    # yellow_taxi_data.hist(bins=50, figsize=(20,25), layout=(5,3))
    # plt.show()
