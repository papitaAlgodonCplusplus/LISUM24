# Week 10 of Data Glacier Intership - Retail Forecasting

This repository is for week 10 of Data Glacier Intership "Retail Forecasting", where I perform EDA and Feature Engineering over the dataset and output some recommendations based on the results

**EDA Performed**

EDA walkthrough is inside the Google Colab shared link below, please open the [Table of Contents](https://runestone.academy/ns/books/published/httlads/PythonReview/google_colab.html) to find 'EDA and Feature Engineering' section.

**Quick summary of the EDA performed:**

1. Lag Period Difference (A.K.A Derivative Function)
2. Rolling Average
3. Sales by Date and Product Plot
4. Product count and sales plot
5. Probability Distribution | Sales over Product and Discount over Product
6. Correlation Heatmap | Holidays
7. Change Ratio over Holidays
8. STL Test
9. SelectKBest
10. RandomForestRegressor
11. Gradient Boosting Regression (for % of relevance pre feature insights)
12. PCA (Principal Component Analysis)
13. Recursive Feature Elimination

* *As a result:*

This forecast project EDA has yielded valuable insights and recommendations. The analysis has shown that offering price discounts, especially during sales drops, can significantly impact sales. Prioritizing investments in top-selling products (SKU1, 3, 6) is crucial. SKU1 performs exceptionally well during Christmas and Easter, with over 10% increased sales. In-store promotions have an immediate effect on SKU1-5 sales, while Catalogue promotions consistently increase sales the next day for all products. Store-End promotions notably enhance SKU4 sales the day after implementation. Each SKU's daily sales range (95%) aids budget planning. Google Mobility has no sales impact. Optimal discount ranges to maximize sales and profit balance vary for each SKU (1-6). These findings offer actionable insights for effective sales strategies and resource allocation.

**Code**

> **WARNING:** Please use the Google Colab link for running the code as it is the optimal choice in terms of resources, comfort and error-free guarantee.

- [(Google Colab) Implementation for running and testing](https://colab.research.google.com/drive/13f50xZob9lJAiG0Bys0gRK7LTChR3I5p?usp=sharing)

- [Implementation for analysis and research only](Src/Forecast_Project.ipynb)


**Project Presentation:**

[Presentation](Presentation/Retail_Forecasting_Presentation.pdf)

**Data PDF document:**

[Dataset specifications](Datadoc/Data_Intake_Report.pdf)

## Questions & Feedback

If you have any questions about the proyect, suggestions or want to spot a mistake, please let me know by creating a new issue or writing me at:

<ALEXANDER.QUESADAQUESADA@ucr.ac.cr>

## License

See the LICENSE file for license rights and limitations (MIT).
