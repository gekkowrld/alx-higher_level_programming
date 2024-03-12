-- Don't let Bob cheat, so punish him by removing some marks

UPDATE second_table
SET score = 10
WHERE name = "Bob";
