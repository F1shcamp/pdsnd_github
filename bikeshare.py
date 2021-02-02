import time
import pandas as pd
import numpy as np


    # set up library of city data options
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    # Set month and day list for options
MONTH_OPTIONS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_OPTIONS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input('Please enter one of the following cities - Chicago, New York City, Washington:  \n')
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print('PLEASE TRY AGAIN \n')
            
            

    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_OPTIONS:
        month_name = input('\nPlease enter a month option - all, january, february, march .... june \n')
        if month_name.lower() in MONTH_OPTIONS:
            month = month_name.lower()
        else:
            print('PLEASE TRY AGAIN \n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_OPTIONS:
        day_name = input ('\nPlease enter a day option - all, monday,tuesday  .... sunday \n')
        if day_name.lower() in DAY_OPTIONS:
            day = day_name.lower()
        else:
            print('PLEASE TRY AGAIN \n')

    check = ''
    while check.lower() != 'yes':
        print('-'*40)
        print('\nYou have filterd your analysis using the folloing criteria: \nCITY: {}'.format(city_name.title()))
        print('MONTH: {}'.format(month.title()) + ('\nDAY: {}'.format(day.title())))
        check = input('\nIs this correct? Yes or No: ')
        if check.lower() == 'yes':
            return city, month, day
        else:
            print('-'*40 + '\nRESTARTING')
            city, month, day = get_filters()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load csv data into dataframe
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != 'all':
        month = MONTH_OPTIONS.index(month)
        df = df.loc[df['month'] == month]

    # Filter by day
    if day != 'all':
        df= df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    month_count = (df['month'].values == most_common_month).sum()
    print('\nThe most common month is: ' + MONTH_OPTIONS[most_common_month].title() + '  Count({})'.format(month_count) )

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    day_count = (df['day_of_week'].values == most_common_day_of_week).sum()
    print('\nThe most common day of week is: ' + most_common_day_of_week + '  Count({})'.format(day_count))

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    hour_count = (df['hour'].values == most_common_start_hour).sum()
    print('\nThe most common start hour is: ' + str(most_common_start_hour) + '  Count({})'.format(hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(5)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    start_count = (df['Start Station'].values == common_start_station).sum()
    print('\nThe most commonly used start station is: ' + common_start_station + '  Count({})'.format(start_count))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    end_count = (df['End Station'].values == common_end_station).sum()
    print('\nThe most commonly used end station is: ' + common_end_station + '  Count({})'.format(end_count))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station'] + '||' + df['End Station']).mode()[0]
    combo_count = (df['Start Station'] + '||' + df['End Station'].values == most_frequent_combination).sum()
    print('\nThe most frequenst combination of start and end station trip is: ' + most_frequent_combination + '  Count({})'.format(combo_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(5)

    # Used to convers seconed to a day:hour:minute:second format(sample code from https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
def seconds_to_dms(total_travel_time):
    time = float(total_travel_time)
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    conversion = ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
    return conversion


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is: ' + str(seconds_to_dms(total_travel_time)))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean value for travel time is: ' + str(seconds_to_dms(mean_travel_time)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(5)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe count of user types is:\n' + str(user_types) + '\n')
    time.sleep(5)
    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print('The count of user gender is:\n' + str(gender))
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('\nThe earliest born rider was born in: {}\n'.format(int(earliest_birth)))
        print('The most recent born rider was born in: {}\n'.format(int(most_recent_birth)))
        print('The most common birth year of riders  is: {}\n'.format(int(most_common_birth)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(5)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
