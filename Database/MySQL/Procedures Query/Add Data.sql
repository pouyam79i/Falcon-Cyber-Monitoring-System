USE Falcon_Cyber_Monitoring_System;
DROP PROCEDURE IF EXISTS AddData;
DELIMITER &&
CREATE PROCEDURE AddData (
    IN `N_CHANNEL` VARCHAR(128),
    IN `N_ID` INT(11) UNSIGNED,
    IN `N_FROM_ID` VARCHAR(32),
    IN `N_DATE` int(11) UNSIGNED,
    IN `N_MESSAGE` TEXT,
    IN `N_VIEWS` int(11) UNSIGNED,
    IN `N_EDIT_DATE` int(11) UNSIGNED,
    IN `N_SYMBOL_NAME` VARCHAR(64),
    IN `N_SYMBOL_TYPE` VARCHAR(64),
    IN `N_SIGNAL_POLARITY` float,
    IN `N_PERCENTAGE_CHANGE` float
    )
BEGIN
    INSERT INTO Data(CHANNEL, ID, FROM_ID, DATE, MESSAGE, VIEWS, EDIT_DATE, SYMBOL_NAME, SYMBOL_TYPE, SIGNAL_POLARITY, PERCENTAGE_CHANGE)
    VALUES (N_CHANNEL, N_ID, N_FROM_ID, N_DATE, N_MESSAGE, N_VIEWS, N_EDIT_DATE, N_SYMBOL_NAME, N_SYMBOL_TYPE, N_SIGNAL_POLARITY, N_PERCENTAGE_CHANGE);
END &&
DELIMITER ;