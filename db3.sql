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

DROP TABLE IF EXISTS transports;
CREATE TABLE transports(
    ca_id INTEGER,
    co_id INTEGER,
    s_id INTEGER,
    PRIMARY KEY (ca_id, co_id, s_id),
    FOREIGN KEY (ca_id) REFERENCES Captain,
    FOREIGN KEY (co_id) REFERENCES Container,
    FOREIGN KEY (s_id) REFERENCES Ship
);

DROP TABLE IF EXISTS has_as_destination;
CREATE TABLE has_as_destination(
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
