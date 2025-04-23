
import pandas as pd
import numpy as np
from scipy import stats

# Load and prepare data
df_feedback = pd.read_csv("customer_feedback.csv")
df_sales = pd.read_csv("sales_data.csv")
df_feedback['date'] = pd.to_datetime(df_feedback['date'])
df_sales['date'] = pd.to_datetime(df_sales['date'])

def feedback_analysis(df_feedback):
    ios_scores = df_feedback[df_feedback['product'] == 'iOS']['feedback_score'].to_numpy()
    android_scores = df_feedback[df_feedback['product'] == 'Android']['feedback_score'].to_numpy()

    std_ios = np.std(ios_scores, ddof=1)
    std_android = np.std(android_scores, ddof=1)
    equal_var = np.isclose(std_ios, std_android, rtol=0.1)

    t_stat, p_val = stats.ttest_ind(ios_scores, android_scores, equal_var=equal_var)
    return t_stat, p_val

def sales_analysis(df_sales):
    before = df_sales[df_sales['date'] < '2023-03-01']['sales'].to_numpy()
    after = df_sales[df_sales['date'] >= '2023-03-01']['sales'].to_numpy()

    std_before = np.std(before, ddof=1)
    std_after = np.std(after, ddof=1)
    equal_var = np.isclose(std_before, std_after, rtol=0.1)

    t_stat, p_val = stats.ttest_ind(before, after, equal_var=equal_var)
    return t_stat, p_val

def seasonal_analysis(df_sales):
    summer = df_sales[df_sales['date'].dt.month.isin([6, 7, 8])]['sales'].to_numpy()
    winter = df_sales[df_sales['date'].dt.month.isin([12, 1, 2])]['sales'].to_numpy()

    std_summer = np.std(summer, ddof=1)
    std_winter = np.std(winter, ddof=1)
    equal_var = np.isclose(std_summer, std_winter, rtol=0.1)

    t_stat, p_val = stats.ttest_ind(summer, winter, equal_var=equal_var)
    return t_stat, p_val

def consistency_analysis(df_feedback):
    months = [1, 5, 9, 12]
    feedback_groups = [
        df_feedback[df_feedback['date'].dt.month == m]['feedback_score'].to_numpy()
        for m in months
    ]
    f_stat, p_val = stats.f_oneway(*feedback_groups)
    return f_stat, p_val

def corr_analysis(df_feedback, df_sales):
    df_feedback['month'] = df_feedback['date'].dt.to_period('M')
    df_sales['month'] = df_sales['date'].dt.to_period('M')

    avg_feedback = df_feedback.groupby('month')['feedback_score'].mean().reset_index()
    monthly_sales = df_sales.groupby('month')['sales'].sum().reset_index()

    merged = pd.merge(avg_feedback, monthly_sales, on='month')
    high = merged[merged['feedback_score'] >= merged['feedback_score'].median()]['sales'].to_numpy()
    low = merged[merged['feedback_score'] < merged['feedback_score'].median()]['sales'].to_numpy()

    std_high = np.std(high, ddof=1)
    std_low = np.std(low, ddof=1)
    equal_var = np.isclose(std_high, std_low, rtol=0.1)

    t_stat, p_val = stats.ttest_ind(high, low, equal_var=equal_var)
    return t_stat, p_val

# Run all analyses
print("Feedback Analysis:", feedback_analysis(df_feedback))
print("Sales Analysis:", sales_analysis(df_sales))
print("Seasonal Analysis:", seasonal_analysis(df_sales))
print("Consistency Analysis:", consistency_analysis(df_feedback))
print("Correlation Analysis:", corr_analysis(df_feedback, df_sales))
