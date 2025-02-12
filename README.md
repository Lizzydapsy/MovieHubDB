The purpose of our project was to create a data-driven web application using PostgreSQL and Redis for efficient data storage and caching. By integrating these two technologies with Flask as the backend framework, we aimed to build an application that could fetch and display movie data from PostgreSQL while using Redis to cache frequently accessed queries, improving performance. The project also allowed us to enhance our frontend development skills, where we displayed the movie data in an interactive table and visualised genre distribution. Through this project, we learned how to effectively use both relational databases (PostgreSQL) and in-memory caching systems (Redis), improving our understanding of backend development, database management, and the importance of optimising data retrieval.

Phase 1: Project Planning and Setup

Naz and I started by defining the project's structure, deciding on PostgreSQL, Redis, and Flask. We sketched the design, focusing on how data would flow and the type of visualisation (genre distribution of movies) we wanted. We also designed the database schema and discussed using Redis for caching frequently accessed data to improve performance. After setting up the project environment, we created a GitHub repository and installed the necessary libraries.

![Hierarchical diagram illustrating the file structure of the "movie-data-project". The root directory "movie-data-project" contains a "backend" folder with "app.py", "database.py", "config.py", and "requirements.txt"; a "frontend" folder with "index.html" and "script.js"; a "data" folder with "movie.csv"; and loose files ".gitignore", "README.md", and "run.sh". Arrows indicate the parent-child relationships between directories and files.](image-2.png)

![Flowchart depicting the architecture of a web application. Starting at the top, a "Client" box labeled with "+HTTP requests" and "+UI/UX interactions" connects to a "Frontend" box containing "+HTML", "+CSS", "+Displays data", and "+JavaScript (fetch API)".  An arrow labeled "Interacts with UI  Renders data on UI" goes from Client to Frontend.  Another arrow labeled "Sends HTTP requests (AJAX/fetch)" goes from Frontend to a "Backend" box with "+Flask app", "+API routes", and "+Handles business logic".  An arrow labeled "Returns data" goes from Backend back to Frontend.  The Backend box has an arrow labeled "Calls API route for data" pointing to an "API" box with "+GET /data", "+Fetches data from either Redis or PostgreSQL", "+Stores fetched data in Redis", and "+Switches between Redis/PostgreSQL based on config".  Arrows connect the API box to both a "Redis" box with "+Cache data" and "+set() and get()" (labeled "Fetches data from Redis cache (if enabled)") and a "PostgreSQL" box with "+Store data" and "+SQL queries" (labeled "Fetches data from PostgreSQL if enabled").  Finally, an arrow labeled "Cache miss leads to DB query (if Redis is used first)" goes from Redis to PostgreSQL.](image.png)

Once the design was in place, we turned to setting up the project environment. I helped Naz create a GitHub repository and pushed the initial commits. We also set up the project folders and installed PostgreSQL, Redis, and the necessary Python libraries, ensuring everything was ready for the next phase of development.

Phase 2: Backend Development - Database and API

With the setup complete, we moved to backend development. I created the PostgreSQL database and defined the schema, while Naz configured Redis and connected it to Flask. We then wrote API routes to fetch movie data, integrating Redis caching to optimise performance. We tested the backend to ensure it could switch between Redis and PostgreSQL based on data availability.

Phase 3: Loading Data into PostgreSQL and Redis

We then focused on populating the databases. I wrote a script to load movie data into PostgreSQL, while Naz set up caching for popular queries in Redis. We validated the data in both databases to ensure accuracy.

Phase 4: Frontend Development

For the frontend, I designed the HTML structure and CSS for the movie data table, while Naz wrote the JavaScript to integrate the frontend with the backend. We also added a visualisation feature to display genre distribution. After testing the frontend, we ensured seamless interaction with the backend.

Phase 5: Testing, Scaling, and Optimisation

Naz wrote unit tests for the backend, and I focused on testing the frontend. We ran performance tests to assess how Redis improved response times, optimised SQL queries, added pagination, and implemented lazy loading for better frontend performance.

Phase 6: Documentation and Group Presentation

In the final phase, we worked on the documentation, ensuring it covered setup, backend, and frontend details. We also prepared for the presentation, with me covering the backend and Redis caching, and Naz explaining the frontend and visualisation components.

I feel proud of what Naz and I accomplished. We successfully integrated PostgreSQL, Redis, and Flask to build a fully functional application. It was rewarding to see how Redis helped optimise performance and how we could display the movie data efficiently. The project gave us the opportunity to learn how to work with both Redis and PostgreSQL, understand their roles in backend development, and integrate both technologies into a data-driven application. We also improved our skills in frontend development (using either Jupyter Notebook or HTML), version control, and testing. It was an excellent learning experience, and we’re thrilled with how well we worked together as a team.