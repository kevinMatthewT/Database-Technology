insert into plane(Plane_ID,Plane_Type)
values
  (1,"Tiger Air"),
  (2,"Sky High Airlines");

insert into flight(Flight_Number,Plane_ID,Departure_time,Departure_city,Departure_country,Arrival_time,Arrival_city,Arrival_country)
values
    (1,1,"2023-01-06 15:00:00","Seoul","South Korea","2023-01-06 17:10:00","Osaka","Japan"),
    (2,2,"2023-01-06 23:00:00","Jakarta","Indonesia","2023-01-07 02:00:00","Tokyo","Japan");
   
   
insert into passenger(Passenger_ID,Name,Age,Sex,Date_of_birth,Address,Phone_Number,Email)
values
    (1,"Dainton Parker",30,"M","1993-01-02","Jl. Danau Sunter Utara No.45, Sunter Agung, Kec. T...",656083944,"d.parker@randatmail.com"),
    (2,"Adrianna Walker",23,"F","2000-01-02","208-208 上岩田 小国町 Nagaoka, Niigata 949-5332, Japan",930707387,"a.walker@randatmail.com"),
    (3,"Preston Armstrong",29,"M","1994-01-02","95XJ+43M, Yingbin Blvd, Huadu District, Guangzhou,...",371009041,"p.armstrong@randatmail.com"),
    (4,"Richard Perry",26,"M","1997-01-02","60 Airport Boulevard #048-049, Terminal 2 Singapore",355261138,"r.perry@randatmail.com"),
    (5,"Amy Ellis",25,"F","1998-01-02","3 Stadium Walk, Singapura 397692",142266820,"a.ellis@randatmail.com"),
    (6,"Maximillian Thompson",18,"M","2005-01-02","Harare, Zimbabwe",11969896,"m.thompson@randatmail.com"),
    (7,"Naomi Murray",25,"F","1998-01-02","64 Big Rock Cove St. Pueblo, CO 81001",695624873,"n.murray@randatmail.com"),
    (8,"Walter Allen",28,"M","2001-01-02","8 Armstrong Street Olive Branch, MS 38654",138564715,"w.allen@randatmail.com"),
    (9,"Julia Carter",21,"F","2008-01-02","41 North Overlook Street Seymour, IN 47274",426987844,"j.carter@randatmail.com"),
    (10,"Tony Nelson",18,"M","2005-01-02","89 Shady Road Beverly, MA 01915",43381070,"t.nelson@randatmail.com"),
    (11,"Lucia Baker",30,"F","1993-01-02","81 Golden Star St. Irwin, PA 15642",810340478 ,"l.baker@randatmail.com"),
    (12,"Maya Dixon",36,"F","1987-01-02","110 York Street Rock Hill, SC 29730",111192037,"m.dixon@randatmail.com"),
    (13,"Lydia Tucker",33,"F","1990-01-02","4585 Shimerville Rd Clarence, New York(NY), 14031",926400561,"l.tucker@randatmail.com"),
    (14,"Preston Anderson",40,"M","1983-01-02","(870) 535-6166 2913 S Mississippi St Pine Bluff,...",534981197,"p.anderson@randatmail.com"),
    (15,"Ashton Hamilton",40,"M","1983-01-02","105 Harmony Path Bonaire, Georgia(GA), 31005",811509560,"a.hamilton@randatmail.com"),
    (16,"Chester Crawford",3,"M","1984-01-02","2314 Duckett St #APT C Conway, South Carolina(SC)..",419153453,"c.crawford@randatmail.com"),
    (17,"Lyndon Richards",40,"M","1983-01-02","20037 30th Hwy Buhl, Idaho(ID), 83316",379855584,"l.richards@randatmail.com"),
    (18,"Jack Reed",31,"M","1992-01-02","218 S Pine St Batesburg, South Carolina(SC), 2900...",643393572,"j.reed@randatmail.com"),
    (19,"William Farell",32,"M","1991-01-02","1472 Wesley Dr Griffin, Georgia(GA), 30224",556333480,"w.farrell@randatmail.com"),
    (20,"Aline Murphy",31,"F","1992-01-02","16544 NE North Main St Summitville, Indiana(IN), ...",835975603,"a.murphy@randatmail.com")
    ;

insert into booking(Booking_ID,Booking_Date,Flight_Number,Passenger_ID)
Values
    (1,"2023-01-04",1,1),
    (2,"2023-01-03",1,2),
    (3,"2023-01-04",1,3),
    (4,"2023-01-02",2,4),
    (5,"2023-01-01",2,5),
    (6,"2023-01-05",1,6),
    (7,"2023-01-05",2,7),
    (8,"2023-01-02",2,8),
    (9,"2023-01-05",2,9),
    (10,"2023-01-02",2,10),
    (11,"2023-01-04",2,11),
    (12,"2023-01-05",1,12),
    (13,"2023-01-04",2,13),
    (14,"2023-01-05",2,14),
    (15,"2023-01-01",2,15),
    (16,"2023-01-05",2,16),
    (17,"2023-01-05",1,17),
    (18,"2023-01-02",1,18),
    (19,"2023-01-04",1,19),
    (20,"2023-01-05",1,20);

insert into payment(Booking_ID, Payment_Type, Payment_Amount,Payment_Status)
values
    (1,"Cash",25000,"NOT PAID"),
    (2,"Card",0,"PAID"),
    (3,"Cash",30000,"NOT PAID"),
    (4,"Cash",15000,"NOT PAID"),
    (5,"Card",0,"PAID"),
    (6,"Card",0,"PAID"),
    (7,"Card",0,"PAID"),
    (8,"Card",0,"PAID"),
    (9,"Cash",0,"PAID"),
    (10,"Cash",45000,"NOT PAID"),
    (11,"Card",0,"PAID"),
    (12,"Card",0,"PAID"),
    (13,"Card",0,"PAID"),
    (14,"Cash",0,"PAID"),
    (15,"Card",0,"PAID"),
    (16,"Card",0,"PAID"),
    (17,"Card",0,"PAID"),
    (18,"Card",0,"PAID"),
    (19,"Card",0,"PAID"),
    (20,"Cash",50000,"NOT PAID");
