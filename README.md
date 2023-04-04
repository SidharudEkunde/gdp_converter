1.Title:"India's GDP Converter".
2.Description: This project retrieves India's GDP data from a data source and displays in the form of graph. It also allows users to convert the GDP data from USD to INR using an API. 
3.Requirements: attached above requirements.txt file to run application
4.Follow below steps to run application:
  1. you need to have Python installed on your system.
  2. install all requirments to run Django application
     follow below command to install all requirments: pip install -r requirments.txt.
  3. install MySQL Server
     Create gdp database
  4. python manage.py makemigrations && python manage.py maigrate
  5. Test the project:
      To test that your project is set up correctly, you can run the development server using the following command:
          python manage.py runserver. 


5. Usgae:
  localhost:8000/api/udp this Url is resposiable/helpful to iterate data from source data file and insert data into DB(MySQL)
  localhost:8000/api/chart this Url is resposiable/helpful to fetch data from database and plot data in the form of graph, to convert GDP data from USD to INR.
