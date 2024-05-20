.PHONY: help build up start down destroy stop restart logs logs-api ps

NO_GPU_FILENAME=

ifeq ($(NO_GPU), 1)
	NO_GPU_FILENAME=_no_gpu
endif

build:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml  build $(c)
up:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml up -d $(c)
	docker exec -d ollama ollama run llama3
start:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml start $(c)
down:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml down $(c)
destroy:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml down -v $(c)
stop:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml stop $(c)
restart:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml stop $(c)
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml up -d $(c)
logs:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml logs --tail=100 -f $(c)
ps:
	docker-compose -f docker-compose${NO_GPU_FILENAME}.yml ps
