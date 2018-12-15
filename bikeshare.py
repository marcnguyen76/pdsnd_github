# Marc Nguyen

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n>>>\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        city = city.lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('Error: "{}" is an invalid city. Please enter a city from the list.'.format(city))
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to filter: all, january, february, ... , june\n> ')
        month = month.lower()
        if any([month == 'all', month == 'january', month == 'february', month == 'march', month == 'april',
                month == 'may', month == 'june']):
            break
        else:
            print('Input Error: {} is an invalid filter. Please select a value from the list.'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to filter: all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday\n> ')
        day = day.lower()
        if any([day == 'all', day == 'monday', day == 'tuesday', day == 'wednesday', day == 'thursday',
                day == 'friday', day == 'saturday', day == 'sunday']):
            break
        else:
            print('Input Error: {} is an invalid filter. Please select a value from the list.'.format(day))

    print('\n' + '-'*60)
    return city, month, day


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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month

    # extract month from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month
    # find the most common month (from 0 to 12)
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Frequent Start Day:', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n' + '-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular Start Station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_station_comb = df['Start Station'] + ' >>> ' + df['End Station']
    popular_station_comb = popular_station_comb.mode()[0]
    print('Most popular Station Combination: ', popular_station_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n' + '-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel time: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n' + '-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Counts:\n', user_type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Counts: \n', gender_count)
    except:
        print('\nGender Counts: No Data')

    # TO DO: Display earliest, most recent, and most common year of birth
	# some data does not contain birth year
    try:
        birth_year_min = df['Birth Year'].min()
        print('\nBirth Year Minimum: ', birth_year_min)
        birth_year_max = df['Birth Year'].max()
        print('Birth Year Maximum: ', birth_year_max)
        birth_year_mode = df['Birth Year'].mode()[0]
        print('Birth Year Mode: ', birth_year_mode)
    except:
        print('\nBirth Year: No Data')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n' + '-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # Display raw data with user input
        more_data = True
        line_count = 5
		# Display raw data 5 lines at a time until user exit by typing 'No' or continue to press ENTER to
		# continue showing data
        while more_data:
            see_data = input("Would you like to see the first 5 lines of raw data ('Yes' or 'No')\n>>>")
            see_data = see_data.lower()

            if see_data == 'yes':
                print(df.head())
                while True:
                    see_data = input("Would you like to see 5 more lines of raw data (Press ENTER for Yes or enter 'No')\n>>>")
                    see_data = see_data.lower()
                    if see_data == '' or see_data == 'yes':
                        print(df.iloc[line_count:line_count+5, :])
                        line_count += 5
                        if line_count > df.shape[0]:
                            more_data = False
                            print('End of Data')
                            break
                    elif see_data == 'no':
                        more_data = False
                        break
                    else:
                        print("'{}' is an invalid entry.  Please enter ('Yes' or 'No')".format(see_data))
                        
            elif see_data == 'no':
                break
            else:
                print("'{}' is an invalid entry.  Please enter ('Yes' or 'No')".format(see_data))       
         
        print('\n' + '-'*60)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
