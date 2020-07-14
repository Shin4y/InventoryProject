Notes for future convenience:

Database setup:
All models inherit from the commonObject model, so all objects in all tables (except for the commonObject table) have a one to one relationship with an object in the commonObject table. 
This application makes the connection from commonObject table to the respective subclass table 
is through the use of slugs. By doing so, most of the code is generalized, with the exception of models, which will need to be hard coded when another model is needed. 