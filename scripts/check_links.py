import os
import re
from bs4 import BeautifulSoup
import sys


def validate_internal_links(site_dir):
    """
    Rudimentary internal link validator for Jekyll _site output.
    """
    if not os.path.exists(site_dir):
        print(f"Error: {site_dir} does not exist. Build the site first.")
        return False

    errors = []
    html_files = []

    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    print(f"Checking {len(html_files)} HTML files for broken internal links...")

    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

            for link in soup.find_all("a", href=True):
                href = link["href"]

                # We only care about internal links
                if (
                    href.startswith("http")
                    or href.startswith("//")
                    or href.startswith("mailto:")
                    or href.startswith("#")
                ):
                    continue

                # Construct the path to the target file
                # Strip baseurl if present (this is a simple approximation)
                # You might need to adjust this depending on how Jekyll is configured
                clean_href = href.split("?")[0].split("#")[0]

                if not clean_href:
                    continue

                target_path = ""
                if clean_href.startswith("/"):
                    # Absolute from site root
                    target_path = os.path.join(site_dir, clean_href.lstrip("/"))
                else:
                    # Relative
                    target_path = os.path.normpath(
                        os.path.join(os.path.dirname(file_path), clean_href)
                    )

                # Check if it's a directory (Jekyll often uses folder/ instead of folder/index.html)
                if os.path.isdir(target_path):
                    target_path = os.path.join(target_path, "index.html")

                if not os.path.exists(target_path):
                    errors.append(
                        f"Broken link in {os.path.relpath(file_path, site_dir)}: {href} (Target not found: {os.path.relpath(target_path, site_dir)})"
                    )

    if errors:
        print("\nFound broken links:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nNo broken internal links found!")
        return True


if __name__ == "__main__":
    site_root = "_site"
    if len(sys.argv) > 1:
        site_root = sys.argv[1]

    success = validate_internal_links(site_root)
    sys.exit(0 if success else 1)
