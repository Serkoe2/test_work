docker-redis=docker-redis.yml

local_up:
	docker-compose -f $(redis)  up -d

.PHONY: local_up