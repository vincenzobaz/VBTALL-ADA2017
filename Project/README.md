# Characterisation of post Cold War conflicts
[Data Story](https://vincenzobaz.github.io/VBTALL-ADA2017/)
# Abstract
Through our studies, we’ve analysed major historical conflicts, mainly until the end of the cold war. Since the end of the cold war, we’ve seen a complexification of the conflicts that have occurred: from small, local conflicts, to conflicts spanning entire regions such as what happened with the Arab Spring. Understanding the depth and context of these conflicts is out of the reach of the non-specialist. In this work, we will attempt to use data analysis tool and techniques to extract meaningful and comprehensible informations about those conflicts. We will use the UCDP dataset that tracks conflicts since the 1989 and related datasets that can fill the gaps in specific aspects of the conflicts, such as the human movements, the economy or even the perception by external medias. In the end, we will attempt to generate networks that will add depth and new dimensions to the simple chronology of conflicts given in the UCDP dataset. Finally, we will present our result through interactive visualisations shedding light on the stories hidden in the data.

# Research questions

 - How to characterize the post cold war conflicts?
 - How conflicts influence each others geographically, temporally, in magnitude, etc.?
 - What is the influence of conflicts with regards to neighbouring countries, population movements, perception by the media, economical flows?
 - How can other datasets that are not directly contained in the chosen dataset can be used to augment the depth of our analysis?
 - How to organize these information in graphs, time-series and maps in such a way that meaningful information can be extracted, analysed and showed?

# Dataset
We will focus our research on the UCDP dataset. Depending on the richness of the UCDP dataset, we might consider additional data sources such as UNHCR (United Nations Human High Commissioner for Refugees), medias (200y project or other), dataset on economics (Atlas on Economic Complexity) or others.

The dataset is easily downloadable from the project website. We will start by analyzing and preprocessing the data using pandas. We will then try to build networks using networkx.
The csv data already contains conflits with dates, type of violence, geographical coordinates, names of the entities involved, number of deaths and pointers towards news agencies articles reporting the conflict. We expect the data not to need important cleaning.

Data size is manageable as csv files have very reasonable size and can be stored locally.

# A list of internal milestones up until project milestone 2

 - Get acquainted with the dataset.
 - Organize the data in structures compatible with our analysis.
 - Create functions that can extract mathematical characteristics of conflicts by country, geographical locality, time.

# Questions for TAa

 - Is it possible to include data from additional datasets later on?
 - We think we will use the networkx library for our graphs? Do you think it will work with the UCDP dataset? Do you recommend other libraries?


# Milestone 2 roundup
**The code for the milestone 2 is in the `notebook-merge.ipynb` notebook**.

We imported and got acquainted with the main dataset. As planned, we imported
some complementary data from the United Nations Human High Commissioner for Refugees.

Both dataset required some cleaning and wrangling. The data was imported into
pandas dataframes:

 - A simple dataframes generated from the UCDP csv data file to which we added
the computed duration of each event.
 - A dataframe where we grouped events by conflict and aggregated some of the related
statistics.
 - A dataframe containing the cleaned data about refugees.
 - A dataframe linking the displacement of refugees to the events described in
the UCDP dataset.

We then proceeded to build some networkx graphs which, together with the dataframes,
will be the main data structure that we will use for our analysis:

 - a network linking events to conflicts: the conflicts coordinates are computed
as the centroid of the singular events (mean of latitude and longitude). The edges
linking events to conflicts will contain information about the distance between the
conflict and the event.
 - A network whose nodes ar the distinct `side_a` and `side_b` of the events
connected by edges containing information about the number of deaths in the event.

We also tried to start to visualize the data. `geopandas` allowed to easily draw
static maps to quickly get acquainted with the data. However we wanted to build
interactive visualizations using pandas. The number of markers to plot being
relatively high, the notebook-folium interaction could not complete the operation.
Therefore we resulted to generating the html/javascript from the notebook and to
open it in a browser.

## Milestone 3 roundup
The data story is available [here](https://vincenzobaz.github.io/VBTALL-ADA2017/).

### Contributions
 - Thomas: Network of distances, writing up the report, exploratory statistics
 - Laurier: GDP, HDI and UNHCR datatasets extraction, wrangling and merge. Interactive maps and interactive graph.
 - Vincenzo: Sides analysis, plots and visualizations, web page

