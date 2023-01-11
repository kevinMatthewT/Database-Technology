CREATE TABLE Plane(
    Plane_ID INTEGER PRIMARY KEY NOT NULL,
    Plane_Type TEXT NOT NULL
);


CREATE TABLE passenger(
    Passenger_ID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Sex TEXT NOT NULL,
    Date_of_birth TEXT NOT NULL,
    Address TEXT NOT NULL,
    Phone_Number INTEGER NOT NULL,
    Email INTEGER NOT NULL 
);

CREATE TABLE flight(
    Flight_Number INTEGER PRIMARY KEY NOT NULL,
    Plane_ID INTEGER,
    Departure_time TEXT NOT NULL,
    Departure_city TEXT NOT NULL,
    Arrival_time TEXT NOT NULL,
    Destination_time TEXT NOT NULL,
    FOREIGN KEY (Plane_ID) REFERENCES Plane(Plane_ID)
);
