.PHONY: all clean serve module week

all:
	@echo "Available commands:"
	@echo "  make serve      - Run Jekyll server"
	@echo "  make module NAME=name - Create a new module"
	@echo "  make week NUM=n   - Create a new week"

serve:
	bundle exec jekyll serve --livereload

module:
	python3 scripts/scaffold.py module $(NAME)

week:
	python3 scripts/scaffold.py week $(NUM)

clean:
	rm -rf _site
