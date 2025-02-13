# Movie Database Management and Visualization System 

The purpose of our project was to create a data-driven visualization dashboard using PostgreSQL and Redis for efficient data storage and caching. By integrating these two technologies with Flask as the backend framework, we aimed to build an application that could fetch and display movie data from PostgreSQL or Redis, improving performance. The project also allowed us to enhance our frontend development skills, where we displayed the movie data in an interactive table and visualised genre distribution. Through this project, we learned how to effectively use both relational databases (PostgreSQL) and non-relational databse (Redis), improving our understanding of backend development and database management.

### Phase 1: Project Planning and Setup

Naz and I started by defining the project's structure, deciding on PostgreSQL, Redis, and Flask. We sketched the design, focusing on how data would flow and the type of visualisation (genre distribution of movies) we wanted. We also designed the database schema and discussed using Redis for caching frequently accessed data to improve performance. After setting up the project environment, we created a GitHub repository.

**Project Structure**

```
moviehubdb/
│
├── backend/
│   ├── app.py                # Main application file
│   ├── config.ini            # Configuration file (INI format)
│   ├── config.py             # Configuration settings (Python)
│   ├── database.py           # Database connection and operations
│   ├── models.py             # Database models or other backend models
│   ├── populate_db.py        # Data population script
│   ├── redis_cache.py        # Redis caching utility
│   └── requirements.txt      # List of dependencies for backend
│
├── data/
│   └── movies.csv            # CSV file containing movie data
│
├── frontend/
│   └── visualization.ipynb   # Jupyter notebook for data visualization
│
├── tests/
│   ├── test_api.py           # API tests
│   └── test_database.py      # Database tests
│
├── .gitignore                # Git ignore rules
├── README.md                 # Project description and documentation

```



**System Design**

![A diagram illustrating a three-tier system architecture consisting of a Frontend, ClientAPI, and Backend, along with PostgreSQL and Redis databases. The diagram shows the flow of data and interactions between these components. The Frontend box (teal) lists methods: collect_user_input() returning a dictionary, send_request_to_client_api() taking a dictionary and returning void, display_data() taking a dictionary and returning void, and render_visualizations() taking a dictionary and returning void. It has arrows indicating "Sends User Request" and "Delivers Response" to and from the ClientAPI. The ClientAPI box (purple) lists methods: send_request() taking an endpoint string and data dictionary and returning a dictionary, and handle_response() taking a response dictionary and returning void. It has arrows labeled "Sends Request" and "Sends Response" to and from the Backend, and "Handles Request" pointing to the Backend. The Backend box (green) lists methods: process_request() taking a request dictionary and returning a dictionary, fetch_from_postgres() and fetch_from_redis() each taking a string and returning a dictionary, store_in_redis() taking a string key and a value dictionary and returning void, and switch_cache_or_db() taking a key string and query string and returning a dictionary. It has arrows labeled "Queries/Postgres" and "Interacts" to PostgreSQL, and "Caches/Retrieves Data" and "Interacts" to Redis. The PostgreSQL box (salmon) lists methods: query_data() taking a query string and returning a dictionary. The Redis box (pink) lists methods: get_cache() taking a key string and returning a dictionary, set_cache() taking a key string and value dictionary and returning void, and delete_cache() taking a key string and returning void. A separate Visualization box (light purple) is connected to the Frontend by a line labeled "Displays Data." The diagram components are contained within rounded rectangles and connected with arrows indicating the direction of data flow and interaction.](image.png)

Once the design was in place, we turned to setting up the project environment and the necessary Python libraries. I helped set up the project folders, ensuring everything was ready for the next phase of development.

### Phase 2: Backend Development - Database and API

With the setup complete, we moved to backend development. I created the PostgreSQL database and defined the schema, while Naz configured Redis and connected it to Flask. We then wrote API routes to fetch movie data, integrating Redis caching to optimise performance. We tested the backend to ensure it could switch between Redis and PostgreSQL.

### Phase 3: Loading Data into PostgreSQL and Redis

We then focused on populating the databases. I wrote a script to load movie data into PostgreSQL, while Naz set up that of Redis. We validated the data in both databases to ensure accuracy.

### Phase 4: Frontend Development

Within our Jupyter Notebook frontend development, I focused on the user interface and presentation, structuring notebook cells for a clear layout of the movie data table and interactive elements.  This included `ipywidgets` for filters, Pandas styling for the table, Markdown for explanations.  Naz handled the dynamic interaction with the backend API, writing Python code (using `requests`) to send requests, process JSON responses, and update the displayed data, including handling API endpoints, pagination, error handling.  We collaborated on the data visualization feature; I explored plotting libraries, while Naz implemented the chosen visualization using appropriate library and connected it to backend data".  Finally, we thoroughly tested the frontend within the notebook to ensure seamless backend communication.


### Phase 5: Testing, Scaling, and Optimisation

Naz wrote unit tests for the backend, and I focused on testing the frontend. We ran performance tests to assess how Redis improved response times, optimised SQL queries, and implemented lazy loading for better frontend performance.

### Phase 6: Documentation and Group Presentation

In the final phase, we worked on the documentation, ensuring it covered setup, backend, and frontend details. We also prepared for the presentation, with me covering the backend and Redis caching, and Naz explaining the frontend and visualisation components.

I feel proud of what Naz and I accomplished. We successfully integrated PostgreSQL, Redis, and Flask to build a functional dashboard. It was rewarding to see how we could display the movie data efficiently regardless of the type of database. The project gave us the opportunity to learn how to work with both Redis and PostgreSQL, understand their roles in backend development, and integrate both technologies into a data-driven application. We also improved our skills in frontend development using either Jupyter, version control, and testing. It was an excellent learning experience, and we’re thrilled with how well we worked together as a team.