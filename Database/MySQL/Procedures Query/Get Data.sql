USE Falcon_Cyber_Monitoring_System;
DROP PROCEDURE IF EXISTS GetData;
DELIMITER &&
CREATE PROCEDURE GetData (
    IN `I_CHANNEL` VARCHAR(128),
    IN `I_ID` INT(11) UNSIGNED,
    IN `I_FROM_ID` VARCHAR(32),
    OUT `O_DATE` int(11) UNSIGNED,
    OUT `O_MESSAGE` TEXT,
    OUT `O_VIEWS` int(11) UNSIGNED,
    OUT `O_EDIT_DATE` int(11) UNSIGNED,
    OUT `O_SYMBOL_NAME` VARCHAR(64),
    OUT `O_SYMBOL_TYPE` VARCHAR(64),
    OUT `O_SIGNAL_POLARITY` float,
    OUT `O_PERCENTAGE_CHANGE` float,
    OUT `O_REG_DATE` TIMESTAMP
    )
BEGIN
    SELECT DATE, MESSAGE, VIEWS, EDIT_DATE,
           SYMBOL_NAME, SYMBOL_TYPE,SIGNAL_POLARITY,
           PERCENTAGE_CHANGE, REG_DATE
    INTO O_DATE, O_MESSAGE, O_VIEWS, O_EDIT_DATE,
        O_SYMBOL_NAME, O_SYMBOL_TYPE, O_SIGNAL_POLARITY,
        O_PERCENTAGE_CHANGE, O_REG_DATE
    FROM Signals
    WHERE CHANNEL = I_CHANNEL AND ID = I_ID AND FROM_ID = I_FROM_ID;
END &&
DELIMITER ;