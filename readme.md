# Backend Test Readme
> By Chung Mang Fung Ernest

## Before
clone the git repo 

## Docker Setup
1. Prepare and start a docker environment

2. Run the following code
    ```sh
    docker pull mongo
    docker run -d -p 27017:27017 --name mongodb mongo
    ```
3. Run import.py to import the data
You can check the import process by inspecting the mongodb
    ```sh
    docker exec -it mongodb bash
    mongo
    show dbs
    use newdb
    db.movies.find()
    ```
    You then can find the data is imported in database newdb, collection movies.

## API testing
1. Run the following code
    ```sh
    myproject\Scripts\activate
    python app.py
    ```
    The server will be turned on.

2. Check the API (Recommand using Postman, but you can directly click the link)
    a. check http://localhost:5000/movies
    b. check http://localhost:5000/movieDetail?uuid={uuid}
    > Remarks: Before testing (b), make sure you have copied the uuid of one of the record before testing.
    Example: http://localhost:5000/movieDetail?uuid=8a90c1ed-4684-426c-93a3-0497441e4bdd
    (The uuid will be different!)

## Reference for this backend task
- https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
- https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/
- https://stackoverflow.com/questions/56128397/how-to-connect-to-mongo-inside-a-docker-container-using-pymongo/56128792
- https://github.com/PrettyPrinted/mongodb_backed_restful/blob/master/mongo.py
- https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
