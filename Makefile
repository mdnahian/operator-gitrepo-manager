LOADER_BUILD_VERSION := latest
LOADER_IMAGE_NAME := gitrepo-loader
LOADER_FULL_IMAGE_NAME = $(LOADER_IMAGE_NAME):$(LOADER_BUILD_VERSION)

.PHONY: build

build:
	docker build --tag $(LOADER_FULL_IMAGE_NAME) -f ./loader/build/Dockerfile .

run:
	docker run -e REPOSITORY_URL=https://github.com/operator-framework/community-operators.git -e OPERATOR_BUNDLE_DIR=prometheus -it $(LOADER_FULL_IMAGE_NAME) bash