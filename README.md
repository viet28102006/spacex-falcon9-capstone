# Applied Data Science Capstone – SpaceX Falcon 9 First-Stage Landing Prediction

IBM Data Science Professional Certificate – capstone project.  
Goal: predict whether the Falcon 9 first stage will land successfully, so that the cost of a launch can be estimated.

| # | File | Content |
|---|------|---------|
| 1 | `1_spacex_data_collection_api.ipynb` | Data collection with the SpaceX REST API |
| 2 | `2_spacex_webscraping.ipynb` | Web scraping of Falcon 9 launch records from Wikipedia |
| 3 | `3_spacex_data_wrangling.ipynb` | Data wrangling and creation of the `Class` label |
| 4 | `4_spacex_eda_sql.ipynb` | Exploratory data analysis with SQL |
| 5 | `5_spacex_eda_dataviz.ipynb` | Exploratory data analysis with visualization and feature engineering |
| 6 | `6_spacex_launch_site_location_folium.ipynb` | Interactive map analytics with Folium |
| 7 | `7_spacex_dash_app.py` | Interactive dashboard with Plotly Dash |
| 8 | `8_spacex_machine_learning_prediction.ipynb` | Predictive analysis (Logistic Regression, SVM, Decision Tree, KNN) |

`data/` contains the IBM Skills Network datasets used by the notebooks; `maps/` contains the saved Folium maps.

**Main results:** 90 Falcon 9 launches, overall landing success 66.7%; success improved strongly after 2013; KSC LC-39A has the highest success ratio; all four models reach 83.3% test accuracy, with SVM and Decision Tree best on validation (84.8%).

Run the dashboard: `pip install pandas dash plotly` then `python 7_spacex_dash_app.py`.
