-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DELIMITER $$

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
