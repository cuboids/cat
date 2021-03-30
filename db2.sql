DROP TABLE IF EXISTS Author;
CREATE TABLE Author(
    a_id INTEGER,
    a_name CHR(20),
    a_age INTEGER,
    d_id INTEGER,
    PRIMARY KEY (a_id),
);

CREATE TABLE owns(
    a_id INTEGER,
    d_id INTEGER,
    PRIMARY KEY (a_id, d_id),
    FOREIGN KEY (a_id) REFERENCES Author(a_id),
    FOREIGN KEY (d_id) REFERENCES Document(d_id)
);

DROP TABLE IF EXISTS Document;
CREATE TABLE Document(
    d_id INTEGER,
    DOI CHR(30),
    PRIMARY KEY (d_id),
    UNIQUE(DOI)
);

DROP TABLE IF EXISTS Patent;
CREATE TABLE Patent(
    d_id INTEGER,
    type CHR(20),
    PRIMARY KEY (d_id),
    FOREIGN KEY (d_id) REFERENCES Document ON DELETE CASCADE
);

DROP TABLE IF EXISTS ScientArt;
CREATE TABLE ScientArt(
    d_id INTEGER,
    nr_references INTEGER,
    year INTEGER,
    j_id INTEGER,
    PRIMARY KEY (d_id),
    FOREIGN KEY (d_id) REFERENCES DOCUMENT ON DELETE CASCADE,
    FOREIGN KEY (j_id) REFERENCES Journal(j_id)
);

DROP TABLE IF EXISTS Journal;
CREATE TABLE Journal(
    j_id INTEGER,
    j_name CHR(20),
    field_of_study CHR(20),
    PRIMARY KEY (j_id)
);

DROP TABLE IF EXISTS Reviewed;
CREATE TABLE Reviewed(
    p_name CHAR(20),
    d_id INTEGER NOT NULL,
    p_job CHAR(20),
    PRIMARY KEY (p_name, d_id),
    FOREIGN KEY (d_id) REFERENCES ScientArt(d_id) ON DELETE CASCADE
)
