import time
import pandas as pd
import numpy as np
import datetime as dt

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
    flag = True
    while True:
        try:

            print('Hello! Let\'s explore some US bikeshare data!')
            # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = input("Would you like to see data for chicago, new york city or washington \n").lower()
            if city == 'chicago' or city == 'new york city' or city ==  'washington':
                # TO DO: get user input for month (all, january, february, ... , june)
                print("Enter January , February, march, April, May or June \n")
                try:

                    month = int(input("Which month? Interger value in month e.g (January = 1) \n"))
                    if month in [1,2,3,4,5,6]:
                        day = input("Which day? Please Enter day like : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n").title()
                        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]:
                            print("city %s , month %s , day %s" % (city, month, day))
                            print('-' * 40)
                            return city, month, day
                        else:
                            print("\n You Enter Wrong day please enter right one \n")

                            print(0/0)

                    else:
                        print("\n You Enter Wrong Month please enter right one \n")
                        print(0/0)
                except:
                    print("\n You Enter Wrong Syntex please enter right one \n")
                    #break

            else:
                print("\n You Enter Wrong city name please enter right one \n")



        except:
            print("\n Please Enter Right Keywords \n")


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    df['mon'] = df['Start Time'].dt.month
    #print(df['mon'])
    df['dow'] = df['Start Time'].dt.weekday_name
    #print(df['day_of_week'])
    df['Hour'] = df['Start Time'].dt.hour
    #print(df['Hour'])
    df = df[df['mon'] == month]
    df = df[df['dow'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['mon'].mode()[0]
    print("Most common month \n",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['dow'].mode()[0]
    print("most common day of week \n",popular_day)


    # TO DO: display the most common start hour

    start_hour = df['Hour'].mode()[0]
    print("most common start hour \n",start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station : %s \n"%(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station : %s \n"%(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df["common_start_end_station"] =  df['Start Station']+" , "+df['End Station']
    common_start_end_combination = df["common_start_end_station"].mode()[0]

    print("frequent combination of start station and end station : %s \n"%common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time : %s \n"%total_travel_time)



    # TO DO: display mean travel time
    total_mean_time = df['Trip Duration'].mean()
    print("Total Mean Time : %s \n"%total_mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    total_usertypes= df["User Type"].value_counts().to_string()
    #total_coustomer = df[df["User Type"]=="Customer"].count()
    print("Total user types \n%s"%total_usertypes)
    #print("Customer : %s \n"%total_coustomer)

    # TO DO: Display counts of gender
    #if city!="washington":
    try:
        gender_counts = df["Gender"].value_counts().to_string()
        print("\n Total Gender \n%s"%gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        most_earlist_dob = df['Birth Year'].min()
        print("Most earlist date of birth : %s \n"%most_earlist_dob)
        most_recent_dob = df['Birth Year'].max()
        print("Most recent date of birth : %s \n"%most_recent_dob)
        most_common_dob = df['Birth Year'].mode()[0]
        print("Most Common date of birth : %s \n"%most_common_dob)
    except:
        print("You enter wrong city in this city gender and birth year is not placed \n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#df = load_data('chicago',1, "Friday")
#print(df.head(3))

def raw_data(df):
    print("\n Displaying Raw data \n")
    u_i = input('\nWhat would you like to see 5 raw data?\nPlease enter yes or no\n').lower()
    if u_i ==('yes'):
        i = 0
        while True:
            print(df.iloc[i:i + 5])
            i += 5
            md = input('Would you like to see more 5 raw data? Please enter yes or no: ').lower()
            if md !=('yes'):
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
