-- Context: Write code in SQL is a nice level up!

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score)
BEGIN
    IF NOT EXISTS(SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects where name = project_name), score);
END;

DELIMITER ;
