CREATE TABLE problems (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE,
    name TEXT NOT NULL,
    problem_number INTEGER UNIQUE,
    is_archived BOOLEAN DEFAULT 0
);
CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE problem_tags (
    problem_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (problem_id, tag_id),
    FOREIGN KEY(problem_id) REFERENCES problems(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id)
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    problem_id INTEGER NOT NULL,
    quality INTEGER NOT NULL,
    easiness REAL,
    interval INTEGER,
    reps INTEGER DEFAULT 0,
    review_datetime TEXT NOT NULL,
    post_mortem TEXT,
    FOREIGN KEY(problem_id) REFERENCES problems(id)
);
