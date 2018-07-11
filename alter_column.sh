
for i in `seq 0 255`;do
sql="ALTER TABLE \`tag\`.\`tag_pid_$i\` CHANGE COLUMN \`key1\` \`key\` VARCHAR(64) NOT NULL ;"
/usr/local/mysql/bin/mysql --login-path=root_local tag -e "$sql"

done