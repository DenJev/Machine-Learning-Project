import pandas as pd
from Python.Code.Class_Data_Exploration import DataExploration


def main():
    model_df = DataExploration(pd.read_csv("Data_In/VehicleData_csv.csv"))  # loads in the data

    print(model_df._data_set.head())  # prints the first 5 columns of the data-set
    print(model_df.dim_data())  # prints the dimension of the data set
    model_df.missing_data_ratio_print()  # prints the percentage of missing values in the data set (NONE FOUND!)

    model_df._data_set.to_csv("Data_Out/data_set_out.csv")  # saves the pandas data frame to a CSV file

    model_df.box_plot("ConditionScore", "FinancialYear")  # box plot of the Condition score for each Year
    model_df.box_plot("ConditionScore", "Manufacturer")  # box plot of the Condition score for each Manufacturer

    # function that prints the number of inspections each financial year.
    model_df.column_value_count("FinancialYear")

    #  function that plots the percentage of what year each inspection occurs.
    model_df.bar_graph_percentage("FinancialYear")


if __name__ == "__main__":
    main()
