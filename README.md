REST API
--------

This service sits between all the microservices and the outside world.

The structure of the service is inside app each directory bar main corrosponds to a service and inside that directory are a number of blueprints which map to sets of url which forward requests to that service.

This service also handles generating JWT Tokens and validating them. When the service recieves a valid JWT token the School-Id, User-Id and Permissions from that token are forwarded to any other service calls in the header.

