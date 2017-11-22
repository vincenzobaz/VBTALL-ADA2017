# Characterisation of post Cold War conflicts

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

