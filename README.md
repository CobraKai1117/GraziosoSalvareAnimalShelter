About the Project
This program enables users to search for animals in Texas to be trained for rescue services. Users utilize a dashboard to interact with a database containing this data. Depending on the needs of the user, this data can be filtered into several different rescue operations. The results are then displayed to a user through a data table, as well as a graph containing the animals’ location. 

Motivation: 
This program helps law enforcement and other government entities easily identify and locate potential dogs to be trained for search and rescue (SAR) services. This saves trainers time and resources so they can focus on their primary task, training the animal.

Functionality: 
Here is a simple demonstration of what this program can do. First the user is shown the entire collection of animals. To improve readability, the results in the data table are limited to 10 per page. Below the data table lies the geolocation plot and the age distribution. The former contains the locations of each animal in the dataset, the latter contains a range of age of the animals.

![Pet Initial State](https://user-images.githubusercontent.com/43760180/208280333-58260fe6-bf91-499d-842d-d33792d41d26.png)



![Pet Dashboard initial state](https://user-images.githubusercontent.com/43760180/208280312-38dfa944-1ff8-4f83-9510-6efb76bb5ad4.png)


![Pet Dashboard Initial GPS](https://user-images.githubusercontent.com/43760180/208280315-b5d95b93-50cb-43f0-9835-9b50a1db9ffe.png)

The user next selects the Disaster or Individual Tracking selection from the drop down widget. This filters the data results so that only those animals who meet the desired criteria are displayed. This filter carries over to the data table, the geolocation map and the age distribution.

![Pet Dashboard Diaster and Individual Tracking](https://user-images.githubusercontent.com/43760180/208280350-920ff710-8dd4-464d-8ca3-cb454bb2397a.png)

![Pet Dashboard Image 2](https://user-images.githubusercontent.com/43760180/208280352-a0033575-d261-4675-81a1-f7cefcf36556.png)


The user then selects the Water Rescue option from the drop down. As with the previous screenshot, the results are filtered to reflect the dropdown changes.

![Water Rescue](https://user-images.githubusercontent.com/43760180/208280411-83e45e98-766a-4500-842d-d3d5318f2bf7.png)

The user selects the final option and again receives filtered results based on the search criteria. If the user wants to see the data without filters, they just need to select the Reset option as shown in the first image.

Tools used:
There were several tools used to develop this program:
●	Python
●	MongoDB
●	Dash
●	Plotly

Python was utilized through the Python CRUD (Create Read Update Delete) module. This module allows users to perform actions against the database. In this case, the module allows users to perform search queries against the database containing shelter animals and retrieve the results.
MongoDB allows Python to interact with it through the user of a Python Driver called PyMongo. PyMongo provides support for establishing database connections. It can also easily convert data into different formats enabling many different sources of data to be accessed by the user.
Dash is a framework that simplifies developing apps for the web.  It is ideal for customized user interfaces and programs that rely heavily on data. Unlike traditional web applications, Dash is written entirely in Python and doesn’t require users to know other web languages such as HTML, CSS, or JavaScript. It also separates programs into two parts: layout and functionality. This separation ensures aspects such as testing, and debugging are easier to implement.
Plotly is an open-source Python plotting library. It works in conjunction with Dash to develop data charts based on various data and parameters. These charts can be stand alone or combined with other components to produce more complex applications.

