# Surfs_up Analysis
Module 9
## Overview of the analysis:
The purpose of this analysis was to help our investors W. Avy get an idea of the temperature trends for the month of June and December before deciding if our surf and ice cream shop business is sustainable year-round.

## Results:
At first, we made an sqlalchemy query to get the observed temperature `tobs` for the month of June and December using the `func.strftime` function. We then converted the results into a list using the `np.ravel` function, then converted our list to a DataFrame, and used the `describe` function to obtain the statistics summary.

```
june_tobs = session.query(Measurement.tobs).\
    filter(func.strftime("%m", Measurement.date) == "06").all()
june_tobs

june_temp = list(np.ravel(june_tobs))
june_temp

df_june = pd.DataFrame(june_temp, columns=['June Temp'])
df_june

df_june.describe()
```
 
We can see from the `DataFrame` and the `histogram` that the average (mean) and median (50%) temperature is ~75 F for June while it is ~71 F for December. While it is a little bit cooler in December, temperatures are below 69 F only 25% of the time. These lower 60s are still good for surfing with wetsuits but surfers may not want a refreshing ice cream below 65 F. Luckily for us, these lows represent only ~8% of the temperature measurement counts, which would be 2 to 3 days a month.


![df_stats](Resources/df_stats.png)


![June_Temp_hist](Resources/June_Temp_hist.png)


![Dec_Temp_hist](Resources/Dec_Temp_hist.png)


## Summary:
Overall, this project ...
