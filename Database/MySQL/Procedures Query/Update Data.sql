USE Falcon_Cyber_Monitoring_System;
DROP PROCEDURE IF EXISTS UpdateData;
DELIMITER &&
CREATE PROCEDURE UpdateData (
    IN `U_CHANNEL` VARCHAR(128),
    IN `U_ID` INT(11) UNSIGNED,
    IN `U_FROM_ID` VARCHAR(32),
    IN `U_DATE` int(11) UNSIGNED,
    IN `U_MESSAGE` TEXT,
    IN `U_VIEWS` int(11) UNSIGNED,
    IN `U_EDIT_DATE` int(11) UNSIGNED,
    IN `U_SYMBOL_NAME` VARCHAR(64),
    IN `U_SYMBOL_TYPE` VARCHAR(64),
    IN `U_SIGNAL_POLARITY` float,
    IN `U_PERCENTAGE_CHANGE` float
    )
BEGIN
    UPDATE Data
    SET DATE = U_DATE, MESSAGE = U_MESSAGE,
        VIEWS = U_VIEWS, EDIT_DATE = U_EDIT_DATE,
        SYMBOL_NAME = U_SYMBOL_NAME, SYMBOL_TYPE = U_SYMBOL_TYPE,
        SIGNAL_POLARITY = U_SIGNAL_POLARITY,
        PERCENTAGE_CHANGE = U_PERCENTAGE_CHANGE,
        REG_DATE = CURRENT_TIMESTAMP
    WHERE CHANNEL = U_CHANNEL AND ID = U_ID AND FROM_ID = U_FROM_ID;
END &&
DELIMITER ;