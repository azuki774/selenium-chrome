container_name=selenium-chrome
.PHONY: build
build:
	docker build -t azuki774/selenium-chrome -f build/Dockerfile .
