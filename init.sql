CREATE DATABASE plc_prototype;

USE plc_prototype;

CREATE TABLE member (
    idx           INT auto_increment NOT NULL COMMENT 'index',
    user_email    VARCHAR(100) NOT NULL COMMENT 'email',
    user_password VARCHAR(100) NOT NULL COMMENT 'password',
    PRIMARY KEY (idx, user_email)
)
ENGINE=InnoDB COMMENT='user information';

INSERT INTO member (user_email, user_password) VALUES('user@user.com', 'userpassword');
COMMIT;