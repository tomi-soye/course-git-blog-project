import time
import math
import pandas as pd
import numpy as np

#Filenames
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Months to be analysed
MONTH_DATA = { 'january' or 'jan': 1,
                'february' or 'feb': 2,
                'march' or 'mar': 3,
                'april' or 'apr': 4,
                'may' or 'may': 5,
                'june' or 'jun': 6}

#Days to be analysed
WEEK_DATA = { 'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        print("Which country's data would you like to view?")
        city = input('Chicago/CH, New York City/NYC, or Washington/WA? ').lower()
        print()
        if city=='ch':
            city='chicago'
        if city=='ny' or city=='nyc':
            city='new york city'
        if city=='wa' or city=='washington dc':
            city='washington'
        if city not in CITY_DATA:
            print('Kindly enter a valid city')
            continue
        city = CITY_DATA[city]
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        choice = input('Do you want to filter the data by month and/or week? Yes/No ').lower()
        print()
        if choice=='yes' or choice=='y':
            choice=True
        elif choice=='no' or choice=='n':
            choice=False
        else:
            print('Sorry, i am confused. Kindly input "yes" or "no".')
            continue
        break

    while 1:
        if choice:
            filter=input('Do you want to filter by month or day or both ').lower()
            print()
            if filter=='month':
                print("Which month's data are you interested in?")
                month = input('January, February, March, April, May, June- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('Sorry I am confused. Kindly input a month between January and June?')
                    continue
                month = MONTH_DATA[month]
                day='all'
            elif filter=='day':
                print("Which day's data do you want to view? ")
                day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday- ').lower()
                print()
                if day not in WEEK_DATA:
                    print("Sorry I don't understand. Please try again.")
                    continue
                day = WEEK_DATA[day]
                month='all'
            elif filter=='both':
                print("Which month's data do you want to view?")
                month = input('January, February, March, April, May, June- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('Sorry I am confused. Please try again.')
                    continue
                month = MONTH_DATA[month]
                print('And day of the week?')
                day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday- ').lower()
                print()
                if day not in WEEK_DATA:
                    print('Sorry I am confused. Please try again.')
                    continue
                day = WEEK_DATA[day]
            else:
                print('Sorry I am confused. Please try again.')
                continue
            break
        else:
            day='all'
            month='all'
            break

    print('-'*40)
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
    df = pd.read_csv(city)
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #temporary_df = pd.read_csv(city)
    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_freq_month:
            most_freq_month = num.title()
    print('The most common month for travel is {}'.format(most_freq_month))

    # TO DO: display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num]==most_freq_day:
            most_freq_day = num.title()
    print('The most common day of week for travel is {}'.format(most_freq_day))

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_freq_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(most_freq_hour))
    df.drop('hour',axis=1,inplace=True)
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print('Most commonly used start station as per our data was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print()
    print('Most commonly used end station as per our data was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print()
    most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequnt combination of start station and end station trip was {}'.format(most_freq_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    print()
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # TO DO: display mean travel time
    print()
    td_mean = math.ceil(df['Trip Duration'].mean())
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('Number of types of users are {}'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s - {}'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('Sorry, no gender data for this city.')
    else:
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('Data related to birth year of users is not available for this city.')
    else:
        birth = df.groupby('Birth Year', as_index=False).count()
        print('Earliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('Would you like to view some of the data? Yes/No ').lower()
    print()
    if choice=='yes' or choice=='y':
        choice=True
    elif choice=='no' or choice=='n':
        choice=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Additional five? Yes/No ').lower()
            if choice=='yes' or choice=='y':
                continue
            elif choice=='no' or choice=='n':
                break
            else:
                print('You did not enter a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y':
            break

if __name__ == "__main__":
	main()