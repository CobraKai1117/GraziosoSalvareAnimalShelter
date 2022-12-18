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




**README questions:**

**How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

 I tried to keep parts of my program modularized. Each section of the program is responsible for a specific task. For the Python file, my code is broken up based on what part of CRUD it is doing. I have functions whose sole tasks is to create and add entries to a database. Other sections are solely responsible for updating or deleting these entries. This makes it easier to maintain, refactor and debug this code in the future. I can run unit tests based on what function I want to test. If I need to make any additions or changes, these will only be applied to specific parts of the program. Because the program is modularized, any errors that occur are easier to locate and debug. While this CRUD module is primarily used for MongoDB databases, this could be applied and configured for other types of database systems. The functionality could also be expanded upon in the future so that it could read documents of multiple file types and add/modify them to a database.   


**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

 As a computer scientist, the most important step for me would be to properly identify the problem. If this process is not done successfully, then either the wrong problem will be solved,the problem is only partially solved or the problem is solved incorrectly. All these issues lead to wasted time and resources. So my first approach would be to figure out what exactly the problem is. 
Unlike previous projects I had done, this one required me to combine multiple components together and integrate them in a seamless way. With past projects, I usually had to build everything from scratch. This project required me to utilize components from Dash, Plotly, MongoDB as well as Python. I also used Jupyter Notebook for testing purposes. Essentially I had to learn 4 different frameworks and combine them together to make this project. Since many programs utilized multiple components from various sources, this is a more "realistic" project compared to previous projects. This experience will be valuable and serve as a stepping stone for when I start my first software development job. 
Before this project, I did have limited experience working with databases, primarily with relational databases using SQL. With this project I utilized MongoDB and a terminal window to add the database to the project. While it was harder to implement, I also had access to additional functionality I wouldn't have if I wasn't using the console. I can apply the knowledge I learned from this project to create a database for a client as well as perform CRUD operations on them.

**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

Computer scientists are in a nutshell problem solvers that develop algorithms to solve these problems. These problems are generally complex and can potentially affect millions of users. When they develop efficient algorithms, these programs make people's lives much easier. However, if the algorithms are inefficient this can lead to many angry and frustrated users. An example of this would be if you use a mobile app to log into your bank. If the app is not properly optimized and too many people try to use the app at once, it might take you a long time to perform operations in the app or the app might even crash. This will lead to people not using your app and taking their business elsewhere. This app allows users to easily find potential canines to train for rescue work such as finding people lost in the wilderness or from natural diasters. It takes large amounts of data and filers the results into an easy to read format that a user can access. As a result, this app can save Grazioso Salvare time and resources.

