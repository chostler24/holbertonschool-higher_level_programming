-- creates user_0d_1 with all privileges
CREATE USER IF NOT EXISTS user_0d_1;
GRANT ALL PRIVILEGES ON mysql TO user_0d_1;
IDENTIFIED BY user_0d_1_pwd;
