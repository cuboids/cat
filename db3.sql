DROP TABLE IF EXISTS Captain;
CREATE TABLE Captain(
    ca_id INTEGER,
    ca_name CHAR(20),
    license_since DATE,
    PRIMARY KEY (ca_id)
);

DROP TABLE IF EXISTS Container;
CREATE TABLE Container(
    co_id INTEGER,
    content CHAR(20),
    PRIMARY KEY (co_id)
);

DROP TABLE IF EXISTS Ship;
CREATE TABLE Ship(
    s_id INTEGER,
    created_at DATE,
    s_name CHAR(20),
    PRIMARY KEY (s_id)
);


/* We have added a transport id to the transports relationship.
   This helps to distinguish multiple transports involving the
   same ship, captain, and container. Furthermore, we assume
   that each container has a unique ID (like real containers
   have). */

DROP TABLE IF EXISTS transports;
CREATE TABLE transports(
    t_id INTEGER, -- We include a transport ID
    ca_id INTEGER,
    s_id INTEGER,
    co_id INTEGER,
    PRIMARY KEY (t_id, ca_id, s_id, co_id),
    UNIQUE (t_id, co_id), -- Each container is shipped by 1 ship and 1 captain.
    FOREIGN KEY (ca_id) REFERENCES Captain,
    FOREIGN KEY (co_id) REFERENCES Container,
    FOREIGN KEY (s_id) REFERENCES Ship
);

/* For each container at a particular transport, the
   destination is recorded. */

DROP TABLE IF EXISTS has_as_destination;
CREATE TABLE has_as_destination(
    t_id INTEGER,
    co_id INTEGER,
    l_id INTEGER,
    PRIMARY KEY (t_id, co_id),
    FOREIGN KEY (t_id) REFERENCES transports,
    FOREIGN KEY (l_id) REFERENCES Location
);

DROP TABLE IF EXISTS departs_to;
CREATE TABLE departs_to(
    ca_id INTEGER,
    co_id INTEGER,
    s_id INTEGER,
    l_id INTEGER,
    PRIMARY KEY (ca_id, co_id, s_id, l_id),
    FOREIGN KEY (ca_id) REFERENCES Captain,
    FOREIGN KEY (co_id) REFERENCES Container,
    FOREIGN KEY (s_id) REFERENCES Ship,
    FOREIGN KEY (l_id) REFERENCES Location
);

DROP TABLE IF EXISTS Location;
CREATE TABLE Location(
    l_id INTEGER,
    l_name CHAR(20),
    PRIMARY KEY(l_id)
)
