USE Falcon_Cyber_Monitoring_System;
DROP PROCEDURE IF EXISTS ShowAllData;
DELIMITER &&
CREATE PROCEDURE ShowAllData ()
BEGIN
    SELECT * FROM Signals;
END &&
DELIMITER ;