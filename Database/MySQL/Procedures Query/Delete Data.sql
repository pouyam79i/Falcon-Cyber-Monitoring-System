USE Falcon_Cyber_Monitoring_System;
DROP PROCEDURE IF EXISTS DelData;
DELIMITER &&
CREATE PROCEDURE DelData (
    IN `CHANNEL` VARCHAR(128),
    IN `ID` INT(11) UNSIGNED,
    IN `FROM_ID` VARCHAR(32)
    )
BEGIN
    DELETE FROM Signals
    WHERE Signals.CHANNEL = CHANNEL AND Signals.ID = ID AND Signals.FROM_ID = FROM_ID;
END &&
DELIMITER ;