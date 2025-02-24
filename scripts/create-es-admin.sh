AUTH_USERNAME=elastic
AUTH_PASSWORD=elastic


curl -X POST "elastic:elastic@localhost:9200/_security/user/admin" -H 'Content-Type: application/json' -d '{
  "password" : "admin123",
  "roles" : [ "admin" ],
  "full_name" : "Admin User",
  "email" : "admin@example.com"
}'


curl -X POST "elastic:elastic@localhost:9200/_security/user/super" -H 'Content-Type: application/json' -d '{
  "password" : "admin123",
  "roles" : [ "superuser" ],
  "full_name" : "Super User",
  "email" : "super@example.com"
}'
