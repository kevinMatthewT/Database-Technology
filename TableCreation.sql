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
    Departure_country TEXT NOT NULL,
    Arrival_time TEXT NOT NULL,
    Arrival_city TEXT NOT NULL,
    Arrival_country TEXT NOT NULL,
    FOREIGN KEY (Plane_ID) REFERENCES Plane(Plane_ID)
);

CREATE TABLE booking(
    Booking_ID INTEGER PRIMARY KEY NOT NULL,
    Booking_Date TEXT NOT NULL,
    Flight_Number INTEGER NOT NULL,
    Passenger_ID INTEGER NOT NULL,
    FOREIGN KEY (Flight_Number) REFERENCES flights(Flight_Number),
    FOREIGN KEY (Passenger_ID) REFERENCES passenger(Passenger_ID)
);

CREATE TABLE payment(
    Booking_ID INTEGER,
    Payment_Type TEXT NOT NULL,
    Payment_Amount INTEGER,
    Payment_Status TEXT NOT NULL,
    FOREIGN KEY (Booking_ID) REFERENCES booking(Booking_ID)
);
